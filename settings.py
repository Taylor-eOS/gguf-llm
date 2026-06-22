N_CTX = 4 * 1024
N_THREADS = 6
STYLE_INSTRUCTION = "[Omit lineshifts and formatting. Write continuously.]"
SEGMENT_MODE = True
MAX_TOKENS = 2 * 1024
PRINT_PROCESSING_PROMPT = False
BASE = 'Role: You are a sequential text processing tool, run from a script. Output only the requested text itself. Do not add any other explanations or comments.'
#REQUEST = 'Condense this book segment into a clear and simple encapsulation. Present the central causal mechanism while omitting less important details. In other words compress a summary of the main point. Infer the underlying meaning instead of repeating the text verbatim. Write for a reader that gets an entire book of similar segments summarized, wanting to extract the gist of each segment. Assume the context is known and does not have to be repeated. Do not sanitize contrarian aspects. Apply the same narrative voice as the original content. Omit introductory phrases like “the takeaway is”.'
REQUEST = 'Write this segment into slightly less difficult language, while preserving exactly the same meaning, nuance, tone, emphasis, implications, qualifications, and level of detail. Make the fewest changes necessary. Leave sentences unchanged unless they contain wording that is unusually complex, formal, or cumbersome for an adult general reader. Replace difficult words only when a more common alternative expresses the same meaning with equal precision. You may split sentences that are overloaded with multiple distinct ideas, but do not reorganize, condense, summarize, or remove information. Do not make the writing simpler than necessary. The goal is only to smooth excessive complexity, not to alter the authors style or reduce nuance. When a choice is uncertain, preserve the original wording. Never use em dashes or snaily parenthetical insertions.',

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
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF",
        "filename": "Qwopus3.5-9B-coder-Exp-Q4_K_M.gguf",
        "thinking": True,
        "comment": "not fast, no swap",
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
        "thinking": True,
        "comment": "overthinks",
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
        "comment": "for rewriting censored material, short, slow, verbose, swaps",
    },
    {
        "repo_id": "DreamFast/qwen3-8b-heretic",
        "filename": "gguf/qwen3-8b-heretic-Q4_K_M.gguf",
        "thinking": True,
        "comment": "not too much thinking, very uncensored",
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
        "comment": "workhorse, 3.29GB, fast, limited censorship, does summaries well",
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q4_k_m.gguf",
        "thinking": False,
        "comment": "for Pi, 1.12GB, concise, can stop, precise",
    },
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-IQ4_XS.gguf", #there are bigger Q ones
        "comment": "for Pi, 940MB",
    },
    {
        "repo_id": "janhq/Jan-v3.5-4B-gguf",
        "filename": "Jan-v3.5-4B-Q5_K_M.gguf", #Q4 loops
        "thinking": True,
        "comment": "personality, kind of fun, 2.72GB, fast, refuses",
    },
    {
        "repo_id": "bartowski/aya-expanse-8b-GGUF",
        "filename": "aya-expanse-8b-IQ4_XS.gguf",
        "thinking": False,
        "comment": "for translation",
    },
    {
        "repo_id": "MaziyarPanahi/aya-expanse-8b-abliterated-GGUF",
        "filename": "aya-expanse-8b-abliterated.Q5_K_M.gguf",
        "comment": "for translation, abliterated",
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
        "comment": "thinks too much, fast enough, fails at translation, swaps but not slow, thinking loops",
    },
    {
        "repo_id": "bartowski/nbeerbower_Gemma4-Gutenberg-31B-Heretic-GGUF",
        "filename": "nbeerbower_Gemma4-Gutenberg-31B-Heretic-IQ2_S.gguf", #M swaps heavily, could try XS
        "comment": "31B, creative writing not logic, limited cache, keep short, swaps",
    },
    {
        "repo_id": "bartowski/google_gemma-4-26B-A4B-it-GGUF",
        "filename": "google_gemma-4-26B-A4B-it-IQ3_XS.gguf", #or try M
        "comment": "12.4GB, big",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-it-Claude-4.6-4.8-Opus-GGUF",
        "filename": "gemma4-opus48-Q6_K.gguf", #or try Q4_K_M
        "comment": "",
    },
    {
        "repo_id": "KevinJK51/Qwen3.6-12B-IQ-Ultra-Heretic-Uncensored-Thinking-V2-Hightop-GGUF",
        "filename": "Qwen3.6-12B-IQ-Q5_K_M.gguf", #or try IQ-Q5_K_M, there are a lot more sizes
        "comment": "",
    },
    {
        "repo_id": "MaziyarPanahi/NVIDIA-Nemotron-Nano-12B-v2-GGUF",
        "filename": "NVIDIA-Nemotron-Nano-12B-v2.Q5_K_M.gguf", #also bigger Q6_K or smaller Q6_K
        "comment": "",
    },
    {
        "repo_id": "VLTX/VertaLily-1.2-1B-GGUF",
        "filename": "VertaLily-1.2-1B-Q8_0-stable.gguf",
        "thinking": False,
        "comment": "1.25GB, can stop, follows style, good translation",
    },
    {
        "repo_id": "MaziyarPanahi/Phi-3.5-mini-instruct-GGUF",
        "filename": "Phi-3.5-mini-instruct.IQ4_XS.gguf", #or IQ3_XS
        "thinking": False,
        "comment": "try on Pi, 2GB, seems to work, keeps going",
    },
    {
        "repo_id": "second-state/dolphin-2.6-mistral-7B-GGUF",
        "filename": "dolphin-2.6-mistral-7b-Q5_K_M.gguf", #or Q4_K_M or Q6_K
        "thinking": False,
        "comment": "same as local-language-models",
    },
    {
        "repo_id": "bartowski/dolphin-2.9.3-mistral-7B-32k-GGUF",
        "filename": "dolphin-2.9.3-mistral-7B-32k-Q6_K_L.gguf", #smaller ones might fit Pi
        "thinking": False,
        "comment": "good, doesn't refuse but boring",
    },
    {
        "repo_id": "bartowski/dolphin-2.8-mistral-7b-v02-GGUF",
        "filename": "dolphin-2.8-mistral-7b-v02-IQ4_XS.gguf", #smaller ones might fit Pi
        "thinking": False,
        "comment": "older dolphin mistral, uncensored",
    },
    {
        "repo_id": "diffusionmodels1254ani/gemma-3-12b-it-heretic-v2",
        "filename": "gguf/gemma-3-12b-it-heretic-v2-Q5_K_M.gguf", #or Q4
        "comment": "have same model by another user",
    },
    {
        "repo_id": "",
        "filename": "",
        "comment": "",
    },
]
