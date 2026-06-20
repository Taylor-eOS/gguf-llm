from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from pathlib import Path
import settings

DEBUG_SUMMARY = True

def is_cached(model):
    repo_slug = "models--" + model["repo_id"].replace("/", "--")
    return (Path.home() / ".cache" / "huggingface" / "hub" / repo_slug).is_dir()

def load_model(model):
    path = hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])
    return Llama(model_path=path, n_ctx=settings.N_CTX, n_threads=settings.N_THREADS, verbose=False)

def pick_model():
    print("Available models ([x] = cached):")
    for i, m in enumerate(settings.MODELS):
        tag = "[x]" if is_cached(m) else "[ ]"
        print(f" {i + 1:2d} {tag} {m['repo_id']}")
    while True:
        try:
            choice = input("Select model number: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            raise SystemExit
        if choice.isdigit() and 1 <= int(choice) <= len(settings.MODELS):
            return settings.MODELS[int(choice) - 1]
        print(f"Enter a number between 1 and {len(settings.MODELS)}.")

def build_summary_prompt(pairs):
    lines = []
    for i, (q, a) in enumerate(pairs, 1):
        lines.append(f"Q{i}: {q}")
        lines.append(f"A{i}: {a}")
    body = "\n".join(lines)
    return (
        "Extract key facts from the exchanges below as compressed notes. "
        "Use semicolons to separate facts. No bullet points, no line breaks, no headers, no good grammar needed. "
        "Write this as one continuous block of text, not repeating the Q&A format. "
        "Never repeat a question. Never analyze or comment. Fewer words is strictly better. "
        "Use the same language as the exchanges.\n\n"
        + body
        + "\n\nCompressed facts:"
    )

def summarize(llm, pairs):
    prompt = build_summary_prompt(pairs)
    response = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        stream=False,
    )
    return response["choices"][0]["message"]["content"].strip()

def strip_think(text):
    marker = "</think>"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[idx + len(marker):].strip()

def stream_response(llm, prompt):
    print()
    stream = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], stream=True)
    tokens = []
    for chunk in stream:
        delta = chunk["choices"][0]["delta"]
        token = delta.get("content", "")
        if token:
            print(token, end="", flush=True)
            tokens.append(token)
    print()
    return "".join(tokens)

def run_chat_loop(llm):
    print("Prompt:\n")
    pairs = []
    summary = ""
    while True:
        try:
            prompt = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
        if not prompt:
            continue
        context_prefix = ""
        if summary:
            context_prefix = f"Context from earlier in this conversation:\n{summary}\n\nCurrent query:\n"
        full_prompt = context_prefix + prompt + settings.STYLE_INSTRUCTION
        answer = stream_response(llm, full_prompt)
        pairs.append((prompt, strip_think(answer)))
        summary = strip_think(summarize(llm, list(pairs)))
        if DEBUG_SUMMARY:
            print(f"\n[Summary]: {summary}\n")

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
