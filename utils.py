from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from pathlib import Path
import settings

def is_cached(model):
    repo_slug = "models--" + model["repo_id"].replace("/", "--")
    return (Path.home() / ".cache" / "huggingface" / "hub" / repo_slug).is_dir()

def load_model(model):
    path = hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])
    return Llama(model_path=path, n_ctx=settings.N_CTX, n_threads=settings.N_THREADS, verbose=False)

def pick_model():
    DIM = "\033[2m"
    RESET = "\033[0m"
    cached_symb = "x"
    thinking_symb= "t"
    nonthinking_symb = "n"
    neither_symb = " "
    print(f"Available models ([{cached_symb}] = cached, [{nonthinking_symb}] = non-thinking):")
    for i, m in enumerate(settings.MODELS):
        tag = f"[{cached_symb}]" if is_cached(m) else f"[{neither_symb}]"
        think_val = m.get("thinking")
        think_tag = f"[{thinking_symb}]" if think_val is True else (f"[{neither_symb}]" if think_val is None else f"[{nonthinking_symb}]")
        comment = f"  {DIM}({m['comment']}){RESET}" if m.get("comment") else "  ()"
        #print(f"{i + 1:2d} {tag}{think_tag} {m['repo_id']}{comment}")
        print(f"{i + 1:2d} {tag}{think_tag} {m['repo_id']}")
        if comment != "": print(f"        {comment}")
    while True:
        try:
            choice = input("Select model number: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            raise SystemExit
        if choice.isdigit() and 1 <= int(choice) <= len(settings.MODELS):
            return settings.MODELS[int(choice) - 1]
        print(f"Enter a number between 1 and {len(settings.MODELS)}.")

