from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from pathlib import Path
import settings

def is_cached(model):
    repo_slug = "models--" + model["repo_id"].replace("/", "--")
    return (Path.home() / ".cache" / "huggingface" / "hub" / repo_slug).is_dir()

def load_model(model):
    path = hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])
    return Llama(model_path=path, n_ctx=settings.N_CTX, n_threads=settings.N_THREADS, verbose=False)

def pick_model():
    print("Available models ([x] = cached, [T] = thinking):")
    for i, m in enumerate(settings.MODELS):
        tag = "[x]" if is_cached(m) else "[ ]"
        think_val = m.get("thinking")
        think_tag = "[T]" if think_val is True else ("[ ]" if think_val is None else "[N]")
        print(f" {i + 1:2d} {tag}{think_tag} {m['repo_id']}")
    while True:
        try:
            choice = input("Select model number: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            raise SystemExit
        if choice.isdigit() and 1 <= int(choice) <= len(settings.MODELS):
            return settings.MODELS[int(choice) - 1]
        print(f"Enter a number between 1 and {len(settings.MODELS)}.")

def stream_response(llm, prompt):
    print()
    stream = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], stream=True)
    for chunk in stream:
        delta = chunk["choices"][0]["delta"]
        token = delta.get("content", "")
        if token:
            print(token, end="", flush=True)
    print()

def run_chat_loop(llm):
    print("Prompt:\n")
    while True:
        try:
            prompt = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
        if not prompt:
            continue
        stream_response(llm, prompt + settings.STYLE_INSTRUCTION)

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)

