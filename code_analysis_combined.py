import os
from utils import load_model, pick_model
import settings

"""
Goes through a continuous code file and processes chunks in token limit size.
"""

input_file = "input_code.txt"
output_file = "output_code.txt"
CODE_MAX_TOKENS = 8 * 1024
CODE_N_CTX = 12 * 1024
CODE_CHARS_PER_TOKEN = 4
STATE = {"llm": None, "outfile": None,}
TRUNCATE_INPUT = True
DELIMITER = "```\n\n```"

def build_prompt(label, content):
    parts = [
        f"Chunk: \"{label}\"",
        settings.BASE,
        "File content:\n" + content,
        settings.CODE_TASK + "\nProcessed:",
    ]
    return "\n".join(parts)

def split_functions(text):
    raw_chunks = text.split(DELIMITER)
    functions = []
    for raw in raw_chunks:
        piece = raw.strip()
        if piece.startswith("```"):
            piece = piece[3:]
        if piece.endswith("```"):
            piece = piece[:-3]
        piece = piece.strip("\n")
        if piece:
            functions.append(piece)
    return functions

def budget_chars():
    budget_tokens = CODE_N_CTX - CODE_MAX_TOKENS
    budget_chars = budget_tokens * CODE_CHARS_PER_TOKEN
    overhead = len(build_prompt("batch", ""))
    limit = budget_chars - overhead
    if limit < 0:
        limit = 0
    return limit

def pack_batches(functions):
    limit = budget_chars()
    batches = []
    current = []
    current_len = 0
    for func in functions:
        func_len = len(func) + 2
        if TRUNCATE_INPUT and func_len > limit:
            func = func[:max(limit - 2, 0)]
            func_len = len(func) + 2
        if current and current_len + func_len > limit:
            batches.append(current)
            current = []
            current_len = 0
        current.append(func)
        current_len += func_len
    if current:
        batches.append(current)
    return batches

def summarize_batch(label, functions):
    content = "\n\n".join(functions)
    prompt = build_prompt(label, content)
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    result = STATE["llm"].create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=CODE_MAX_TOKENS,
        temperature=0.7,
        top_p=0.9,
    )
    return result["choices"][0]["message"]["content"].strip()

def write_summary(label, function_count, summary):
    STATE["outfile"].write(f"=== {label} ({function_count} functions) ===\n")
    STATE["outfile"].write(summary + "\n\n")
    STATE["outfile"].flush()
    print(f"=== {label} ({function_count} functions) ===")
    print(summary)
    print()

def load_functions():
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    return split_functions(text)

def main():
    model = pick_model()
    STATE["llm"] = load_model(model, CODE_N_CTX)
    functions = load_functions()
    if not functions:
        print(f"No functions found in {input_file}")
        return
    batches = pack_batches(functions)
    with open(output_file, "w", encoding="utf-8") as outfile:
        STATE["outfile"] = outfile
        for index, batch in enumerate(batches, start=1):
            label = f"batch_{index}_of_{len(batches)}"
            summary = summarize_batch(label, batch)
            write_summary(label, len(batch), summary)

if __name__ == "__main__":
    main()
