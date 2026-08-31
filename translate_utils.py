from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import json

PARAGRAPH_PLACEHOLDER = "\x00"

def load_model(repo_id, filename, n_ctx=8 * 1024, n_threads=6):
    path = hf_hub_download(repo_id=repo_id, filename=filename)
    return Llama(model_path=path, n_ctx=n_ctx, n_threads=n_threads, verbose=False)

def read_elements(input_file, segment_mode=True):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    elements = []
    for i, paragraph in enumerate(text.split("\n\n")):
        if i > 0:
            elements.append(PARAGRAPH_PLACEHOLDER)
        if segment_mode:
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

def build_translation_pairs(translate_fn, elements, json_file):
    pairs = []
    for counter, element in enumerate(elements):
        translation = PARAGRAPH_PLACEHOLDER if element == PARAGRAPH_PLACEHOLDER else translate_fn(element)
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

def translate_file(translate_fn, input_file, output_file, segment_mode=True):
    elements = read_elements(input_file, segment_mode=segment_mode)
    json_file = output_file.replace(".txt", ".json")
    pairs = build_translation_pairs(translate_fn, elements, json_file)
    write_txt(pairs, output_file)
    print("Translation written to output files")
