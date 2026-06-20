from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from pathlib import Path
from run import is_cached, load_model, pick_model
import settings

DEBUG_SUMMARY = True

def build_summary_prompt(pairs):
    lines = []
    for i, (q, a) in enumerate(pairs, 1):
        lines.append(f"Q{i}: {q}")
        lines.append(f"A{i}: {a}")
    body = "\n".join(lines)
    return (
        "Extract key facts from the exchange between a user and LLM assistant as compressed notes. "
        "No bullet points, no line breaks, no headers, no good grammar needed. "
        "Write this as one continuous block of text, without bullet points, line breaks, or headers, and not repeating the Q&A format. "
        "Don't analyze or comment. The purpose is to provicde a compact truncation as context for the next response. "
        "Use the same language as the exchanges.\n\n"
        + body
        + "\n\nCompressed facts:"
    )

def summarize(llm, pairs):
    prompt = build_summary_prompt(pairs)
    response = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        stream=False,
    )
    return response["choices"][0]["message"]["content"].strip()

def strip_think(text):
    marker = "</think>"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[idx + len(marker):].strip()

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
        full_prompt = context_prefix + prompt + settings.STYLE_INSTRUCTION
        answer = stream_response(llm, full_prompt)
        pairs.append((prompt, strip_think(answer)))
        summary = strip_think(summarize(llm, list(pairs)))
        if DEBUG_SUMMARY:
            print(f"\n[Summary]: {summary}\n")

if __name__ == "__main__":
    model = pick_model()
    llm = load_model(model)
    run_chat_loop(llm)
