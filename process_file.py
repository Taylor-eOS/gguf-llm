from utils import is_cached, load_model, pick_model, split_lines_by_tokens, strip_think
import settings

input_file = "input.txt"
output_file = "output.txt"
truncate_safety_margin = 16

def process_line(llm, line):
    parts = [
        f"Input content: \"{line}\"",
        settings.BASE,
        f"Task: {settings.REQUEST}\nProcessed:",
    ]
    prompt = "\n".join(parts)
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    result = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=settings.MAX_TOKENS,
        temperature=0.7,
        top_p=0.9,
    )
    return strip_think(result["choices"][0]["message"]["content"].strip())

def write_output(outfile, output):
    output = "\n".join(line for line in output.split("\n") if line.strip() != "")
    print(output)
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

def segment_token_count(llm, paragraph_lines):
    return len(llm.tokenize("\n".join(paragraph_lines).encode("utf-8"), add_bos=False))

def compute_budget(llm):
    overhead = len(llm.tokenize(
        (f"Input content: \"\"\n{settings.BASE}\nTask: {settings.REQUEST}\nProcessed:").encode("utf-8"),
        add_bos=False
    ))
    return settings.N_CTX - settings.MAX_TOKENS - overhead

def check_oversized_segments(llm, segments, budget):
    oversized = []
    segment_index = 0
    for segment in segments:
        if segment is None:
            continue
        segment_index += 1
        tokens = segment_token_count(llm, segment)
        if tokens > budget:
            preview = " ".join(" ".join(segment).split()[:10])
            oversized.append((segment_index, tokens, preview))
    return oversized

def truncate_segment(llm, segment, budget):
    text = "\n".join(segment)
    tokens = llm.tokenize(text.encode("utf-8"), add_bos=False)
    limit = max(budget - truncate_safety_margin, 0)
    truncated_tokens = tokens[:limit]
    truncated_text = llm.detokenize(truncated_tokens).decode("utf-8", errors="ignore")
    return truncated_text

def process_segments(llm, segments, outfile, budget, allow_split):
    for segment in segments:
        if segment is None:
            outfile.write("\n")
            outfile.flush()
            continue
        tokens = segment_token_count(llm, segment)
        if tokens > budget and allow_split:
            for chunk in split_lines_by_tokens(llm, segment, budget):
                write_output(outfile, process_line(llm, "\n".join(chunk)))
        elif tokens > budget:
            write_output(outfile, process_line(llm, truncate_segment(llm, segment, budget)))
        else:
            write_output(outfile, process_line(llm, "\n".join(segment)))

def process_lines(llm, infile, outfile):
    for raw_line in infile:
        line = raw_line.rstrip("\n")
        if line.strip() == "":
            outfile.write("\n")
            outfile.flush()
        else:
            write_output(outfile, process_line(llm, line))

def pick_request():
    for i, request in enumerate(settings.REQUESTS, 1):
        sample = " ".join(request.split()[:10])
        print(f"{i}: {sample}...")
    choice = input(f"Pick a task [1-{len(settings.REQUESTS)}]: ").strip()
    try:
        index = int(choice) - 1
        if index < 0 or index >= len(settings.REQUESTS):
            raise ValueError
    except ValueError:
        index = 0
    settings.REQUEST = settings.REQUESTS[index]

def main():
    model = pick_model()
    _segment_mode = input("Use segment mode? [Y/n]: ").strip().lower()
    _segment_mode = _segment_mode if _segment_mode in ("y", "yes", "") else "n"
    _segment_mode = _segment_mode in ("y", "yes", "")
    pick_request()
    llm = load_model(model)
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        if _segment_mode:
            segments = read_segments(infile)
            budget = compute_budget(llm)
            oversized = check_oversized_segments(llm, segments, budget)
            allow_split = True
            if oversized:
                print(f"\n{len(oversized)} segment(s) exceed the token budget of {budget}:")
                for index, tokens, preview in oversized:
                    print(f"{tokens}: \"{preview}...\"")
                choice = input("\nSplit oversized segments? [Y/n] (no truncates instead): ").strip().lower()
                allow_split = choice in ("y", "yes", "")
            process_segments(llm, segments, outfile, budget, allow_split)
        else:
            process_lines(llm, infile, outfile)

if __name__ == "__main__":
    main()
