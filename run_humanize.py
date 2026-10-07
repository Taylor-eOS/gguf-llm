from pathlib import Path
from utils import load_model

INPUT_PATH = "input.txt"
OUTPUT_PATH = "output.txt"
CONTEXT = 8192
MAX_NEW_TOKENS = 2048
MODEL = {
    "repo_id": "jialinyyzz/humanizer",
    "filename": "humanizer-12b-Q4_K_M.gguf",
}
INSTRUCTION = (
    "Rewrite the text below so it reads like a person wrote it, not a language model.\n"
    "Reorganize it as you see fit. Vary sentence length on purpose. Cut hedging,\n"
    "throat-clearing, and any sentence that only announces what comes next.\n"
    "Prefer the concrete word over the abstract one. It is fine to sound uneven.\n"
    "Every fact, number, unit, date, name and quotation must survive unchanged."
)
SEPARATOR = "\n### Rewritten:\n"

def read_draft():
    path = Path(INPUT_PATH or input("Draft file: ").strip())
    if not path.is_file():
        print(f"{path} not found.")
        raise SystemExit
    draft = path.read_text(encoding="utf-8").strip()
    if not draft:
        print(f"{path} is empty.")
        raise SystemExit
    return draft

def build_prompt(draft):
    return INSTRUCTION + "\n\n" + draft + SEPARATOR

def check_fits(llm, prompt):
    tokens = len(llm.tokenize(prompt.encode("utf-8")))
    print(f"Prompt is {tokens} tokens, context is {llm.n_ctx()}.")
    if tokens + MAX_NEW_TOKENS > llm.n_ctx():
        print(f"Draft too long, raise CONTEXT or split the draft (prompt plus {MAX_NEW_TOKENS} new tokens must fit).")
        raise SystemExit

def generate(llm, prompt):
    parts = []
    finish_reason = None
    stream = llm.create_completion(
        prompt=prompt,
        max_tokens=MAX_NEW_TOKENS,
        temperature=1.0,
        top_p=0.95,
        top_k=0,
        min_p=0.0,
        repeat_penalty=1.0,
        stream=True,
    )
    print()
    for chunk in stream:
        choice = chunk["choices"][0]
        token = choice.get("text", "")
        if token:
            parts.append(token)
            print(token, end="", flush=True)
        if choice.get("finish_reason"):
            finish_reason = choice["finish_reason"]
    print()
    if finish_reason == "length":
        print("Warning: output hit the token limit and may be cut off.")
    return "".join(parts).strip()

def save_result(text):
    Path(OUTPUT_PATH).write_text(text + "\n", encoding="utf-8")
    print(f"Saved to {OUTPUT_PATH}.")

def main():
    draft = read_draft()
    llm = load_model(MODEL, c_ntx=CONTEXT)
    prompt = build_prompt(draft)
    check_fits(llm, prompt)
    result = generate(llm, prompt)
    if not result:
        print("Model returned nothing.")
        raise SystemExit
    save_result(result)

if __name__ == "__main__":
    main()
