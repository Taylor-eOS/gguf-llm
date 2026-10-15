import time
from jinja2.sandbox import ImmutableSandboxedEnvironment
import process_file
import settings

DISABLE_THINKING = True

def special_token_text(llm, key):
    token_id = llm.metadata.get(key)
    if token_id is None:
        return ""
    return llm.detokenize([int(token_id)], special=True).decode("utf-8", errors="ignore")

def raise_template_exception(message):
    raise ValueError(message)

def render_prompt(llm, messages):
    template_source = llm.metadata.get("tokenizer.chat_template")
    if not template_source:
        return None
    environment = ImmutableSandboxedEnvironment(trim_blocks=True, lstrip_blocks=True)
    template = environment.from_string(template_source)
    return template.render(messages=messages, add_generation_prompt=True, enable_thinking=False, bos_token=special_token_text(llm, "tokenizer.ggml.bos_token_id"), eos_token=special_token_text(llm, "tokenizer.ggml.eos_token_id"), raise_exception=raise_template_exception)

def generate(llm, messages):
    prompt = render_prompt(llm, messages) if DISABLE_THINKING else None
    if prompt is None:
        return llm.create_chat_completion(messages=messages, max_tokens=settings.MAX_TOKENS, temperature=0.6, top_p=0.95, top_k=20, presence_penalty=1.0)
    return llm.create_completion(prompt=prompt, max_tokens=settings.MAX_TOKENS, temperature=0.6, top_p=0.95, top_k=20, presence_penalty=1.0)

def choice_text(choice):
    if "message" in choice:
        return choice["message"]["content"]
    return choice["text"]

def run_completion(llm, messages):
    if settings.PRINT_PROCESSING_PROMPT:
        for message in messages:
            print(message["content"])
    start_time = time.perf_counter()
    try:
        result = generate(llm, messages)
    except ValueError as error:
        print(f"Warning: {error}")
        return None
    usage = result["usage"]
    if settings.PRINT_TOKEN_USAGE:
        print(f"Prompt tokens: {usage['prompt_tokens']}, completion tokens: {usage['completion_tokens']}, n_ctx: {llm.n_ctx()}")
    if settings.PRINT_GENERATION_SPEED:
        elapsed = time.perf_counter() - start_time
        tokens_per_second = usage["completion_tokens"] / elapsed if elapsed > 0 else 0.0
        print(f"Generated {usage['completion_tokens']} tokens in {elapsed:.2f}s ({tokens_per_second:.2f} tok/s)")
    choice = result["choices"][0]
    if choice["finish_reason"] == "length":
        print("Warning: generation filled the context, output was cut off.")
    return choice_text(choice).strip()

process_file.run_completion = run_completion

if __name__ == "__main__":
    process_file.main()
