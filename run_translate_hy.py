import run_translate as rt

rt.REPO_ID = "tencent/HY-MT1.5-7B-GGUF"
rt.FILENAME = "HY-MT1.5-7B-Q8_0.gguf"
#rt.REPO_ID = "mradermacher/Huihui-HY-MT1.5-7B-abliterated-i1-GGUF"
#rt.FILENAME = "Huihui-HY-MT1.5-7B-abliterated.i1-Q6_K.gguf"
rt.SOURCE_LANG = input("Source language (e.g. English, German, Spanish, French, Japanese, Korean): ") or "English"
rt.TARGET_LANG = input("Target language (e.g. German, English, Spanish, French, Japanese, Korean): ") or "German"

def translate_hy(llm, text):
    prompt = f"Translate the following text from {rt.SOURCE_LANG} to {rt.TARGET_LANG}.\nText: {text}"
    messages = [{"role": "user", "content": prompt}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

rt.translate = translate_hy

if __name__ == "__main__":
    llm = rt.load_model()
    rt.translate_file(llm, rt.INPUT_FILE, rt.OUTPUT_FILE)
