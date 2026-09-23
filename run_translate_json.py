from functools import partial
import json
import utils_translate as tu
from run_translate_hy import REPO_ID, FILENAME, translate

INPUT_FILE = "input.json"
OUTPUT_FILE = "output.json"
FILE_ENDING = "_translate.json"

def read_records(input_file):
    records = []
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records

def write_json_lines(records, pairs, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for record, pair in zip(records, pairs):
            entry = dict(record)
            entry["text"] = pair["translation"]
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    target_lang = input("Target language (e.g. English, German, Spanish, Korean): ") or "English"
    llm = tu.load_model(REPO_ID, FILENAME)
    translate_fn = partial(translate, llm, target_lang)
    records = read_records(INPUT_FILE)
    elements = [record["text"] for record in records]
    progress_file = OUTPUT_FILE.replace(".json", FILE_ENDING)
    on_progress = lambda pairs: write_json_lines(records, pairs, OUTPUT_FILE)
    pairs = tu.build_translation_pairs(translate_fn, elements, progress_file, on_progress=on_progress)
    write_json_lines(records, pairs, OUTPUT_FILE)
    print(f"Translation written to {OUTPUT_FILE}.")
