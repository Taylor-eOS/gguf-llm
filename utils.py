import os
import sys
import time
import json
from pathlib import Path
from llama_cpp import Llama
from utils_helpers import data_path, log_model_use, log_instruction_use, resolve_model_path, available_memory_bytes, ask_or_exit, strip_think, wait_while_stopped, next_free_path
import models
import settings

def is_cached(model):
    repo_slug = "models--" + model["repo_id"].replace("/", "--")
    return (Path.home() / ".cache" / "huggingface" / "hub" / repo_slug).is_dir()

def remember_model(model):
    save_state_value("model", {"repo_id": model["repo_id"], "filename": model["filename"]})

def configure_system_role(model):
    settings.USE_SYSTEM_ROLE = not model.get("no_system_role", False)
    if not settings.USE_SYSTEM_ROLE:
        print("Model is marked no_system_role, putting the instruction into the user message.")

def build_messages(system, user, flat_prompt):
    if settings.USE_SYSTEM_ROLE:
        return [{"role": "system", "content": system}, {"role": "user", "content": user}]
    return [{"role": "user", "content": flat_prompt}]

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

def load_model(model, c_ntx=None, redirect_logs=settings.WRITE_LOG):
    if c_ntx is None:
        c_ntx = settings.N_CTX
    log_model_use(model)
    remember_model(model)
    configure_system_role(model)
    path = resolve_model_path(model)
    batch_size = min(c_ntx, settings.MODEL_N_BATCH)
    llama_kwargs = {
        "n_ctx": c_ntx,
        "n_threads": settings.N_THREADS,
        "n_batch": batch_size,
        "n_ubatch": batch_size,
        "flash_attn": True,
        "use_mmap": True,
        "use_mlock": False,
        "verbose": settings.PERFORMANCE_METRICS,
    }
    return construct_llama(path, llama_kwargs, redirect_logs)

def metadata_int(metadata, key):
    value = metadata.get(key)
    if value is None:
        return None
    try:
        parsed = json.loads(value)
    except ValueError:
        return None
    if isinstance(parsed, list):
        parsed = max(parsed) if parsed else None
    return parsed if isinstance(parsed, int) else None

def kv_bytes_per_token(metadata):
    arch = metadata["general.architecture"]
    layers = metadata_int(metadata, f"{arch}.block_count")
    heads = metadata_int(metadata, f"{arch}.attention.head_count")
    heads_kv = metadata_int(metadata, f"{arch}.attention.head_count_kv") or heads
    embd = metadata_int(metadata, f"{arch}.embedding_length")
    key_len = metadata_int(metadata, f"{arch}.attention.key_length") or embd // heads
    value_len = metadata_int(metadata, f"{arch}.attention.value_length") or key_len
    return layers * heads_kv * (key_len + value_len) * 2

def memory_derived_ctx(model, longest_prompt=None):
    tokenizer_llm = load_tokenizer(model)
    metadata = dict(tokenizer_llm.metadata)
    del tokenizer_llm
    try:
        per_token = kv_bytes_per_token(metadata)
    except (KeyError, TypeError):
        print(f"Could not read the KV cache geometry from the model metadata, falling back to N_CTX of {settings.N_CTX}.")
        return settings.N_CTX
    usable = int(available_memory_bytes() * settings.MEMORY_FRACTION)
    memory_ctx = usable // per_token
    trained = metadata_int(metadata, f"{metadata['general.architecture']}.context_length")
    n_ctx = min(memory_ctx, settings.N_CTX_MAX)
    if trained:
        n_ctx = min(n_ctx, trained)
    if longest_prompt is not None:
        n_ctx = min(n_ctx, max(settings.N_CTX_MIN, longest_prompt + settings.RESERVE_TOKENS))
    if n_ctx < 1024:
        fallback = min(settings.N_CTX, trained) if trained else settings.N_CTX
        print(f"The memory estimate allows only {n_ctx} tokens of context, using {fallback} instead.")
        return fallback
    print(f"KV cache estimate: {per_token * n_ctx / 1024 ** 3:.2f} GiB for {n_ctx} tokens (memory would allow {memory_ctx}).")
    return n_ctx

