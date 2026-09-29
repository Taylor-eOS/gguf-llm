import readline
from utils import is_cached, load_model, pick_model
import settings

REPORT_RECEIVED = False

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
            prompt = input("> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
        if not prompt:
            continue
        if REPORT_RECEIVED:
            tokens = len(llm.tokenize(prompt.encode("utf-8"), add_bos=False))
            print(f"Received {len(prompt)} characters, {tokens} tokens, ending with: \"{prompt[-40:]}\"")
        stream_response(llm, settings.SYSTEM_INSTRUCTION + prompt)

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
