from llama_cpp.llama_chat_format import Jinja2ChatFormatter
from utils import build_messages, configure_system_role, load_tokenizer, pick_model
import process_file
import settings

SAMPLE_TEXT = "Please tell me a joke."
SAMPLE_INPUT = "The topic is cats."

def token_text(llm, token_id):
    if token_id < 0:
        return ""
    return llm.detokenize([token_id], special=True).decode("utf-8", errors="replace")

def render(llm, messages):
    template = llm.metadata.get("tokenizer.chat_template")
    if not template:
        return None
    formatter = Jinja2ChatFormatter(template=template, eos_token=token_text(llm, llm.token_eos()), bos_token=token_text(llm, llm.token_bos()))
    try:
        return formatter(messages=messages).prompt
    except Exception as error:
        return f"Template error: {error}"

def show(title, llm, messages):
    prompt = render(llm, messages)
    if prompt is None:
        print("This model has no chat template in its metadata, llama-cpp-python falls back to a default format.")
        for message in messages:
            print(f"[{message['role']}] {message['content']}")
        return
    print(prompt)

def process_file_messages():
    settings.REQUEST = SAMPLE_TEXT
    return build_messages(settings.BASE, process_file.build_user_prompt(SAMPLE_INPUT), process_file.build_process_prompt(SAMPLE_INPUT))

def run_messages():
    return build_messages(settings.SYSTEM_INSTRUCTION, SAMPLE_TEXT, settings.SYSTEM_INSTRUCTION + " <prompt> " + SAMPLE_TEXT + " </prompt> ")

def main():
    model = pick_model()
    configure_system_role(model)
    llm = load_tokenizer(model)
    show("process_file.py", llm, process_file_messages())
    show("run.py", llm, run_messages())

if __name__ == "__main__":
    main()
