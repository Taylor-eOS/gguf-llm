from utils import is_cached, load_model, pick_model
from settings import SYSTEM_INSTRUCTION, STYLE_INSTRUCTION

def stream_response(llm, prompt):
    print()
    messages = []
    system_instruction = SYSTEM_INSTRUCTION
    if system_instruction and hasattr(llm, "metadata") and "tokenizer.chat_template" in llm.metadata:
        messages.append({"role": "system", "content": system_instruction})
    style_instruction = STYLE_INSTRUCTION
    messages.append({"role": "user", "content": prompt + style_instruction})
    kwargs = {"messages": messages, "stream": True}
    if "reasoning" in getattr(llm, "model_path", "").lower():
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
