from functools import partial
import translate_utils as tu

#REPO_ID = "mradermacher/translategemma-12b-it-i1-GGUF"
#FILENAME = "translategemma-12b-it.i1-IQ4_NL.gguf"
#FILENAME = "translategemma-12b-it.i1-Q6_K.gguf"
REPO_ID = "steampunque/translategemma-12b-it-MP-GGUF"
FILENAME = "translategemma-12b-it.Q4_E_H.gguf"  # "translategemma-12b-it.Q6_K_H.gguf"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_translate.txt"
SEGMENT_MODE = True

def translate(llm, source_lang, target_lang, text):
    messages = [{"role": "user", "content": [{
        "type": "text",
        "source_lang_code": source_lang,
        "target_lang_code": target_lang,
        "text": text,
    }]}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

def main():
    source_lang = input("Source language (e.g. en, de, da, es): ") or "en"
    target_lang = input("Target language (e.g. de, en, da, es): ") or "de"
    llm = tu.load_model(REPO_ID, FILENAME)
    translate_fn = partial(translate, llm, source_lang, target_lang)
    tu.translate_file(translate_fn, INPUT_FILE, OUTPUT_FILE, segment_mode=SEGMENT_MODE)

if __name__ == "__main__":
    main()
