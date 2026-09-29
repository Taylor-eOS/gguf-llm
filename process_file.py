import time
from pathlib import Path
from utils import is_cached, load_model, load_tokenizer, log_instruction_use, pick_model, strip_think, wait_while_stopped, load_last_instruction, save_last_instruction
import settings

def run_completion(llm, prompt):
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    raw_tokens = len(llm.tokenize(prompt.encode("utf-8"), add_bos=False))
    n_ctx = llm.n_ctx()
    if settings.PRINT_TOKEN_USAGE:
        print(f"Raw prompt tokens: {raw_tokens}, n_ctx: {n_ctx}, raw + MAX_TOKENS: {raw_tokens + settings.MAX_TOKENS}")
    start_time = time.perf_counter()
    result = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], max_tokens=settings.MAX_TOKENS, temperature=0.7, top_p=0.9)
    consumed = result["usage"]["prompt_tokens"]
    if consumed < raw_tokens:
        print(f"Warning: the model consumed {consumed} prompt tokens but the raw prompt has {raw_tokens}. The input was truncated.")
    if settings.PRINT_GENERATION_SPEED:
        elapsed = time.perf_counter() - start_time
        completion_tokens = result["usage"]["completion_tokens"]
        tokens_per_second = completion_tokens / elapsed if elapsed > 0 else 0.0
        print(f"Generated {completion_tokens} tokens in {elapsed:.2f}s ({tokens_per_second:.2f} tok/s)")
    content = result["choices"][0]["message"]["content"].strip()
    if not Path(settings.KEEP_THINKING_FLAG).is_file():
        content = strip_think(content)
    return content

def build_process_prompt(line, context=None):
    parts = []
    if context:
        parts.append(context)
    parts.append(f"Input content: \"{line}\"")
    parts.append(settings.BASE)
    parts.append(f"{settings.TASK_LINE}: {settings.REQUEST}\nProcessed:")
    return "\n".join(parts)

def process_line(llm, line, context=None):
    return run_completion(llm, build_process_prompt(line, context))

def write_output(outfile, output):
    output = "\n".join(line for line in output.split("\n") if line.strip() != "")
    print(output)
    if output:
        outfile.write(output + "\n")
        outfile.flush()

def read_segments(infile):
    segments = []
    paragraph_lines = []
    for raw_line in infile:
        line = raw_line.rstrip("\n")
        if line.strip() == "":
            if paragraph_lines:
                segments.append(paragraph_lines)
                paragraph_lines = []
            segments.append(None)
        else:
            paragraph_lines.append(line)
    if paragraph_lines:
        segments.append(paragraph_lines)
    return segments

def read_line_segments(infile):
    segments = []
    for raw_line in infile:
        line = raw_line.rstrip("\n")
        segments.append(None if line.strip() == "" else [line])
    return segments

def segment_token_count(llm, paragraph_lines):
    return len(llm.tokenize("\n".join(paragraph_lines).encode("utf-8"), add_bos=False))

def prompt_overhead_tokens(llm):
    return len(llm.tokenize((f"Input content: \"\"\n{settings.BASE}\n[{settings.TASK_LINE}: {settings.REQUEST}]\nResponse:").encode("utf-8"), add_bos=False))

def compute_budget(llm, n_ctx):
    overhead = prompt_overhead_tokens(llm)
    return n_ctx - settings.RESERVE_TOKENS - overhead

def longest_segment_tokens(llm, segments):
    longest = 0
    for segment in segments:
        if segment is None:
            continue
        tokens = segment_token_count(llm, segment)
        if tokens > longest:
            longest = tokens
    return longest

def compute_required_ctx(llm, longest_input_tokens):
    overhead = prompt_overhead_tokens(llm)
    required = overhead + settings.RESERVE_TOKENS + longest_input_tokens
    required = max(required, settings.N_CTX_MIN)
    required = min(required, settings.N_CTX_MAX)
    return required

def build_prev_output_context(prev_output):
    if prev_output is None:
        return None
    truncated = prev_output[:settings.PREV_OUTPUT_CONTEXT_CHARS]
    if not truncated:
        return None
    return f"Output from previous request as context: \"{truncated}\""

def abort_oversized_segment(segment, tokens, budget):
    preview = " ".join(" ".join(segment).split()[:10])
    print(f"\nSegment with {tokens} tokens exceeds the budget of {budget}:")
    print(f"\"{preview}...\"")
    print("Cancel and rework the input file.")
    raise SystemExit(1)

def process_segments(llm, segments, outfile, budget, use_prev_output):
    last_output = None
    for segment in segments:
        if segment is None:
            outfile.write("\n")
            outfile.flush()
            continue
        wait_while_stopped()
        tokens = segment_token_count(llm, segment)
        if tokens > budget:
            abort_oversized_segment(segment, tokens, budget)
        context = build_prev_output_context(last_output) if use_prev_output else None
        output = process_line(llm, "\n".join(segment), context)
        write_output(outfile, output)
        last_output = output

def pick_request():
    last_instruction = load_last_instruction()
    last_sample = " ".join(last_instruction.split())[:65] if last_instruction else "none saved"
    print("M: Enter instruction manually.")
    print(f"L: Last used instruction: {last_sample}")
    for i, request in enumerate(settings.REQUESTS, 1):
        sample = " ".join(request.split())[:92]
        print(f"{i}: {sample}")
    choice = input(f"Pick an instruction [1-{len(settings.REQUESTS)}, M, L]: ").strip().lower()
    if choice == "m":
        custom = input("Enter instruction: ").strip()
        settings.REQUEST = custom if custom else settings.REQUESTS[0]
    elif choice == "l":
        if last_instruction is None:
            print("No last used instruction saved, using the first predefined one.")
            settings.REQUEST = settings.REQUESTS[0]
        else:
            settings.REQUEST = last_instruction
    else:
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(settings.REQUESTS):
                raise ValueError
        except ValueError:
            index = 0
        settings.REQUEST = settings.REQUESTS[index]
    save_last_instruction(settings.REQUEST)
    log_instruction_use(settings.REQUEST)

def measure_required_ctx(model, segments):
    tokenizer_llm = load_tokenizer(model)
    longest_tokens = longest_segment_tokens(tokenizer_llm, segments)
    required_ctx = compute_required_ctx(tokenizer_llm, longest_tokens)
    del tokenizer_llm
    return required_ctx

def main():
    model = pick_model()
    pick_request()
    segment_mode = input("Use segment mode? [Y/n]: ").strip().lower() in ("y", "yes", "")
    use_prev_output = input("Include previous output as context? [y/N]: ").strip().lower() in ("y", "yes")
    with open(settings.INPUT_FILE, "r", encoding="utf-8") as infile:
        segments = read_segments(infile) if segment_mode else read_line_segments(infile)
    required_ctx = measure_required_ctx(model, segments)
    print(f"Using context window of {required_ctx} tokens.")
    llm = load_model(model, c_ntx=required_ctx)
    budget = compute_budget(llm, required_ctx)
    with open(settings.OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        process_segments(llm, segments, outfile, budget, use_prev_output)

if __name__ == "__main__":
    main()
