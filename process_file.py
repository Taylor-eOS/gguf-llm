import time
from pathlib import Path
from utils import is_cached, load_model, load_tokenizer, log_instruction_use, pick_model, strip_think
import settings

input_file = "input.txt"
output_file = "output.txt"
PREV_OUTPUT_CONTEXT_CHARS = 400

def run_completion(llm, prompt):
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    if settings.PRINT_TOKEN_USAGE:
        prompt_tokens = len(llm.tokenize(prompt.encode("utf-8"), add_bos=False))
        n_ctx = llm.n_ctx()
        total = prompt_tokens + settings.MAX_TOKENS
        print(f"Prompt tokens: {prompt_tokens}, n_ctx: {n_ctx}, prompt_tokens + MAX_TOKENS: {total}")
        if total > n_ctx:
            print(f"Warning: prompt_tokens + MAX_TOKENS exceeds n_ctx by {total - n_ctx} tokens, completion may be cut off.")
    start_time = time.perf_counter()
    result = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], max_tokens=settings.MAX_TOKENS, temperature=0.7, top_p=0.9,)
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

def read_lines(infile):
    lines = []
    for raw_line in infile:
        line = raw_line.rstrip("\n")
        lines.append(line)
    return lines

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

def longest_line_tokens(llm, lines):
    longest = 0
    for line in lines:
        tokens = len(llm.tokenize(line.encode("utf-8"), add_bos=False))
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
    truncated = prev_output[:PREV_OUTPUT_CONTEXT_CHARS]
    if not truncated:
        return None
    return f"Output from previous request (as context): \"{truncated}\""

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
        tokens = segment_token_count(llm, segment)
        if tokens > budget:
            abort_oversized_segment(segment, tokens, budget)
        context = build_prev_output_context(last_output) if use_prev_output else None
        output = process_line(llm, "\n".join(segment), context)
        write_output(outfile, output)
        last_output = output

def process_lines(llm, lines, outfile, use_prev_output):
    last_output = None
    for line in lines:
        if line.strip() == "":
            outfile.write("\n")
            outfile.flush()
        else:
            context = build_prev_output_context(last_output) if use_prev_output else None
            output = process_line(llm, line, context)
            write_output(outfile, output)
            last_output = output

def pick_request():
    manual_option = 1
    print(f"{manual_option}: Enter instruction manually.")
    for i, request in enumerate(settings.REQUESTS, 2):
        sample = " ".join(request.split()[:10])
        print(f"{i}: {sample}...")
    choice = input(f"Pick an instruction [1-{len(settings.REQUESTS) + 1}]: ").strip()
    try:
        index = int(choice) - 1
        if index < 0 or index > len(settings.REQUESTS):
            raise ValueError
    except ValueError:
        index = 1
    if index == 0:
        custom = input("Enter instruction: ").strip()
        settings.REQUEST = custom if custom else settings.REQUESTS[0]
    else:
        settings.REQUEST = settings.REQUESTS[index - 1]
    log_instruction_use(settings.REQUEST)

def measure_required_ctx(model, segment_mode, segments, lines):
    tokenizer_llm = load_tokenizer(model)
    if segment_mode:
        longest_tokens = longest_segment_tokens(tokenizer_llm, segments)
    else:
        longest_tokens = longest_line_tokens(tokenizer_llm, lines)
    required_ctx = compute_required_ctx(tokenizer_llm, longest_tokens)
    del tokenizer_llm
    return required_ctx

def main():
    model = pick_model()
    _segment_mode = input("Use segment mode? [Y/n]: ").strip().lower()
    _segment_mode = _segment_mode if _segment_mode in ("y", "yes", "") else "n"
    _segment_mode = _segment_mode in ("y", "yes", "")
    pick_request()
    _use_prev_output = input("Include previous output as context? [y/N]: ").strip().lower()
    use_prev_output = _use_prev_output in ("y", "yes")
    with open(input_file, "r", encoding="utf-8") as infile:
        if _segment_mode:
            segments = read_segments(infile)
            lines = None
        else:
            segments = None
            lines = read_lines(infile)
    required_ctx = measure_required_ctx(model, _segment_mode, segments, lines)
    print(f"Using context window of {required_ctx} tokens.")
    llm = load_model(model, c_ntx=required_ctx)
    with open(output_file, "w", encoding="utf-8") as outfile:
        if _segment_mode:
            budget = compute_budget(llm, required_ctx)
            process_segments(llm, segments, outfile, budget, use_prev_output)
        else:
            process_lines(llm, lines, outfile, use_prev_output)

if __name__ == "__main__":
    main()
