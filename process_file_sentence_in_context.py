from utils import load_model, load_tokenizer, pick_model, strip_think
from process_file import compute_required_ctx, read_segments, write_output
import settings

input_file = "input.txt"
output_file = "output.txt"
use_line_shifts = True
starting_output = input("Starting output: ") or ""

def split_segment_sentences(segment_lines):
    if use_line_shifts:
        return [line.strip() for line in segment_lines if line.strip() != ""]
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

def longest_context_and_sentence(llm, segments):
    longest_context_tokens = 0
    longest_sentence_tokens = 0
    for segment in segments:
        if segment is None:
            continue
        context = "\n".join(segment)
        context_tokens = len(llm.tokenize(context.encode("utf-8"), add_bos=False))
        if context_tokens > longest_context_tokens:
            longest_context_tokens = context_tokens
        for sentence in split_segment_sentences(segment):
            sentence_tokens = len(llm.tokenize(sentence.encode("utf-8"), add_bos=False))
            if sentence_tokens > longest_sentence_tokens:
                longest_sentence_tokens = sentence_tokens
    return longest_context_tokens, longest_sentence_tokens

def measure_required_ctx(model, segments):
    tokenizer_llm = load_tokenizer(model)
    longest_context_tokens, longest_sentence_tokens = longest_context_and_sentence(tokenizer_llm, segments)
    longest_input_tokens = longest_context_tokens + longest_sentence_tokens
    required_ctx = compute_required_ctx(tokenizer_llm, longest_input_tokens)
    del tokenizer_llm
    return required_ctx

def compute_budget(n_ctx):
    return n_ctx - settings.MAX_TOKENS

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
    with open(input_file, "r", encoding="utf-8") as infile:
        segments = read_segments(infile)
    required_ctx = measure_required_ctx(model, segments)
    print(f"Using context window of {required_ctx} tokens.")
    llm = load_model(model, c_ntx=required_ctx)
    with open(output_file, "w", encoding="utf-8") as outfile:
        budget = compute_budget(required_ctx)
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
