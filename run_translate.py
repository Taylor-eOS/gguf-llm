from huggingface_hub import hf_hub_download
from llama_cpp import Llama

REPO_ID = "mradermacher/translategemma-12b-it-i1-GGUF"
FILENAME = "translategemma-12b-it.i1-IQ4_NL.gguf"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_translate.txt"
SOURCE_LANG = "en"
TARGET_LANG = "de"
N_CTX = 4096
N_THREADS = 6

def load_model():
    path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
    return Llama(model_path=path, n_ctx=N_CTX, n_threads=N_THREADS, verbose=False)

def translate(llm, text):
    messages = [{"role": "user", "content": [{"type": "text", "source_lang_code": SOURCE_LANG, "target_lang_code": TARGET_LANG, "text": text,}]}]
    result = llm.create_chat_completion(messages=messages, stream=False)
    return result["choices"][0]["message"]["content"]

if __name__ == "__main__":
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        text = f.read()
    llm = load_model()
    result = translate(llm, text)
    print(result)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(result)
