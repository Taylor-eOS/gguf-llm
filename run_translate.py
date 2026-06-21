from huggingface_hub import hf_hub_download
from llama_cpp import Llama

MODEL = {
    "repo_id": "mradermacher/translategemma-12b-it-i1-GGUF",
    "filename": "translategemma-12b-it.i1-IQ4_NL.gguf",
}
SOURCE_LANG = "en"
TARGET_LANG = "de"
SAMPLE_TEXT = "The quick brown fox jumps over the lazy dog."
N_CTX = 4096
N_THREADS = 6

def load_model():
    path = hf_hub_download(repo_id=MODEL["repo_id"], filename=MODEL["filename"])
    return Llama(model_path=path, n_ctx=N_CTX, n_threads=N_THREADS, verbose=False)

def translate(llm, text):
    messages = [{"role": "user", "content": [{
        "type": "text",
        "source_lang_code": SOURCE_LANG,
        "target_lang_code": TARGET_LANG,
        "text": text,
    }]}]
    print()
    stream = llm.create_chat_completion(messages=messages, stream=True)
    for chunk in stream:
        delta = chunk["choices"][0]["delta"]
        token = delta.get("content", "")
        if token:
            print(token, end="", flush=True)
    print()

if __name__ == "__main__":
    llm = load_model()
    translate(llm, SAMPLE_TEXT)
