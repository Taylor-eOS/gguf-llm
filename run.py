from utils import is_cached, load_model, pick_model
from settings import SYSTEM_INSTRUCTION

def stream_response(llm, prompt, has_system, is_reasoning):
    print()
    messages = []
    if has_system:
        messages.append({"role": "system", "content": SYSTEM_INSTRUCTION})
        messages.append({"role": "user", "content": prompt})
    else:
        messages.append({"role": "user", "content": prompt + SYSTEM_INSTRUCTION})
    kwargs = {"messages": messages, "stream": True}
    if is_reasoning:
        kwargs["extra_body"] = {"extra_generation_params": {"disable_thinking": True}}
    try:
        stream = llm.create_chat_completion(**kwargs)
    except Exception:
        kwargs.pop("extra_body", None)
        stream = llm.create_chat_completion(**kwargs)
    for chunk in stream:
        delta = chunk["choices"][0]["delta"]
        token = delta.get("content", "")
        if token:
            print(token, end="", flush=True)
    print()

def run_chat_loop(llm):
    has_system = False
    if SYSTEM_INSTRUCTION and hasattr(llm, "metadata") and "tokenizer.chat_template" in llm.metadata:
        has_system = True
    print(f"System prompt supported: {has_system}")
    is_reasoning = "reasoning" in getattr(llm, "model_path", "").lower()
    print(f"Disable thinking supported: {is_reasoning}")
    print("\nPrompt:\n")
    while True:
        try:
            prompt = input(">>> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break
        if not prompt:
            continue
        stream_response(llm, prompt, has_system, is_reasoning)

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