def load_tokenizer(model, redirect_logs=settings.WRITE_LOG):
    path = resolve_model_path(model)
    llama_kwargs = {
        "n_ctx": 32,
        "n_threads": settings.N_THREADS,
        "n_batch": settings.TOKENIZER_N_BATCH,
        "use_mmap": True,
        "use_mlock": False,
        "vocab_only": True,
        "verbose": settings.PERFORMANCE_METRICS,
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
        print(f"{i + 1:2d} {tag}{think_tag} {m['repo_id'][:88]}{dup_marker}")
        if comment != "":
            print(f"          {comment}")

def filter_models(models_list, query):
    tokens = query.lower().split()
    if not tokens:
        return models_list
    thinking_only = "t" in tokens
    nonthinking_only = "n" in tokens
    cached_only = "x" in tokens
    tokens = [tok for tok in tokens if tok not in ("t", "n", "x")]
    filtered = []
    for m in models_list:
        think_val = m.get("thinking")
        if thinking_only and think_val is not True:
            continue
        if nonthinking_only and think_val is not False:
            continue
        if cached_only and not is_cached(m):
            continue
        haystack = m["repo_id"].lower()
        if m.get("comment"):
            haystack += " " + m["comment"].lower()
        if all(tok in haystack for tok in tokens):
            filtered.append(m)
    return filtered

def available_models():
    return [m for m in models.MODELS if m.get("repo_id") and m.get("filename")]

def print_model_menu(last_model, current):
    cached_symb = "x"
    nonthinking_symb = "n"
    print(f"Available models ([{cached_symb}] = cached, [{nonthinking_symb}] = non-thinking):")
    if last_model is not None:
        print(f"l: Last used model: {last_model['repo_id']} ({last_model['filename']})")
    print_model_list(current)
    print("Keywords to filter, number to select, l or Enter for last used, * to reset, t thinking models, n non-thinking, x downloaded.")

def select_by_number(raw, current):
    idx = int(raw)
    if 1 <= idx <= len(current):
        return current[idx - 1]
    print(f"Enter a number between 1 and {len(current)}.")
    return None

def confirm_model(model):
    return ask_or_exit(f"Use {model['repo_id']}? [Y/n]: ").lower() != "n"

def pick_model():
    all_models = available_models()
    if not all_models:
        print("No usable models defined.")
        raise SystemExit
    last_model = find_last_model(all_models)
    current = all_models
    print_model_menu(last_model, current)
    while True:
        raw = ask_or_exit("Filter / select: ")
        if raw == "" and len(current) == 1:
            return current[0]
        if raw.lower() == "l" or (raw == "" and last_model in current):
            if last_model is None:
                print("No last used model saved.")
                continue
            return last_model
        if raw == "*":
            current = all_models
            print_model_list(current)
            continue
        if raw.isdigit():
            selected = select_by_number(raw, current)
            if selected is not None:
                return selected
            continue
        if raw == "":
            print_model_list(current)
            continue
        narrowed = filter_models(current, raw)
        if not narrowed:
            print("No matches.")
            continue
        current = narrowed
        print_model_list(current)
        if len(current) == 1 and confirm_model(current[0]):
            return current[0]

def read_state():
    state_path = data_path(settings.LAST_INSTRUCTION_FILE)
    if not state_path.is_file():
        return {}
    return json.loads(state_path.read_text(encoding="utf-8"))

def write_state(state):
    data_path(settings.LAST_INSTRUCTION_FILE).write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

def load_state_value(key, expected_type=None):
    value = read_state().get(key)
    if expected_type is not None and not isinstance(value, expected_type):
        return None
    return value

def save_state_value(key, value):
    state = read_state()
    state[key] = value
    write_state(state)

def find_last_model(models_list):
    last = load_state_value("model")
    if last is None:
        return None
    for m in models_list:
        if m["repo_id"] == last["repo_id"] and m["filename"] == last["filename"]:
            return m
    return None
