from utils import is_cached, load_model, pick_model, strip_think
import settings

summaries = []

def build_summary_prompt(question, answer):
    return (settings.SUMMARY_INSTRUCTION + f"Q: {question}\nA: {answer}" + "\n\nCompressed facts:")

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
    context_prefix = ""
    if summaries:
        context_prefix = "Summary of earlier queries in this conversation:\n" + "\n".join(summaries) + "\n\nCurrent query:\n"
    return context_prefix + prompt + settings.SYSTEM_INSTRUCTION

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
        summary = summarize(llm, prompt, answer)
        summaries.append(summary)
        if settings.DEBUG_SUMMARY:
            print(f"\n[Summary]: {summary}\n")

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
