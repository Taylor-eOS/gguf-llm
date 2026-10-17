from datetime import datetime
from jinja2 import TemplateError
from jinja2.sandbox import ImmutableSandboxedEnvironment

EXPECTED_BOS_COUNT = {"no_bos": 0, "bos_in_template": 1, "bos_by_tokenizer": 1}
ENVIRONMENT = ImmutableSandboxedEnvironment(trim_blocks=True, lstrip_blocks=True)
ENVIRONMENT.globals["strftime_now"] = lambda fmt: datetime.now().strftime(fmt)
MECHANISM = None
BOS_MODE = "no_bos"
TEMPLATE = None
BOS_TEXT = ""
EOS_TEXT = ""
STOP_TEXTS = []

def raise_template_exception(message):
    raise ValueError(message)

def special_token_text(llm, key):
    token_id = llm.metadata.get(key)
    if token_id is None:
        return ""
    return llm.detokenize([int(token_id)], special=True).decode("utf-8", errors="ignore")

def stop_texts(llm):
    texts = []
    for key in ("tokenizer.ggml.eos_token_id", "tokenizer.ggml.eot_token_id"):
        text = special_token_text(llm, key)
        if text and text not in texts:
            texts.append(text)
    return texts

def render(messages, **variables):
    try:
        return TEMPLATE.render(messages=messages, add_generation_prompt=True, bos_token=BOS_TEXT, eos_token=EOS_TEXT, raise_exception=raise_template_exception, **variables)
    except TemplateError as error:
        raise ValueError(f"Chat template error: {error}") from error

def disable_with_enable_thinking(messages):
    return render(messages, enable_thinking=False)

def disable_with_empty_think(messages):
    prompt = render(messages)
    if not prompt.endswith("<think>\n"):
        prompt += "<think>\n"
    return prompt + "\n</think>\n\n"

MECHANISMS = {"enable_thinking": disable_with_enable_thinking, "empty_think": disable_with_empty_think}

def tokenize_prompt(llm, text):
    return llm.tokenize(text.encode("utf-8"), add_bos=BOS_MODE == "bos_by_tokenizer", special=True)

def leading_bos_count(llm, tokens):
    bos_id = llm.token_bos()
    count = 0
    for token in tokens:
        if bos_id < 0 or token != bos_id:
            break
        count += 1
    return count

def check_bos(llm):
    tokens = tokenize_prompt(llm, MECHANISM([{"role": "user", "content": "probe"}]))
    found = leading_bos_count(llm, tokens)
    expected = EXPECTED_BOS_COUNT[BOS_MODE]
    if found != expected:
        print(f"Warning: the prompt starts with {found} BOS tokens but \"{BOS_MODE}\" expects {expected}. Check disable_thinking entry.")
    elif BOS_MODE == "no_bos" and llm.metadata.get("tokenizer.ggml.add_bos_token") == "true":
        print("Warning: the model metadata asks for a BOS token but \"no_bos\" adds none. Consider bos_by_tokenizer.")

def deactivate(reason):
    global MECHANISM
    MECHANISM = None
    print(f"Warning: {reason}, thinking stays enabled.")

def ask(model):
    global MECHANISM, BOS_MODE
    MECHANISM = None
    setting = model.get("disable_thinking")
    if not isinstance(setting, str) or not setting:
        return
    name, _, bos_mode = setting.partition("/")
    bos_mode = bos_mode or "no_bos"
    if name not in MECHANISMS or bos_mode not in EXPECTED_BOS_COUNT:
        print(f"Warning: unknown disable_thinking setting \"{setting}\", thinking stays enabled.")
        return
    if input("Disable thinking? [y/N]: ").strip().lower() in ("y", "yes"):
        MECHANISM = MECHANISMS[name]
        BOS_MODE = bos_mode
        print(f"Disabling thinking via {setting}.")

def prepare(llm):
    global TEMPLATE, BOS_TEXT, EOS_TEXT, STOP_TEXTS
    if MECHANISM is None:
        return
    source = llm.metadata.get("tokenizer.chat_template")
    if not source:
        deactivate("the model has no chat template")
        return
    try:
        TEMPLATE = ENVIRONMENT.from_string(source)
        BOS_TEXT = special_token_text(llm, "tokenizer.ggml.bos_token_id")
        EOS_TEXT = special_token_text(llm, "tokenizer.ggml.eos_token_id")
        STOP_TEXTS = stop_texts(llm)
        check_bos(llm)
    except (TemplateError, ValueError) as error:
        deactivate(f"the chat template could not be set up ({error})")

def as_chat_result(result):
    choice = result["choices"][0]
    return {"usage": result["usage"], "choices": [{"finish_reason": choice["finish_reason"], "message": {"content": choice["text"]}}]}

def generate(llm, messages, **sampling):
    if MECHANISM is None:
        return llm.create_chat_completion(messages=messages, **sampling)
    tokens = tokenize_prompt(llm, MECHANISM(messages))
    return as_chat_result(llm.create_completion(prompt=tokens, stop=STOP_TEXTS, **sampling))
