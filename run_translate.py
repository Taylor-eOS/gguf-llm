from huggingface_hub import hf_hub_download
from llama_cpp import Llama

N_CTX = 6 * 1024
N_THREADS = 6
REPO_ID = "mradermacher/translategemma-12b-it-i1-GGUF"
FILENAME = "translategemma-12b-it.i1-IQ4_NL.gguf"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_translate.txt"
SOURCE_LANG = "en"
TARGET_LANG = "de"

def load_model():
    path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    return Llama(model_path=path, n_ctx=N_CTX, n_threads=N_THREADS, verbose=False)

def translate(llm, text):
    messages = [{"role": "user", "content": [{"type": "text", "source_lang_code": SOURCE_LANG, "target_lang_code": TARGET_LANG, "text": text}]}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

def translate_file(llm, input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    paragraphs = text.split("\n\n")
    translated = []
    for i, paragraph in enumerate(paragraphs):
        lines = [line for line in paragraph.splitlines() if line.strip()]
        para_translated = []
        for line in lines:
            result = translate(llm, line)
            print(result)
            para_translated.append(result)
        translated.append("\n".join(para_translated))
    output = "\n\n".join(translated)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(output)

if __name__ == "__main__":
    llm = load_model()
    translate_file(llm, INPUT_FILE, OUTPUT_FILE)
