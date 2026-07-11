from utils import load_model, pick_model
import settings

input_file = "input_code.txt"
output_file = "output_code.txt"
CODE_MAX_TOKENS = 8 * 1024
CODE_N_CTX = 12 * 1024
CODE_CHARS_PER_TOKEN = 4
STATE = {"llm": None, "outfile": None,}
TRUNCATE_INPUT = True
DELIMITER = "---"

def build_prompt(identifier, body):
    parts = [
        f"Block: \"{identifier}\"",
        settings.BASE,
        "File content:\n" + body,
        settings.CODE_TASK + "\nProcessed:",
    ]
    return "\n".join(parts)

def split_blocks(text):
    blocks = []
    raw_chunks = text.split(DELIMITER)
    for raw in raw_chunks:
        chunk = raw.strip("\n")
        if not chunk.strip():
            continue
        lines = chunk.split("\n", 1)
        identifier = lines[0].strip()
        body = lines[1].strip("\n") if len(lines) > 1 else ""
        if identifier:
            blocks.append((identifier, body))
    return blocks

EMPTY_PROMPT_LEN = len(build_prompt("identifier", ""))

def truncate_body(body):
    budget_tokens = CODE_N_CTX - CODE_MAX_TOKENS
    limit = budget_tokens * CODE_CHARS_PER_TOKEN - EMPTY_PROMPT_LEN
    if limit < 0:
        limit = 0
    if TRUNCATE_INPUT and len(body) > limit:
        return body[:limit]
    return body

def summarize_block(identifier, body):
    prompt = build_prompt(identifier, body)
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    try:
        result = STATE["llm"].create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=CODE_MAX_TOKENS,
            temperature=0.7,
            top_p=0.9,
        )
        summary = result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"{identifier}\tERROR: {e}")
        return None
    return summary.replace("\t", " ").replace("\n", " ")

def write_summary(identifier, summary):
    STATE["outfile"].write(f"{identifier}\t{summary}\n")
    STATE["outfile"].flush()
    print(f"{identifier}\t{summary}")

def load_blocks():
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    return split_blocks(text)

def main():
    model = pick_model()
    STATE["llm"] = load_model(model, CODE_N_CTX)
    blocks = load_blocks()
    if not blocks:
        print(f"No blocks found in {input_file}")
        return
    with open(output_file, "w", encoding="utf-8") as outfile:
        STATE["outfile"] = outfile
        for identifier, body in blocks:
            body = truncate_body(body)
            summary = summarize_block(identifier, body)
            if summary is None:
                continue
            write_summary(identifier, summary)

if __name__ == "__main__":
    main()
