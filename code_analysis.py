from utils import load_model, pick_model
import settings
import os

input_dir = "input"
output_file = "output.txt"

STATE = {
    "llm": None,
    "outfile": None,
}

def build_prompt(filename, content):
    parts = [
        f"Filename: \"{filename}\"",
        settings.BASE,
        "File content:\n" + content,
        settings.CODE_TASK + "\nProcessed:",
    ]
    return "\n".join(parts)

def summarize_file(filepath):
    filename = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    prompt = build_prompt(filename, content)
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    result = STATE["llm"].create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=settings.MAX_TOKENS,
        temperature=0.7,
        top_p=0.9,
    )
    return result["choices"][0]["message"]["content"].strip()

def write_summary(filename, summary):
    STATE["outfile"].write(f"=== {filename} ===\n")
    STATE["outfile"].write(summary + "\n\n")
    STATE["outfile"].flush()
    print(f"=== {filename} ===")
    print(summary)
    print()

def gather_input_files():
    entries = []
    for name in sorted(os.listdir(input_dir)):
        path = os.path.join(input_dir, name)
        if os.path.isfile(path):
            entries.append(path)
    return entries

def main():
    model = pick_model()
    STATE["llm"] = load_model(model)
    files = gather_input_files()
    if not files:
        print(f"No files found in {input_dir}/")
        return
    with open(output_file, "w", encoding="utf-8") as outfile:
        STATE["outfile"] = outfile
        for filepath in files:
            summary = summarize_file(filepath)
            write_summary(os.path.basename(filepath), summary)

if __name__ == "__main__":
    main()

