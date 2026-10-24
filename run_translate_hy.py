from functools import partial
import utils_translate as tu

REPO_ID = "tencent/HY-MT1.5-7B-GGUF"
FILENAME = "HY-MT1.5-7B-Q8_0.gguf"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_translate.txt"
SEGMENT_MODE = True
LANG_MAP = {"e": "English", "g": "German", "s": "Spanish", "f": "French", "i": "Italian", "p": "Portuguese", "j": "Japanese", "k": "Korean", "c": "Chinese", "r": "Russian", "a": "Arabic", "n": "Norwegian", "d": "Danish",}

def resolve_language(raw: str) -> str:
    raw = (raw or "").strip()
    if not raw:
        return "English"
    key = raw.lower()
    if len(key) == 1 and key in LANG_MAP:
        return LANG_MAP[key]
    return raw

def translate(llm, target_lang, text):
    if target_lang.strip().lower() in ("chinese", "zh", "mandarin", "中文"):
        prompt = f"将以下文本翻译为中文,注意只需要输出翻译后的结果,不要额外解释: {text}"
    else:
        prompt = f"Translate the following segment into natural {target_lang}, without additional commentary: {text}"
    messages = [{"role": "user", "content": prompt}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

if __name__ == "__main__":
    raw = input("Target language (e.g. e=English, g=German, s=Spanish): ")
    target_lang = resolve_language(raw)
    print(f"Using target language: {target_lang}")
    llm = tu.load_model(REPO_ID, FILENAME)
    translate_fn = partial(translate, llm, target_lang)
    tu.translate_file(translate_fn, INPUT_FILE, OUTPUT_FILE, segment_mode=SEGMENT_MODE)
