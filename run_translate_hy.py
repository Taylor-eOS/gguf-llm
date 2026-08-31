from functools import partial
import translate_utils as tu

REPO_ID = "tencent/HY-MT1.5-7B-GGUF"
FILENAME = "HY-MT1.5-7B-Q8_0.gguf"
#REPO_ID = "mradermacher/Huihui-HY-MT1.5-7B-abliterated-i1-GGUF"
#FILENAME = "Huihui-HY-MT1.5-7B-abliterated.i1-Q6_K.gguf"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_translate.txt"
SEGMENT_MODE = True

def translate(llm, source_lang, target_lang, text):
    prompt = f"Translate the following text from {source_lang} to {target_lang}.\nText: {text}"
    messages = [{"role": "user", "content": prompt}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

def main():
    source_lang = input("Source language (e.g. English, German, Spanish, French, Japanese, Korean): ") or "English"
    target_lang = input("Target language (e.g. German, English, Spanish, French, Japanese, Korean): ") or "German"

    llm = tu.load_model(REPO_ID, FILENAME)
    translate_fn = partial(translate, llm, source_lang, target_lang)
    tu.translate_file(translate_fn, INPUT_FILE, OUTPUT_FILE, segment_mode=SEGMENT_MODE)

if __name__ == "__main__":
    main()
