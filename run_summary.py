from utils import is_cached, load_model, pick_model, strip_think
import settings

summaries = []
recent = []

def build_summary_prompt(question, answer):
    return (settings.SUMMARY_INSTRUCTION + "\n\n" + f"Q: {question}\nA: {answer}" + "\n\nCompressed exchange:")

def summarize(llm, question, answer):
    prompt = build_summary_prompt(question, answer)
    response = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], stream=False,)
    return strip_think(response["choices"][0]["message"]["content"]).strip()

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

def build_full_prompt(prompt):
    parts = []
    if summaries:
        parts.append("Summary of earlier queries in this conversation:\n" + "\n".join(summaries))
    if recent:
        parts.append("Most recent exchanges:\n" + "\n\n".join(f"Q: {q}\nA: {a}" for q, a in recent))
    context_prefix = ""
    if parts:
        context_prefix = "\n\n".join(parts) + "\n\nCurrent query:\n"
    return context_prefix + prompt + settings.SYSTEM_INSTRUCTION

def summarize_overflow(llm):
    while len(recent) > settings.SUMMARY_RECENT_PAIRS:
        question, answer = recent.pop(0)
        summary = summarize(llm, question, answer)
        summaries.append(summary)
        if settings.DEBUG_SUMMARY:
            print(f"\n[Summary]: {summary}\n")

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
        answer = strip_think(stream_response(llm, build_full_prompt(prompt)))
        recent.append((prompt, answer))
        summarize_overflow(llm)

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
