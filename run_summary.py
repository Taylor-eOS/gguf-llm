from utils import is_cached, load_model, pick_model, strip_think
import settings

DEBUG_SUMMARY = True

def build_summary_prompt(pairs):
    lines = []
    for i, (q, a) in enumerate(pairs, 1):
        lines.append(f"Q{i}: {q}")
        lines.append(f"A{i}: {a}")
    body = "\n".join(lines)
    return (settings.SUMMARY_INSTRUCTION + body
        + "\n\nCompressed facts:"
    )

def summarize(llm, pairs):
    prompt = build_summary_prompt(pairs)
    response = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        stream=False,
    )
    return response["choices"][0]["message"]["content"].strip()

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
            context_prefix = f"This is a summary of the earlier queries in this conversation:\n{summary}\n\nCurrent query:\n"
        full_prompt = context_prefix + prompt + settings.SYSTEM_INSTRUCTION
        answer = stream_response(llm, full_prompt)
        pairs.append((prompt, strip_think(answer)))
        summary = strip_think(summarize(llm, list(pairs)))
        if DEBUG_SUMMARY:
            print(f"\n[Summary]: {summary}\n")

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)

