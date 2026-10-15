import time
from utils import build_messages, load_model, load_state_value, load_tokenizer, log_instruction_use, memory_derived_ctx, pick_model, save_state_value, strip_think, wait_while_stopped, next_free_path
import settings

def run_completion(llm, messages):
    if settings.PRINT_PROCESSING_PROMPT:
        for message in messages:
            print(message["content"])
    start_time = time.perf_counter()
    try:
        result = llm.create_chat_completion(messages=messages, max_tokens=settings.MAX_TOKENS, temperature=0.6, top_p=0.95, top_k=20, presence_penalty=1.0)
    except ValueError as error:
        print(f"Warning: {error}")
        return None
    usage = result["usage"]
    if settings.PRINT_TOKEN_USAGE:
        print(f"Prompt tokens: {usage['prompt_tokens']}, completion tokens: {usage['completion_tokens']}, n_ctx: {llm.n_ctx()}")
    if settings.PRINT_GENERATION_SPEED:
        elapsed = time.perf_counter() - start_time
        tokens_per_second = usage["completion_tokens"] / elapsed if elapsed > 0 else 0.0
        print(f"Generated {usage['completion_tokens']} tokens in {elapsed:.2f}s ({tokens_per_second:.2f} tok/s)")
    choice = result["choices"][0]
    if choice["finish_reason"] == "length":
        print("Warning: generation filled the context, output was cut off.")
    return choice["message"]["content"].strip()

def build_user_prompt(line, context=None):
    parts = []
    if context:
        parts.append(context)
    parts.append(f"Input content: <context>\"{line}\"</context>")
    parts.append(f"Instruction: <instruction>{settings.REQUEST}</instruction>")
    return "\n".join(parts)

def build_process_prompt(line, context=None):
    return settings.BASE + "\n" + build_user_prompt(line, context)

def process_line(llm, line, context=None):
    messages = build_messages(settings.BASE, build_user_prompt(line, context), build_process_prompt(line, context))
    return run_completion(llm, messages)

def write_output(outfile, output):
    if not load_state_value("keep_thinking", bool):
        output = strip_think(output)
    output = "\n".join(line for line in output.split("\n") if line.strip() != "")
    print(output)
    if output:
        outfile.write(output + "\n")
        outfile.flush()
    return output

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

def build_prev_output_context(prev_output):
    if prev_output is None:
        return None
    truncated = prev_output[max(0, len(prev_output) - settings.PREV_OUTPUT_CONTEXT_CHARS):]
    if not truncated:
        return None
    return f"Output from previous request as context: \"{truncated}\""

def abort_oversized_segment(segment, tokens, n_ctx):
    preview = " ".join(" ".join(segment).split()[:10])
    print(f"\nSegment with {tokens} prompt tokens leaves too little of the {n_ctx} token context for thinking and answer:")
    print(f"\"{preview}...\"")
    print("Cancel and rework the input file.")
    raise SystemExit(1)

def segment_token_counts(llm, segments, use_prev_output):
    context = build_prev_output_context("x") if use_prev_output else None
    extra = settings.PREV_OUTPUT_CONTEXT_CHARS if use_prev_output else 0
    counts = []
    for segment in segments:
        if segment is None:
            continue
        prompt = build_process_prompt("\n".join(segment), context)
        counts.append((segment, len(llm.tokenize(prompt.encode("utf-8"), add_bos=False)) + extra))
    return counts

def longest_prompt_tokens(model, segments, use_prev_output):
    tokenizer_llm = load_tokenizer(model)
    counts = segment_token_counts(tokenizer_llm, segments, use_prev_output)
    del tokenizer_llm
    return max((tokens for _, tokens in counts), default=0)

def check_segments_fit(llm, segments, use_prev_output):
    n_ctx = llm.n_ctx()
    max_prompt = int(n_ctx * settings.PROMPT_MAX_FRACTION)
    for segment, tokens in segment_token_counts(llm, segments, use_prev_output):
        if tokens >= max_prompt:
            abort_oversized_segment(segment, tokens, n_ctx)

def process_segments(llm, segments, outfile, use_prev_output):
    last_output = None
    for segment in segments:
        if segment is None:
            outfile.write("\n")
            outfile.flush()
            continue
        wait_while_stopped()
        context = build_prev_output_context(last_output) if use_prev_output else None
        output = process_line(llm, "\n".join(segment), context)
        if output is None:
            print(f"Warning: segment starting with \"{segment[0][:60]}\" could not be processed.")
            continue
        last_output = write_output(outfile, output)

def pick_request():
    last_instruction = load_state_value("instruction", str)
    last_sample = " ".join(last_instruction.split())[:65] if last_instruction else "none saved"
    print("m/c: Enter instruction manually.")
    print(f"l: Last used instruction: {last_sample}")
    for i, request in enumerate(settings.REQUESTS, 1):
        sample = " ".join(request.split())[:92]
        print(f"{i}: {sample}")
    choice = input(f"Pick an instruction [1-{len(settings.REQUESTS)}, m/c, l]: ").strip().lower()
    if choice == "m" or choice == "c":
        custom = input("Enter instruction: ").strip()
        settings.REQUEST = custom if custom else "Tell a joke."
    elif choice == "l":
        settings.REQUEST = last_instruction
    else:
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(settings.REQUESTS):
                raise ValueError
        except ValueError:
            index = 0
        settings.REQUEST = settings.REQUESTS[index]
    save_state_value("instruction", settings.REQUEST)
    log_instruction_use(settings.REQUEST)

def main():
    model = pick_model()
    pick_request()
    segment_mode = input("Use segment mode or line mode? [Y/n]: ").strip().lower() in ("y", "yes", "")
    use_prev_output = input("Include previous output as context? [y/N]: ").strip().lower() in ("y", "yes")
    with open(settings.INPUT_FILE, "r", encoding="utf-8") as infile:
        segments = read_segments(infile) if segment_mode else read_line_segments(infile)
    n_ctx = memory_derived_ctx(model, longest_prompt_tokens(model, segments, use_prev_output))
    print(f"Using context window of {n_ctx} tokens.")
    llm = load_model(model, c_ntx=n_ctx)
    check_segments_fit(llm, segments, use_prev_output)
    output_path = next_free_path(settings.OUTPUT_FILE_TEMPLATE)
    print(f"Writing output to {output_path}.")
    with open(output_path, "x", encoding="utf-8") as outfile:
        process_segments(llm, segments, outfile, use_prev_output)

if __name__ == "__main__":
    main()
