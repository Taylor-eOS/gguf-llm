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
INSTRUCTION_LOG_PATH = Path(__file__).resolve().parent / "instruction_use.log"
os.environ["HF_HUB_OFFLINE"] = "1"

def is_cached(model):
    repo_slug = "models--" + model["repo_id"].replace("/", "--")
    return (Path.home() / ".cache" / "huggingface" / "hub" / repo_slug).is_dir()

def log_model_use(model):
    MODEL_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(MODEL_LOG_PATH, "a") as f:
        f.write(f"{timestamp} {model['repo_id']} {model['filename']}\n")

def log_instruction_use(instruction):
    INSTRUCTION_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(INSTRUCTION_LOG_PATH, "a") as f:
        f.write(f"{timestamp} {instruction}\n")

def construct_llama(path, llama_kwargs, redirect_logs):
    log_target = "llama_output.log" if redirect_logs else os.devnull
    log_file = open(log_target, "a" if redirect_logs else "w")
    old_stdout = os.dup(1)
    old_stderr = os.dup(2)
    os.dup2(log_file.fileno(), 1)
    os.dup2(log_file.fileno(), 2)
    try:
        llm = Llama(model_path=path, **llama_kwargs)
    finally:
        sys.stdout.flush()
        sys.stderr.flush()
        os.dup2(old_stdout, 1)
        os.dup2(old_stderr, 2)
        os.close(old_stdout)
        os.close(old_stderr)
        log_file.close()
    return llm

def load_model(model, c_ntx=None, redirect_logs=WRITE_LOG):
    if c_ntx is None:
        c_ntx = settings.N_CTX
    log_model_use(model)
    path = hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])
    batch_size = min(c_ntx, settings.MODEL_N_BATCH)
    llama_kwargs = {
        "n_ctx": c_ntx,
        "n_threads": settings.N_THREADS,
        "n_batch": batch_size,
        "n_ubatch": batch_size,
        "use_mmap": True,
        "use_mlock": False,
        "verbose": PERFORMANCE_METRICS,
    }
    return construct_llama(path, llama_kwargs, redirect_logs)

def load_tokenizer(model, redirect_logs=WRITE_LOG):
    path = hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])
    llama_kwargs = {
        "n_ctx": 32,
        "n_threads": settings.N_THREADS,
        "n_batch": settings.TOKENIZER_N_BATCH,
        "use_mmap": True,
        "use_mlock": False,
        "vocab_only": True,
        "verbose": PERFORMANCE_METRICS,
    }
    return construct_llama(path, llama_kwargs, redirect_logs)

def print_model_list(models_list):
    DIM = "\033[2m"
    RESET = "\033[0m"
    cached_symb = "x"
    thinking_symb = "T"
    nonthinking_symb = "n"
    neither_symb = " "
    repo_id_counts = {}
    for m in models_list:
        repo_id_counts[m["repo_id"]] = repo_id_counts.get(m["repo_id"], 0) + 1
    for i, m in enumerate(models_list):
        tag = f"[{cached_symb}]" if is_cached(m) else f"[{neither_symb}]"
        think_val = m.get("thinking")
        think_tag = f"[{thinking_symb}]" if think_val is True else (f"[{neither_symb}]" if think_val is None else f"[{nonthinking_symb}]")
        comment = f"{DIM}{m['comment']}{RESET}" if m.get("comment") else "  "
        dup_marker = "*" if repo_id_counts[m["repo_id"]] > 1 else ""
        print(f"{i + 1:2d} {tag}{think_tag} {m['repo_id']}{dup_marker}")
        if comment != "":
            print(f"          {comment}")

def filter_models(models_list, query):
    tokens = query.lower().split()
    if not tokens:
        return models_list
    thinking_only = "t" in tokens
    nonthinking_only = "n" in tokens
    tokens = [tok for tok in tokens if tok not in ("t", "n")]
    filtered = []
    for m in models_list:
        think_val = m.get("thinking")
        if thinking_only and think_val is not True:
            continue
        if nonthinking_only and think_val is not False:
            continue
        haystack = m["repo_id"].lower()
        if m.get("comment"):
            haystack += " " + m["comment"].lower()
        if all(tok in haystack for tok in tokens):
            filtered.append(m)
    return filtered

def pick_model():
    cached_symb = "x"
    nonthinking_symb = "n"
    current = models.MODELS
    print(f"Available models ([{cached_symb}] = cached, [{nonthinking_symb}] = non-thinking):")
    print_model_list(current)
    print("Type keywords to filter, a number to select, * to reset.")
    while True:
        try:
            raw = input("Filter / select: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            raise SystemExit
        if raw == "*":
            current = models.MODELS
            print_model_list(current)
            continue
        if raw.isdigit():
            idx = int(raw)
            if 1 <= idx <= len(current):
                return current[idx - 1]
            print(f"Enter a number between 1 and {len(current)}.")
            continue
        if raw == "" and len(current) == 1:
            return current[0]
        if raw == "":
            print_model_list(current)
            continue
        narrowed = filter_models(current, raw)
        if not narrowed:
            print("No matches. List unchanged, try different keywords or * to reset.")
            continue
        current = narrowed
        print_model_list(current)
        if len(current) == 1:
            try:
                confirm = input(f"Use {current[0]['repo_id']}? [Y/n]: ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                print("\nExiting.")
                raise SystemExit
            if confirm != "n":
                return current[0]

def strip_think(text):
    marker = "</think>"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[idx + len(marker):].strip()
