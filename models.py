MODELS = [
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "filename": "gemma4-coding-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.38GB, orig. gemma, works well, censored but can handle most text, in library, swaps",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF",
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.38GB, seems to work, good at code description, good at advice",
    },
    {
        "repo_id": "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF",
        "filename": "qwen2.5-coder-7b-instruct-q5_k_m.gguf",
        "thinking": False,
        "comment": "Q5, 5.44GB, fast coding",
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF",
        "filename": "Qwopus3.5-9B-coder-Exp-Q4_K_M.gguf",
        "thinking": True,
        "comment": "IQ4, 5.23GB, not fast, censored, claims class leader, good responses, too much thinking",
    },
    {
        "repo_id": "prithivMLmods/VibeThinker-3B-GGUF",
        "filename": "VibeThinker-3B.Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 1.93GB, small, too much thinking, may not finish",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-8B-A1B-GGUF",
        "filename": "LFM2.5-8B-A1B-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 5.16GB, fast MoE, refuses, ok answers",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-2.6B-GGUF",
        "filename": "LFM2.5-2.6B-Q5_K_M.gguf",
        "thinking": True,
        "comment": "Q5, 1.94GB",
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
        "comment": "IQ4, 5.19GB, fast, concise, good at translation, censored, in library",
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
        "thinking": False,
        "comment": "Q6, 6.6GB, general, uncensored, not boring",
    },
    {
        "repo_id": "squ11z1/Mythos-nano",
        "filename": "mythos-nano-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 1.93GB, 3B, fast, censored, in library",
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
        "comment": "Q6, 6.6GB, seems ok",
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf", #not recommended in description
        "thinking": False,
        "comment": "IQ3, 3.29GB, Pi, workhorse, fast, limited censorship, does summaries well, in library",
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q6_k.gguf",
        "thinking": False,
        "comment": "Q6, 1.46GB, Pi, concise, can stop, precise, in library",
    },
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-Q6_K_L.gguf",
        "thinking": False,
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
        "comment": "Q6, 6.6GB, abliterated",
    },
    {
        "repo_id": "MaziyarPanahi/mistral-small-3.1-24b-instruct-2503-hf-GGUF",
        "filename": "mistral-small-3.1-24b-instruct-2503-hf.Q3_K_M.gguf",
        "comment": "Q4, 11.5GB, big",
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
        "comment": "IQ4, 11.9GB, 22B, maybe too big",
    },
    {
        "repo_id": "MaziyarPanahi/phi-4-GGUF",
        "filename": "phi-4.Q5_K_M.gguf", #or Q4_K_M if too slow
        "thinking": False,
        "comment": "Q5, 14B, 10.6GB",
    },
    {
        "repo_id": "bartowski/google_gemma-4-26B-A4B-it-GGUF",
        "filename": "google_gemma-4-26B-A4B-it-IQ3_XXS.gguf",
        "comment": "IQ3, 12.2GB, might be too big",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-it-Claude-4.6-4.8-Opus-GGUF",
        "filename": "gemma4-opus48-Q6_K.gguf", #Q4_K_M if slow
        "comment": "Q6, 9.79GB",
    },
    {
        "repo_id": "MaziyarPanahi/NVIDIA-Nemotron-Nano-12B-v2-GGUF",
        "filename": "NVIDIA-Nemotron-Nano-12B-v2.Q5_K_M.gguf", #Q6_K is 10.1GB
        "thinking": True,
        "comment": "Q5, 8.76GB, slow, might be memory-constrained",
    },
    {
        "repo_id": "dominguesm/NVIDIA-Nemotron-Nano-9B-v2-GGUF",
        "filename": "nemotron-nano-9b-v2-q5_k_m.gguf", #or q4_k_s for speed
        "thinking": True,
        "comment": "Q5, 7.07GB, does not swap, not as good at code description as 12B, limited thinking",
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
        "comment": "Q6, 6.26GB, good, does not refuse but boring",
    },
    {
        "repo_id": "unsloth/gemma-4-12b-it-GGUF",
        "filename": "gemma-4-12b-it-Q6_K.gguf",
        "thinking": True,
        "comment": "Q6, 9.79GB",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-230M-GGUF",
        "filename": "LFM2.5-230M-Q8_0.gguf",
        "thinking": False,
        "comment": "Q8, 247MB, tiny, coherent, stops, overly censored",
    },
    {
        "repo_id": "jica98/qwen3.5-4B-super-coder",
        "filename": "qwen3.5-4B-super-coder.Q4_0.gguf",
        "thinking": True,
        "comment": "Q4, 2.61GB, bad at code description, fine at summaried chat",
    },
    {
        "repo_id": "DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF",
        "filename": "Qwen3.5-9B-The-Defiant-Fable-Uncnr-Heretic-NEO-MAX-IQ4_NL.gguf",
        "thinking": True,
        "comment": "IQ4, 6.62GB, seems to think too much",
    },
    {
        "repo_id": "unsloth/gemma-4-E2B-it-GGUF",
        "filename": "gemma-4-E2B-it-IQ4_NL.gguf", #check out Q6_K or Q5_K_M
        "thinking": False,
        "comment": "IQ4, 3.04GB, fast, seems ok",
    },
    {
        "repo_id": "unsloth/gemma-4-E4B-it-GGUF",
        "filename": "gemma-4-E4B-it-Q5_K_S.gguf",
        "thinking": False,
        "comment": "Q5, 5.4GB, actually, fairly good, summarizes well",
    },
    {
        "repo_id": "nguyenmanhd93/phi-4-unsloth-bnb-4bit-gguf-Q4_K_M",
        "filename": "unsloth.Q4_K_M.gguf",
        "comment": "Q4, 8.89GB",
    },
    {
        "repo_id": "mradermacher/Arsh-V1-GGUF",
        "filename": "Arsh-V1.Q4_K_M.gguf",
        "comment": "Q4, 8.89GB",
    },
    {
        "repo_id": "openbmb/MiniCPM5-2B-GGUF",
        "filename": "MiniCPM5-2B-Q4_K_M.gguf", #Only other: Q8_0 is 2.68GB
        "thinking": True,
        "comment": "Q4, 1.56GB",
    },
    {
        "repo_id": "HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF",
        "filename": "Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-IQ2_M.gguf", #IQ3_XS might fit
        "thinking": True,
        "comment": "IQ2, 10.3GB, slow",
    },
    {
        "repo_id": "empero-ai/Qwen3.8-9B-Distill-GGUF",
        "filename": "Qwen3.8-9B-Q5_K_M.gguf",
        "thinking": True,
        "comment": "Q5, 6.46GB, slow, too much thinking",
    },
    {
        "repo_id": "",
        "filename": "",
        "comment": "",
    },
]
