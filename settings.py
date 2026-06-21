k = 1024
N_CTX = 4 * k
N_THREADS = 6
STYLE_INSTRUCTION = ""
SEGMENT_MODE = True
MAX_TOKENS = 2 * k
PRINT = True
BASE = 'Role: You are a sequential text processing tool. Output only the requested text itself, do not add any other explanations or comments.'
REQUEST = 'Condense this book segment into a short, clear, simple, readable encapsulation. Present the central causal mechanism rather than including every detail. Just present a summary of the main point briefly. Keep it short. Assume the context is known and does not have to be repeated. Try to interpret it instead of repeating it verbatim. Do not sanitize contrarian aspects. Do not use any introductory phrases like “it was about”.'
MODELS = [
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "filename": "gemma4-coding-Q4_K_M.gguf",
        "thinking": False,
        "comment": "orig. gemma, works well, censored",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF",
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf",
        "thinking": False,
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "filename": "gemma4-coding-Q4_K_M.gguf",
        "thinking": False,
        "comment": "good, censored",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF",
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf",
        "thinking": False,
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF",
        "filename": "Qwopus3.5-9B-coder-Exp-Q4_K_M.gguf",
        "thinking": True,
    },
    {
        "repo_id": "prithivMLmods/VibeThinker-3B-GGUF",
        "filename": "VibeThinker-3B.Q4_K_M.gguf",
        "thinking": True,
        "comment": "doesn't finish",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-8B-A1B-GGUF",
        "filename": "LFM2.5-8B-A1B-Q4_K_M.gguf",
        "thinking": True,
        "comment": "fast MoE, refuses",
    },
    {
        "repo_id": "tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF",
        "filename": "Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/ibm-granite_granite-4.1-8b-GGUF",
        "filename": "ibm-granite_granite-4.1-8b-Q4_K_M.gguf",
        "thinking": False,
        "comment": "fast, concise, good at translation, censored",
    },
    {
        "repo_id": "DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF",
        "filename": "L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q4_k_s.gguf",
        "thinking": False,
        "comment": "censored",
    },
    {
        "repo_id": "dphn/Dolphin3.0-Llama3.1-8B-GGUF",
        "filename": "Dolphin3.0-Llama3.1-8B-Q4_K_M.gguf",
        "comment": "general",
    },
    {
        "repo_id": "squ11z1/Mythos-nano",
        "filename": "mythos-nano-Q4_K_M.gguf",
        "thinking": True,
        "comment": "fast, censored",
    },
    {
        "repo_id": "DreamFast/gemma-3-12b-it-heretic-v2",
        "filename": "gguf/gemma-3-12b-it-heretic-v2-Q4_K_M.gguf",
        "thinking": False,
        "comment": "for rewriting censored material, short, slow, verbose",
    },
    {
        "repo_id": "DreamFast/qwen3-8b-heretic",
        "filename": "gguf/qwen3-8b-heretic-Q4_K_M.gguf",
    },
    {
        "repo_id": "mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF",
        "filename": "meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf",
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf",
        #"filename": "Mistral-7B-Instruct-v0.3-IQ4_NL.gguf",
        "thinking": False,
        "comment": "workhorse, 3.29GB, fast, limited censorship",
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q4_k_m.gguf",
        "comment": "for Pi, 1.12GB, concise, can stop, precise",
    },
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-IQ4_XS.gguf",
        "comment": "for Pi, 940MB",
    },
    #{
    #    "repo_id": "Andycurrent/Gemma-3-1B-it-GLM-4.7-Flash-Heretic-Uncensored-Thinking_GGUF",
    #    "filename": "Gemma-3-1B-it-GLM-4.7-Flash-Heretic-Uncensored-Thinking_Q4_k_m.gguf",
    #    "thinking": True,
    #    "comment": "806MB, very fast, repeats, thinks, can't stop",
    #},
    {
        "repo_id": "janhq/Jan-v3.5-4B-gguf",
        "filename": "Jan-v3.5-4B-Q4_K_M.gguf",
        "thinking": False,
        "comment": "personality, kind of fun, 2.72GB, fast, refuses",
    },
    {
        "repo_id": "bartowski/aya-expanse-8b-GGUF",
        "filename": "aya-expanse-8b-IQ4_XS.gguf",
        "comment": "for translation",
    },
    {
        "repo_id": "MaziyarPanahi/aya-expanse-8b-abliterated-GGUF",
        "filename": "aya-expanse-8b-abliterated.Q5_K_M.gguf",
        "comment": "for translation, abliterated, Q5",
    },
    {
        "repo_id": "MaziyarPanahi/mistral-small-3.1-24b-instruct-2503-hf-GGUF",
        "filename": "mistral-small-3.1-24b-instruct-2503-hf.Q4_K_S.gguf",
        "comment": "big, slow",
    },
    {
        "repo_id": "MaziyarPanahi/gpt-oss-20b-Derestricted-GGUF",
        "filename": "gpt-oss-20b-Derestricted.Q4_K_M.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/Qwen3-14B-GGUF",
        "filename": "Qwen3-14B.Q4_K_M.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/Mistral-Small-Instruct-2409-GGUF",
        "filename": "Mistral-Small-Instruct-2409.IQ4_XS.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/phi-4-GGUF",
        "filename": "phi-4.Q4_K_M.gguf",
    },
    {
        "repo_id": "unsloth/GLM-4.7-Flash-REAP-23B-A3B-GGUF",
        "filename": "GLM-4.7-Flash-REAP-23B-A3B-IQ4_NL.gguf",
        "thinking": True,
        "comment": "fast enough, thinks too much, fails at translation",
    },
    {
        "repo_id": "TheBloke/em_german_mistral_v01-GGUF",
        "filename": "em_german_mistral_v01.Q4_K_M.gguf",
    }
]
