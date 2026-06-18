from huggingface_hub import hf_hub_download
from llama_cpp import Llama

path = hf_hub_download(
    repo_id="yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
    filename="gemma4-coding-Q4_K_M.gguf"
)

llm = Llama(
    model_path=path,
    n_ctx=2048,
    verbose=False,
)

response = llm.create_chat_completion(
    messages=[
        {"role": "user", "content": "Write a Python line that prints hello world."}
    ]
)

print(response["choices"][0]["message"]["content"])
