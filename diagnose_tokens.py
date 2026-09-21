from utils import load_model, pick_model
import importlib.metadata
import settings

TEST_PASTE_PATH = "input.txt"

def get_llama_cpp_version():
    try:
        return importlib.metadata.version("llama-cpp-python")
    except importlib.metadata.PackageNotFoundError:
        return "not installed / not found via importlib.metadata"

def load_test_paste():
    try:
        with open(TEST_PASTE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"No {TEST_PASTE_PATH} found in the current directory.")
        try:
            return input("Paste the test text directly (single line), then press Enter: ")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            raise SystemExit

def count_tokens(llm, text):
    return len(llm.tokenize(text.encode("utf-8"), add_bos=False))

def run_diagnosis():
    version = get_llama_cpp_version()
    print(f"llama-cpp-python version: {version}")
    print(f"settings.N_CTX: {getattr(settings, 'N_CTX', 'undefined')}")
    print(f"settings.MODEL_N_BATCH: {getattr(settings, 'MODEL_N_BATCH', 'undefined')}")
    model = pick_model()
    llm = load_model(model)
    instruction = settings.SYSTEM_INSTRUCTION
    instruction_tokens = count_tokens(llm, instruction)
    print(f"SYSTEM_INSTRUCTION token count: {instruction_tokens}")
    paste = load_test_paste()
    paste_tokens = count_tokens(llm, paste)
    print(f"Test paste token count: {paste_tokens}")
    combined = paste + instruction
    combined_tokens = count_tokens(llm, combined)
    print(f"Combined (paste + SYSTEM_INSTRUCTION) token count: {combined_tokens}")
    print(f"Sum of separate counts: {paste_tokens + instruction_tokens}")
    n_ctx = getattr(settings, "N_CTX", None)
    if n_ctx is not None:
        print(f"Combined tokens vs N_CTX: {combined_tokens} / {n_ctx}")
        print(f"Headroom remaining: {n_ctx - combined_tokens}")

if __name__ == "__main__":
    run_diagnosis()
