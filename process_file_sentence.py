import pysbd
from utils import load_model, pick_model, strip_think
import settings

input_file = "input.txt"
output_file = "output.txt"
_segmenter = pysbd.Segmenter(language="en", clean=False)
starting_output = input("Starting output: ") or ""

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

def split_segment_sentences(segment_lines):
    text = "\n".join(segment_lines)
    return [s.strip() for s in _segmenter.segment(text) if s.strip()]

def build_prompt(context, last_output, sentence):
    parts = [
        f"Context: \"{context}\"",
        f"Last output: \"{last_output}\"" if last_output else "Last output: {starting_output}",
        f"Sentence to describe: \"{sentence}\"",
        settings.BASE,
        f"Task: {settings.REQUEST}\nProcessed:",
    ]
    return "\n".join(parts)

def prompt_token_count(llm, context, last_output, sentence):
    prompt = build_prompt(context, last_output, sentence)
    return len(llm.tokenize(prompt.encode("utf-8"), add_bos=False))

def compute_budget():
    return settings.N_CTX - settings.MAX_TOKENS

def process_sentence(llm, context, last_output, sentence):
    prompt = build_prompt(context, last_output, sentence)
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

def check_oversized_sentences(llm, segments, budget):
    oversized = []
    segment_index = 0
    for segment in segments:
        if segment is None:
            continue
        segment_index += 1
        context = "\n".join(segment)
        sentences = split_segment_sentences(segment)
        for sentence_index, sentence in enumerate(sentences, 1):
            tokens = prompt_token_count(llm, context, "placeholder last output text", sentence)
            if tokens > budget:
                preview = " ".join(sentence.split()[:10])
                oversized.append((segment_index, sentence_index, tokens, preview))
    return oversized

def process_segments(llm, segments, outfile, budget):
    last_output = ""
    for segment in segments:
        if segment is None:
            outfile.write("\n")
            outfile.flush()
            continue
        context = "\n".join(segment)
        sentences = split_segment_sentences(segment)
        for sentence in sentences:
            tokens = prompt_token_count(llm, context, last_output, sentence)
            if tokens > budget:
                print(f"Skipping oversized sentence ({tokens} tokens): \"{' '.join(sentence.split()[:10])}...\"")
                continue
            output = process_sentence(llm, context, last_output, sentence)
            write_output(outfile, output)
            last_output = output

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
    pick_request()
    llm = load_model(model)
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        segments = read_segments(infile)
        budget = compute_budget()
        oversized = check_oversized_sentences(llm, segments, budget)
        if oversized:
            print(f"\n{len(oversized)} sentence(s) exceed the token budget of {budget}:")
            for segment_index, sentence_index, tokens, preview in oversized:
                print(f"segment {segment_index} sentence {sentence_index}, {tokens} tokens: \"{preview}...\"")
            choice = input("\nProceed and skip oversized sentences? [y/N]: ").strip().lower()
            if choice not in ("y", "yes"):
                print("Aborted")
                return
        process_segments(llm, segments, outfile, budget)

if __name__ == "__main__":
    main()
