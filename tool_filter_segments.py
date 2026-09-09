import re

input_file = "input.txt"
answers_file = "output.txt"
output_file = "output_filtered.txt"
uncertain_file = "output_uncertain.txt"

AFFIRMATIVE_WORDS = {"yes", "y", "true", "correct", "affirmative", "agree", "accurate", "confirmed"}
NEGATIVE_WORDS = {"no", "n", "false", "negative", "incorrect", "disagree", "disagreed"}

def read_segments(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    raw_segments = content.split("\n\n")
    segments = [s.strip() for s in raw_segments if s.strip() != ""]
    return segments

def tokenize(text):
    normalized = text.strip().lower()
    tokens = re.findall(r"[a-z']+", normalized)
    return tokens

def classify_answer(answer):
    tokens = tokenize(answer)
    token_set = set(tokens)
    has_affirmative = not token_set.isdisjoint(AFFIRMATIVE_WORDS)
    has_negative = not token_set.isdisjoint(NEGATIVE_WORDS)
    if has_affirmative and not has_negative:
        return "YES"
    if has_negative and not has_affirmative:
        return "NO"
    return "UNCERTAIN"

def check_segment_counts(segments, answers):
    if len(segments) != len(answers):
        print(f"Warning: input file has {len(segments)} segments but output file has {len(answers)} segments. Results will be truncated to the shorter list.")

def classify_segments(segments, answers):
    count = min(len(segments), len(answers))
    kept = []
    uncertain = []
    for i in range(count):
        verdict = classify_answer(answers[i])
        if verdict == "YES":
            kept.append(segments[i])
        elif verdict == "UNCERTAIN":
            uncertain.append(segments[i])
    return kept, uncertain

def write_segments(path, segments):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(segments))

def main():
    segments = read_segments(input_file)
    answers = read_segments(answers_file)
    check_segment_counts(segments, answers)
    kept, uncertain = classify_segments(segments, answers)
    write_segments(output_file, kept)
    write_segments(uncertain_file, uncertain)
    print(f"Kept {len(kept)} of {len(segments)} segments. Written to {output_file}.")
    print(f"{len(uncertain)} segments were UNCERTAIN. Written to {uncertain_file} for manual review.")

if __name__ == "__main__":
    main()
