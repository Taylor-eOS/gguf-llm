from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from settings import MODELS, N_CTX, N_THREADS

def pick_model():
    print("Available models:")
    for i, m in enumerate(MODELS):
        print(f"  {i + 1}. {m['repo_id']}")
    while True:
        try:
            choice = input("Select model (number): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            raise SystemExit
        if choice.isdigit() and 1 <= int(choice) <= len(MODELS):
            return MODELS[int(choice) - 1]
        print(f"Enter a number between 1 and {len(MODELS)}.")

def load_model(model):
    path = hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])
    return Llama(model_path=path, n_ctx=N_CTX, n_threads=N_THREADS, verbose=False)

def stream_response(llm, prompt):
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
        stream_response(llm, prompt)

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
