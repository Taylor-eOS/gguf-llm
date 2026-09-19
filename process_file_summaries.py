from utils import load_model, log_instruction_use, pick_model, split_lines_by_tokens, strip_think
from process_file import read_segments, segment_token_count, write_output
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

def compute_budget(llm, prev_summary, next_summary):
    parts = []
    if prev_summary is not None:
        parts.append(f"Summary of previous segment: \"{prev_summary}\"")
    if next_summary is not None:
        parts.append(f"Summary of following segment: \"{next_summary}\"")
    parts.append(f"Input content: \"\"")
    parts.append(settings.BASE)
    parts.append(f"Task: {settings.REQUEST}\nProcessed:")
    overhead = len(llm.tokenize("\n".join(parts).encode("utf-8"), add_bos=False))
    return settings.N_CTX - settings.MAX_TOKENS - overhead

def check_oversized_segments(llm, segments, aligned_summaries):
    oversized = []
    segment_index = 0
    for i, segment in enumerate(segments):
        if segment is None:
            continue
        segment_index += 1
        prev_summary, next_summary = neighbor_summaries(aligned_summaries, i)
        budget = compute_budget(llm, prev_summary, next_summary)
        tokens = segment_token_count(llm, segment)
        if tokens > budget:
            preview = " ".join(" ".join(segment).split()[:10])
            oversized.append((segment_index, tokens, budget, preview))
    return oversized

def process_segments(llm, segments, aligned_summaries, outfile, allow_split):
    for i, segment in enumerate(segments):
        if segment is None:
            outfile.write("\n")
            outfile.flush()
            continue
        prev_summary, next_summary = neighbor_summaries(aligned_summaries, i)
        budget = compute_budget(llm, prev_summary, next_summary)
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
    llm = load_model(model)
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(summaries_file, "r", encoding="utf-8") as sumfile, \
         open(output_file, "w", encoding="utf-8") as outfile:
        segments = read_segments(infile)
        summaries = read_summaries(sumfile)
        aligned_summaries = align_summaries_to_segments(segments, summaries)
        oversized = check_oversized_segments(llm, segments, aligned_summaries)
        allow_split = True
        if oversized:
            print(f"\n{len(oversized)} segment(s) exceed their token budget:")
            for index, tokens, budget, preview in oversized:
                print(f"{tokens} > {budget}: \"{preview}...\"")
            choice = input("\nProceed and split oversized segments? [y/N]: ").strip().lower()
            if choice not in ("y", "yes"):
                print("Aborted")
                return
        process_segments(llm, segments, aligned_summaries, outfile, allow_split)

if __name__ == "__main__":
    main()
