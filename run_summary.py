import readline
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
    brevity = "This is a fast back and forth chat. Respond with only a few sentences, as appropriate for this response, in continuous format. Write continuously without any formatting or line shifts at all!"
    system = compact(settings.SYSTEM_INSTRUCTION)
    user = prompt + "\n" + brevity
    messages = build_messages(system, user, system + "\n" + user)
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
    lines = ["<history>"]
    lines.extend(f"<summary>{s}</summary>" for s in summaries)
    for q, a in recent:
        lines.append(f"<user>{q}</user>")
        lines.append(f"<assistant>{a}</assistant>")
    lines.append("</history>")
    lines.append(f"<current_query>{prompt}</current_query>")
    return "\n".join(lines)

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
