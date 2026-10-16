from utils import build_messages, is_cached, load_model, pick_model, strip_think
import settings

summaries = []
recent = []

def compact(text):
    return "\n".join(line for line in text.splitlines() if line.strip())

def separate_answer(text):
    question, marker, answer = text.partition("A:")
    if not marker:
        return text
    return question.rstrip() + " " + marker + answer.lstrip()

def build_summary_prompt(question, answer):
    return compact(settings.SUMMARY_INSTRUCTION) + "\n" + f"Q: {question}\nA: {answer}" + "\nCompressed exchange:"

def summarize(llm, question, answer):
    prompt = build_summary_prompt(question, answer)
    response = llm.create_chat_completion(messages=[{"role": "user", "content": prompt}], stream=False)
    return separate_answer(compact(strip_think(response["choices"][0]["message"]["content"])))

def stream_response(llm, prompt):
    print()
    system = compact(settings.SYSTEM_INSTRUCTION)
    messages = build_messages(system, prompt, system + "\n" + prompt + "\nRespond with 2-3 sentences at most.")
    stream = llm.create_chat_completion(messages=messages, stream=True)
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
        parts.append("Conversation summary:\n" + "\n".join(summaries))
    if recent:
        parts.append("Recent exchanges:\n" + "\n".join(f"Q: {q}\nA: {a}" for q, a in recent))
    if not parts:
        return prompt
    parts.append("Current query: " + prompt)
    return "\n".join(parts)

def summarize_overflow(llm):
    while len(recent) > settings.SUMMARY_RECENT_PAIRS:
        question, answer = recent.pop(0)
        summaries.append(summarize(llm, question, answer))

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
        full_prompt = build_full_prompt(prompt)
        if settings.DEBUG_SUMMARY:
            print()
            print(full_prompt)
        answer = compact(strip_think(stream_response(llm, full_prompt)))
        recent.append((prompt, answer))
        summarize_overflow(llm)

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
