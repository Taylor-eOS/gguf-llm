from huggingface_hub import hf_hub_download
from llama_cpp import Llama

REPO_ID = "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF"
FILENAME = "gemma4-coding-Q4_K_M.gguf"
N_CTX = 4096
N_THREADS = 12

def load_model():
    path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    return Llama(model_path=path, n_ctx=N_CTX, n_threads=N_THREADS, verbose=False,)

def stream_response(llm, prompt):
    stream = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], stream=True,)
    for chunk in stream:
        delta = chunk["choices"][0]["delta"]
        token = delta.get("content", "")
        if token:
            print(token, end="", flush=True)
    print()

def run_chat_loop(llm):
    print("Type your prompt and press Enter. Use Ctrl+C to exit.\n")
    while True:
        try:
            prompt = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
        if not prompt:
            continue
        stream_response(llm, prompt)

def main():
    llm = load_model()
    run_chat_loop(llm)

if __name__ == "__main__":
    main()
