from huggingface_hub import hf_hub_download
from llama_cpp import Llama
import json

PARAGRAPH_PLACEHOLDER = "\x00"

def load_model(repo_id, filename, n_ctx=16 * 1024, n_threads=6):
    path = hf_hub_download(repo_id=repo_id, filename=filename)
    return Llama(model_path=path, n_ctx=n_ctx, n_threads=n_threads, verbose=False)

def read_elements(input_file, segment_mode=True):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    elements = []
    block = []
    for line in lines:
        if not line.strip():
            if block:
                elements.append("\n".join(block))
                block = []
            elements.append(PARAGRAPH_PLACEHOLDER)
        elif segment_mode:
            block.append(line)
        else:
            elements.append(line)
    if block:
        elements.append("\n".join(block))
    return elements

def clean_translation(translation):
    return "\n".join(line for line in translation.splitlines() if line.strip())

def make_pair(counter, original, translation):
    if original == PARAGRAPH_PLACEHOLDER:
        return {"number": counter, "original": "[PARAGRAPH_BREAK]", "translation": "[PARAGRAPH_BREAK]", "advice": "", "corrected": True}
    return {"number": counter, "original": original, "translation": translation, "advice": "", "corrected": False}

def build_translation_pairs(translate_fn, elements, json_file, on_progress=None):
    pairs = []
    for counter, element in enumerate(elements):
        if element == PARAGRAPH_PLACEHOLDER:
            translation = PARAGRAPH_PLACEHOLDER
        else:
            translation = clean_translation(translate_fn(element))
            print(translation)
        pairs.append(make_pair(counter, element, translation))
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(pairs, f, ensure_ascii=False, indent=4)
        if on_progress is not None:
            on_progress(pairs)
    return pairs

def write_txt(pairs, output_file):
    lines = ["" if pair["original"] == "[PARAGRAPH_BREAK]" else pair["translation"] for pair in pairs]
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def translate_file(translate_fn, input_file, output_file, segment_mode=True):
    elements = read_elements(input_file, segment_mode=segment_mode)
    json_file = output_file.replace(".txt", ".json")
    on_progress = lambda pairs: write_txt(pairs, output_file)
    pairs = build_translation_pairs(translate_fn, elements, json_file, on_progress=on_progress)
    write_txt(pairs, output_file)
    print("Translation written to output files.")
