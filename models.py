MODELS = [
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "filename": "gemma4-coding-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.38GB, orig. gemma, works well, censored but can handle most text",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF",
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.38GB, seems to work",
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF",
        "filename": "Qwopus3.5-9B-coder-Exp-IQ4_XS.gguf",
        "thinking": True,
        "comment": "IQ4, 5.23GB, not fast, censored, claims class leader, good responses, too much thinking",
    },
    {
        "repo_id": "prithivMLmods/VibeThinker-3B-GGUF",
        "filename": "VibeThinker-3B.Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 1.93GB, doesn't finish",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-8B-A1B-GGUF",
        "filename": "LFM2.5-8B-A1B-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 5.16GB, fast MoE, refuses",
    },
    {
        "repo_id": "tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF",
        "filename": "Qwen3.6-14B-A3B-FableVibes-Q5_K_M.gguf",
        "thinking": True,
        "comment": "Q5, 9.85GB, overthinks",
    },
    {
        "repo_id": "bartowski/ibm-granite_granite-4.1-8b-GGUF",
        "filename": "ibm-granite_granite-4.1-8b-IQ4_NL.gguf",
        "thinking": False,
        "comment": "IQ4, 5.19GB, fast, concise, good at translation, censored",
    },
    {
        "repo_id": "DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF",
        "filename": "L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q4_k_s.gguf",
        "thinking": False,
        "comment": "Q4, 10.7GB, censored",
    },
    {
        "repo_id": "dphn/Dolphin3.0-Llama3.1-8B-GGUF",
        "filename": "Dolphin3.0-Llama3.1-8B-Q6_K.gguf", #smaller ones might fit Pi
        "comment": "Q6, 6.6GB, general",
    },
    {
        "repo_id": "squ11z1/Mythos-nano",
        "filename": "mythos-nano-Q4_K_M.gguf",
        "thinking": True,
        "comment": "3B, Q4, 1.93GB, fast, censored",
    },
    {
        "repo_id": "DreamFast/gemma-3-12b-it-heretic-v2",
        "filename": "gguf/gemma-3-12b-it-heretic-v2-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.3GB, for rewriting censored material, short, slow, verbose, swaps",
    },
    {
        "repo_id": "DreamFast/qwen3-8b-heretic",
        "filename": "gguf/qwen3-8b-heretic-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 5.03GB, not too much thinking, very uncensored, overly agreeable",
    },
    {
        "repo_id": "mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF",
        "filename": "meta-llama-3.1-8b-instruct-abliterated.Q6_K.gguf",
        "comment": "Q6, 6.6GB",
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf", #not recommended in description
        "thinking": False,
        "comment": "IQ3, 3.29GB, Pi, workhorse, fast, limited censorship, does summaries well",
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3-IQ4_NL.gguf",
        "thinking": False,
        "comment": "IQ4, 4.13GB, workhorse, fast, limited censorship, does summaries well",
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q6_k.gguf",
        "thinking": False,
        "comment": "Q6, Pi, 1.46GB, concise, can stop, precise",
    },
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-Q6_K_L.gguf",
        "comment": "Q6, 1.43GB, Pi",
    },
    {
        "repo_id": "janhq/Jan-v3.5-4B-gguf",
        "filename": "Jan-v3.5-4B-Q6_K.gguf", #Q4 loops
        "thinking": False,
        "comment": "Q6, 3.63GB, personality, kind of fun, fast, refuses",
    },
    {
        "repo_id": "bartowski/aya-expanse-8b-GGUF",
        "filename": "aya-expanse-8b-Q6_K_L.gguf",
        "thinking": False,
        "comment": "Q6, 6.85GB, for translation",
    },
    {
        "repo_id": "MaziyarPanahi/aya-expanse-8b-abliterated-GGUF",
        "filename": "aya-expanse-8b-abliterated.Q6_K.gguf",
        "comment": "Q6, 6.6GB, for translation, abliterated",
    },
    {
        "repo_id": "MaziyarPanahi/mistral-small-3.1-24b-instruct-2503-hf-GGUF",
        "filename": "mistral-small-3.1-24b-instruct-2503-hf.Q4_K_S.gguf", #if this swaps try Q3_K_L (12.4) or Q3_K_M (11.5)
        "comment": "Q4, 13.5GB, big",
    },
    {
        "repo_id": "MaziyarPanahi/gpt-oss-20b-Derestricted-GGUF",
        "filename": "gpt-oss-20b-Derestricted.Q3_K_M.gguf",
        "thinking": True,
        "comment": "Q3, 12.9GB, might be too big, MoE",
    },
    {
        "repo_id": "MaziyarPanahi/Qwen3-14B-GGUF",
        "filename": "Qwen3-14B.Q5_K_M.gguf", #depending on performance, check Q4_K_M or Q6_K
        "comment": "Q5, 10.5GB",
    },
    {
        "repo_id": "MaziyarPanahi/Mistral-Small-Instruct-2409-GGUF",
        "filename": "Mistral-Small-Instruct-2409.IQ4_XS.gguf",
        "comment": "22B, IQ4, 11.9GB, maybe too big",
    },
    {
        "repo_id": "MaziyarPanahi/phi-4-GGUF",
        "filename": "phi-4.Q5_K_M.gguf", #or Q4_K_M if too slow
        "comment": "14B, Q5, 10.6GB",
    },
    {
        "repo_id": "bartowski/google_gemma-4-26B-A4B-it-GGUF",
        "filename": "google_gemma-4-26B-A4B-it-IQ3_XXS.gguf",
        "comment": "IQ3, 12.2GB, might be too big",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-it-Claude-4.6-4.8-Opus-GGUF", #check out yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF
        "filename": "gemma4-opus48-Q6_K.gguf", #Q4_K_M if slow
        "comment": "Q6, 9.79GB",
    },
    {
        "repo_id": "KevinJK51/Qwen3.6-12B-IQ-Ultra-Heretic-Uncensored-Thinking-V2-Hightop-GGUF",
        "filename": "Qwen3.6-12B-IQ-Q6_K.gguf",
        "comment": "Q6, 9.59GB",
    },
    {
        "repo_id": "MaziyarPanahi/NVIDIA-Nemotron-Nano-12B-v2-GGUF",
        "filename": "NVIDIA-Nemotron-Nano-12B-v2.Q5_K_M.gguf", #Q6_K is 10.1GB
        "comment": "Q5, 8.76GB",
    },
    {
        "repo_id": "VLTX/VertaLily-1.2-1B-GGUF",
        "filename": "VertaLily-1.2-1B-Q8_0-stable.gguf",
        "thinking": False,
        "comment": "Q8, 1.25GB, can stop, follows style, good translation",
    },
    {
        "repo_id": "MaziyarPanahi/Phi-3.5-mini-instruct-GGUF",
        "filename": "Phi-3.5-mini-instruct.IQ4_XS.gguf", #or IQ3_XS
        "thinking": False,
        "comment": "IQ4, 2.06GB, try on Pi, seems to work, keeps sending lineshifts",
    },
    {
        "repo_id": "second-state/dolphin-2.6-mistral-7B-GGUF",
        "filename": "dolphin-2.6-mistral-7b-Q5_K_M.gguf", #or Q4_K_M or Q6_K
        "thinking": False,
        "comment": "Q5, 5.13GB, same as local-language-models",
    },
    {
        "repo_id": "bartowski/dolphin-2.9.3-mistral-7B-32k-GGUF",
        "filename": "dolphin-2.9.3-mistral-7B-32k-Q6_K_L.gguf", #smaller ones might fit Pi
        "thinking": False,
        "comment": "Q6, 6.26GB, good, doesn't refuse but boring",
    },
    {
        "repo_id": "bartowski/dolphin-2.8-mistral-7b-v02-GGUF",
        "filename": "dolphin-2.8-mistral-7b-v02-Q6_K.gguf", #smaller ones might fit Pi
        "thinking": False,
        "comment": "Q6, 5.94GB, older dolphin mistral, uncensored",
    },
    {
        "repo_id": "diffusionmodels1254ani/gemma-3-12b-it-heretic-v2",
        "filename": "gemma-3-12b-it-heretic-v2-Q6_K.gguf", #or Q5K_M for speed
        "comment": "Q6, 9.66GB, have same model by another user",
    },
    {
        "repo_id": "unsloth/gemma-4-12b-it-GGUF",
        "filename": "gemma-4-12b-it-Q6_K.gguf",
        "thinking": True,
        "comment": "Q6, 9.79GB",
    },
    {
        "repo_id": "",
        "filename": "",
        "comment": "",
    },
]
