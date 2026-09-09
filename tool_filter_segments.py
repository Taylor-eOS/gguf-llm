input_file = "input.txt"
answers_file = "output.txt"
output_file = "output_filtered.txt"

def read_segments(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    raw_segments = content.split("\n\n")
    segments = [s.strip() for s in raw_segments if s.strip() != ""]
    return segments

def is_affirmative(answer):
    normalized = answer.strip().lower()
    normalized = normalized.strip(".!? ")
    affirmative_values = {"yes", "y", "true", "affirmative", "1"}
    return normalized in affirmative_values

def filter_segments(segments, answers):
    if len(segments) != len(answers):
        print(f"Warning: segment count ({len(segments)}) does not match answer count ({len(answers)}).")
    kept = []
    count = min(len(segments), len(answers))
    for i in range(count):
        if is_affirmative(answers[i]):
            kept.append(segments[i])
    return kept

def write_segments(path, segments):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(segments))

def main():
    segments = read_segments(input_file)
    answers = read_segments(answers_file)
    kept = filter_segments(segments, answers)
    write_segments(output_file, kept)
    print(f"Kept {len(kept)} of {len(segments)} segments. Written to {output_file}.")

if __name__ == "__main__":
    main()

