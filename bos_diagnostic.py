from utils import pick_model, load_tokenizer

def main():
    model = pick_model()
    llm = load_tokenizer(model)
    template = llm.metadata.get("tokenizer.chat_template", "")
    print("add_bos_token:", llm.metadata.get("tokenizer.ggml.add_bos_token"))
    print("bos_token_id:", llm.metadata.get("tokenizer.ggml.bos_token_id"))
    print("template mentions bos_token:", "bos_token" in template)

    print("mentions enable_thinking:", "enable_thinking" in template)
    print("mentions think:", "think" in template)
    print(template[-600:])

if __name__ == "__main__":
    main()
