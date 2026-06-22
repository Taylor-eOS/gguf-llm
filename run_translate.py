from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import json

N_CTX = 8 * 1024
N_THREADS = 6
REPO_ID = "mradermacher/translategemma-12b-it-i1-GGUF"
#FILENAME = "translategemma-12b-it.i1-IQ4_NL.gguf"
FILENAME = "translategemma-12b-it.i1-Q6_K.gguf"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_translate.txt"
SOURCE_LANG = "en"
TARGET_LANG = "de"
SEGMENT_MODE = True

PARAGRAPH_PLACEHOLDER = "\x00"

def load_model():
    path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    return Llama(model_path=path, n_ctx=N_CTX, n_threads=N_THREADS, verbose=False)

def translate(llm, text):
    messages = [{"role": "user", "content": [{"type": "text", "source_lang_code": SOURCE_LANG, "target_lang_code": TARGET_LANG, "text": text}]}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

def read_elements(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    elements = []
    for i, paragraph in enumerate(text.split("\n\n")):
        if i > 0:
            elements.append(PARAGRAPH_PLACEHOLDER)
        if SEGMENT_MODE:
            segment = "\n".join(line for line in paragraph.splitlines() if line.strip())
            if segment:
                elements.append(segment)
        else:
            elements.extend(line for line in paragraph.splitlines() if line.strip())
    return elements

def make_pair(counter, original, translation):
    if original == PARAGRAPH_PLACEHOLDER:
        return {"number": counter, "original": "[PARAGRAPH_BREAK]", "translation": "[PARAGRAPH_BREAK]", "advice": "", "corrected": True}
    return {"number": counter, "original": original, "translation": translation, "advice": "", "corrected": False}

def build_translation_pairs(llm, elements, json_file):
    pairs = []
    for counter, element in enumerate(elements):
        translation = PARAGRAPH_PLACEHOLDER if element == PARAGRAPH_PLACEHOLDER else translate(llm, element)
        if element != PARAGRAPH_PLACEHOLDER:
            print(translation)
        pairs.append(make_pair(counter, element, translation))
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(pairs, f, ensure_ascii=False, indent=4)
    return pairs

def write_txt(pairs, output_file):
    paragraphs = []
    current = []
    for pair in pairs:
        if pair["original"] == "[PARAGRAPH_BREAK]":
            paragraphs.append("\n".join(current))
            current = []
        else:
            current.append(pair["translation"])
    paragraphs.append("\n".join(current))
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n\n".join(paragraphs))

def translate_file(llm, input_file, output_file):
    elements = read_elements(input_file)
    json_file = output_file.replace(".txt", ".json")
    pairs = build_translation_pairs(llm, elements, json_file)
    write_txt(pairs, output_file)
    print(f"Translation written to output files")

if __name__ == "__main__":
    llm = load_model()
    translate_file(llm, INPUT_FILE, OUTPUT_FILE)
