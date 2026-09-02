import os
import sys
from datetime import datetime
from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from pathlib import Path
import settings
import models

WRITE_LOG = False
PERFORMANCE_METRICS = False
MODEL_LOG_PATH = Path(__file__).resolve().parent / "llm_use.log"

def is_cached(model):
    repo_slug = "models--" + model["repo_id"].replace("/", "--")
    return (Path.home() / ".cache" / "huggingface" / "hub" / repo_slug).is_dir()

def log_model_use(model):
    MODEL_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(MODEL_LOG_PATH, "a") as f:
        f.write(f"{timestamp} {model['repo_id']} {model['filename']}\n")

def load_model(model, c_ntx=settings.N_CTX, redirect_logs=WRITE_LOG):
    log_model_use(model)
    path = hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])
    log_target = "llama_output.log" if redirect_logs else os.devnull
    log_file = open(log_target, "a" if redirect_logs else "w")
    old_stdout = os.dup(1)
    old_stderr = os.dup(2)
    os.dup2(log_file.fileno(), 1)
    os.dup2(log_file.fileno(), 2)
    try:
        llm = Llama(
            model_path=path,
            n_ctx=c_ntx,
            n_threads=settings.N_THREADS,
            n_batch=512,
            use_mmap=True,
            use_mlock=False,
            verbose=PERFORMANCE_METRICS
        )
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        os.dup2(old_stdout, 1)
        os.dup2(old_stderr, 2)
        os.close(old_stdout)
        os.close(old_stderr)
        log_file.close()
    return llm

def pick_model():
    DIM = "\033[2m"
    RESET = "\033[0m"
    cached_symb = "x"
    thinking_symb= "T"
    nonthinking_symb = "n"
    neither_symb = " "
    print(f"Available models ([{cached_symb}] = cached, [{nonthinking_symb}] = non-thinking):")
    for i, m in enumerate(models.MODELS):
        tag = f"[{cached_symb}]" if is_cached(m) else f"[{neither_symb}]"
        think_val = m.get("thinking")
        think_tag = f"[{thinking_symb}]" if think_val is True else (f"[{neither_symb}]" if think_val is None else f"[{nonthinking_symb}]")
        comment = f"  {DIM}{m['comment']}{RESET}" if m.get("comment") else "  "
        print(f"{i + 1:2d} {tag}{think_tag} {m['repo_id']}")
        if comment != "":
            print(f"        {comment}")
    while True:
        try:
            choice = input("Select model number: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            raise SystemExit
        if choice.isdigit() and 1 <= int(choice) <= len(models.MODELS):
            return models.MODELS[int(choice) - 1]
        print(f"Enter a number between 1 and {len(models.MODELS)}.")

def split_lines_by_tokens(llm, lines, max_tokens):
    line_tokens = [len(llm.tokenize(line.encode("utf-8"), add_bos=False)) for line in lines]
    total_tokens = sum(line_tokens)
    if total_tokens == 0:
        return [lines] if lines else []
    num_chunks = max(1, -(-total_tokens // max_tokens))
    target_tokens = -(-total_tokens // num_chunks)
    chunks = []
    current = []
    current_tokens = 0
    for line, tokens in zip(lines, line_tokens):
        if current and current_tokens + tokens > max_tokens:
            chunks.append(current)
            current = []
            current_tokens = 0
        elif current and current_tokens >= target_tokens and len(chunks) < num_chunks - 1:
            chunks.append(current)
            current = []
            current_tokens = 0
        current.append(line)
        current_tokens += tokens
    if current:
        chunks.append(current)
    return chunks

def strip_think(text):
    marker = "</think>"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[idx + len(marker):].strip()
