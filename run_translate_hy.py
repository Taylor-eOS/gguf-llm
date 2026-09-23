from functools import partial
import utils_translate as tu

REPO_ID = "tencent/HY-MT1.5-7B-GGUF"
FILENAME = "HY-MT1.5-7B-Q8_0.gguf"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_translate.txt"
SEGMENT_MODE = True

def translate(llm, target_lang, text):
    if target_lang.strip().lower() in ("chinese", "zh", "mandarin", "中文"):
        prompt = f"将以下文本翻译为{target_lang},注意只需要输出翻译后的结果,不要额外解释: {text}"
    else:
        prompt = f"Translate the following segment into {target_lang}, without additional explanation. {text}"
    messages = [{"role": "user", "content": prompt}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

if __name__ == "__main__":
    target_lang = input("Target language (e.g. English, German, Spanish, Korean): ") or "English"
    llm = tu.load_model(REPO_ID, FILENAME)
    translate_fn = partial(translate, llm, target_lang)
    tu.translate_file(translate_fn, INPUT_FILE, OUTPUT_FILE, segment_mode=SEGMENT_MODE)
