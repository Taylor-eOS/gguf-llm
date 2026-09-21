from utils import load_model, load_tokenizer, log_instruction_use, pick_model, split_lines_by_tokens, strip_think
from process_file import compute_required_ctx, prompt_overhead_tokens, read_segments, segment_token_count, write_output
import settings

input_file = "input.txt"
summaries_file = "summaries.txt"
output_file = "output.txt"

def process_line(llm, line, prev_summary, next_summary):
    parts = []
    if prev_summary is not None:
        parts.append(f"Summary of previous segment: \"{prev_summary}\"")
    if next_summary is not None:
        parts.append(f"Summary of following segment: \"{next_summary}\"")
    parts.append(f"Input content: \"{line}\"")
    parts.append(settings.BASE)
    parts.append(f"Task: {settings.REQUEST}\nProcessed:")
    prompt = "\n".join(parts)
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    result = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=settings.MAX_TOKENS,
        temperature=0.7,
        top_p=0.9,
    )
    content = result["choices"][0]["message"]["content"].strip()
    if settings.STRIP_THINKING:
        content = strip_think(content)
    return content

def read_summaries(infile):
    summaries = []
    paragraph_lines = []
    for raw_line in infile:
        line = raw_line.rstrip("\n")
        if line.strip() == "":
            if paragraph_lines:
                summaries.append(" ".join(paragraph_lines))
                paragraph_lines = []
        else:
            paragraph_lines.append(line)
    if paragraph_lines:
        summaries.append(" ".join(paragraph_lines))
    return summaries

def align_summaries_to_segments(segments, summaries):
    aligned = []
    summary_index = 0
    for segment in segments:
        if segment is None:
            aligned.append(None)
        else:
            if summary_index >= len(summaries):
                raise ValueError("summaries.txt has fewer segments than input.txt")
            aligned.append(summaries[summary_index])
            summary_index += 1
    if summary_index != len(summaries):
        raise ValueError("summaries.txt has more segments than input.txt")
    return aligned

def neighbor_summaries(aligned_summaries, segment_index):
    prev_summary = None
    for i in range(segment_index - 1, -1, -1):
        if aligned_summaries[i] is not None:
            prev_summary = aligned_summaries[i]
            break
    next_summary = None
    for i in range(segment_index + 1, len(aligned_summaries)):
        if aligned_summaries[i] is not None:
            next_summary = aligned_summaries[i]
            break
    return prev_summary, next_summary

def longest_segment_with_summaries_tokens(llm, segments, aligned_summaries):
    longest = 0
    for i, segment in enumerate(segments):
        if segment is None:
            continue
        prev_summary, next_summary = neighbor_summaries(aligned_summaries, i)
        extra_parts = []
        if prev_summary is not None:
            extra_parts.append(f"Summary of previous segment: \"{prev_summary}\"")
        if next_summary is not None:
            extra_parts.append(f"Summary of following segment: \"{next_summary}\"")
        extra_tokens = len(llm.tokenize("\n".join(extra_parts).encode("utf-8"), add_bos=False)) if extra_parts else 0
        tokens = segment_token_count(llm, segment) + extra_tokens
        if tokens > longest:
            longest = tokens
    return longest

def measure_required_ctx(model, segments, aligned_summaries):
    tokenizer_llm = load_tokenizer(model)
    longest_tokens = longest_segment_with_summaries_tokens(tokenizer_llm, segments, aligned_summaries)
    required_ctx = compute_required_ctx(tokenizer_llm, longest_tokens)
    del tokenizer_llm
    return required_ctx

def compute_budget(llm, n_ctx, prev_summary, next_summary):
    parts = []
    if prev_summary is not None:
        parts.append(f"Summary of previous segment: \"{prev_summary}\"")
    if next_summary is not None:
        parts.append(f"Summary of following segment: \"{next_summary}\"")
    parts.append(f"Input content: \"\"")
    parts.append(settings.BASE)
    parts.append(f"Task: {settings.REQUEST}\nProcessed:")
    overhead = len(llm.tokenize("\n".join(parts).encode("utf-8"), add_bos=False))
    return n_ctx - settings.MAX_TOKENS - overhead

def check_oversized_segments(llm, n_ctx, segments, aligned_summaries):
    oversized = []
    segment_index = 0
    for i, segment in enumerate(segments):
        if segment is None:
            continue
        segment_index += 1
        prev_summary, next_summary = neighbor_summaries(aligned_summaries, i)
        budget = compute_budget(llm, n_ctx, prev_summary, next_summary)
        tokens = segment_token_count(llm, segment)
        if tokens > budget:
            preview = " ".join(" ".join(segment).split()[:10])
            oversized.append((segment_index, tokens, budget, preview))
    return oversized

def process_segments(llm, n_ctx, segments, aligned_summaries, outfile, allow_split):
    for i, segment in enumerate(segments):
        if segment is None:
            outfile.write("\n")
            outfile.flush()
            continue
        prev_summary, next_summary = neighbor_summaries(aligned_summaries, i)
        budget = compute_budget(llm, n_ctx, prev_summary, next_summary)
        tokens = segment_token_count(llm, segment)
        if tokens > budget and allow_split:
            for chunk in split_lines_by_tokens(llm, segment, budget):
                write_output(outfile, process_line(llm, "\n".join(chunk), prev_summary, next_summary))
        else:
            write_output(outfile, process_line(llm, "\n".join(segment), prev_summary, next_summary))

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

def main():
    model = pick_model()
    pick_request()
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(summaries_file, "r", encoding="utf-8") as sumfile:
        segments = read_segments(infile)
        summaries = read_summaries(sumfile)
    aligned_summaries = align_summaries_to_segments(segments, summaries)
    required_ctx = measure_required_ctx(model, segments, aligned_summaries)
    print(f"Using context window of {required_ctx} tokens.")
    llm = load_model(model, c_ntx=required_ctx)
    with open(output_file, "w", encoding="utf-8") as outfile:
        oversized = check_oversized_segments(llm, required_ctx, segments, aligned_summaries)
        allow_split = True
        if oversized:
            print(f"\n{len(oversized)} segment(s) exceed their token budget:")
            for index, tokens, budget, preview in oversized:
                print(f"{tokens} > {budget}: \"{preview}...\"")
            choice = input("\nProceed and split oversized segments? [y/N]: ").strip().lower()
            if choice not in ("y", "yes"):
                print("Aborted")
                return
        process_segments(llm, required_ctx, segments, aligned_summaries, outfile, allow_split)

if __name__ == "__main__":
    main()
