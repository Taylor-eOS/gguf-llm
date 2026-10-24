import time
import glob
from datetime import datetime
from pathlib import Path
from huggingface_hub.utils import LocalEntryNotFoundError
from huggingface_hub import hf_hub_download
import settings

def data_path(filename):
    return Path(__file__).resolve().parent / filename

def log_model_use(model):
    log_path = data_path(settings.MODEL_LOG_FILE)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{timestamp} {model['repo_id']} {model['filename']}\n")

def log_instruction_use(instruction):
    log_path = data_path(settings.INSTRUCTION_LOG_FILE)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"{timestamp} {instruction}\n")

def resolve_model_path(model):
    try:
        return hf_hub_download(repo_id=model["repo_id"], filename=model["filename"], local_files_only=True)
    except LocalEntryNotFoundError:
        print(f"{model['filename']} is not cached, downloading.")
        return hf_hub_download(repo_id=model["repo_id"], filename=model["filename"])

def available_memory_bytes():
    with open("/proc/meminfo", "r") as f:
        for line in f:
            if line.startswith("MemAvailable:"):
                return int(line.split()[1]) * 1024
    raise RuntimeError("MemAvailable not found in /proc/meminfo")

def ask_or_exit(prompt):
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting.")
        raise SystemExit

def strip_think(text):
    marker = "</think>"
    idx = text.find(marker)
    if idx == -1:
        return text
    return text[idx + len(marker):].strip()

def wait_while_stopped():
    if not Path(settings.PAUSE_FLAG).is_file():
        return
    print("Stop file detected, pausing.")
    while Path(settings.PAUSE_FLAG).is_file():
        time.sleep(10)
    print("Stop file removal detected, resuming.")

def next_free_path(template):
    prefix, suffix = template.split("{n}")
    highest = 0
    for match in glob.glob(template.replace("{n}", "*")):
        number = match[len(prefix):len(match) - len(suffix)]
        if number.isdigit():
            highest = max(highest, int(number))
    return Path(template.format(n=highest + 1))
