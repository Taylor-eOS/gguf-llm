MODELS = [
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "filename": "gemma4-coding-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.4GB, in library, orig. gemma, works well, can handle most requests, swaps",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF",
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.4GB, seems to work, good at code description, good at advice",
    },
    {
        "repo_id": "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF",
        "filename": "qwen2.5-coder-7b-instruct-q5_k_m.gguf", #q4_k_m 4.7GB
        "thinking": False,
        "comment": "Q5, 5.4GB, fast coding, refuses",
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF",
        "filename": "Qwopus3.5-9B-coder-Exp-Q4_K_M.gguf",
        "thinking": True,
        "comment": "IQ4, 5.2GB, not fast, censored, claims class leader, good responses, too much thinking",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-230M-GGUF",
        "filename": "LFM2.5-230M-Q8_0.gguf",
        "thinking": False,
        "comment": "Q8, 247MB, tiny, coherent, stops, overly censored",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-2.6B-GGUF",
        "filename": "LFM2.5-2.6B-Q5_K_M.gguf",
        "thinking": True,
        "comment": "Q5, 1.9GB, popular, sub-4GB agentic tool-use",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-8B-A1B-GGUF",
        "filename": "LFM2.5-8B-A1B-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 5.2GB, fast MoE, refuses, ok answers",
    },
    {
        "repo_id": "bartowski/ibm-granite_granite-4.1-8b-GGUF",
        "filename": "ibm-granite_granite-4.1-8b-IQ4_NL.gguf",
        "thinking": False,
        "comment": "IQ4, 5.2GB, in library, fast, concise, good at translation, censored",
    },
    {
        "repo_id": "DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF",
        "filename": "L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q4_k_s.gguf",
        "thinking": False,
        "comment": "Q4, 10.7GB, censored, ?",
    },
    {
        "repo_id": "dphn/Dolphin3.0-Llama3.1-8B-GGUF",
        "filename": "Dolphin3.0-Llama3.1-8B-Q6_K.gguf", #smaller ones might fit Pi
        "thinking": False,
        "comment": "Q6, 6.6GB, general, uncensored, not boring, in separate script",
    },
    {
        "repo_id": "squ11z1/Mythos-nano",
        "filename": "mythos-nano-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 1.9GB, 3B, fast, censored",
    },
    {
        "repo_id": "DreamFast/gemma-3-12b-it-heretic-v2",
        "filename": "gguf/gemma-3-12b-it-heretic-v2-Q4_K_M.gguf",
        "thinking": False,
        "comment": "Q4, 7.3GB, for rewriting censored material, short, slow, verbose, swaps",
    },
    {
        "repo_id": "DreamFast/qwen3-8b-heretic",
        "filename": "qwen3-8b-heretic-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 5GB, not too much thinking, very uncensored, overly agreeable, good summaries",
    },
    {
        "repo_id": "mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF",
        "filename": "meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf", #seems to make similar responses as Q6 but that was more censored
        "thinking": False,
        "comment": "Q4, 4.9GB, clever, not overly censored",
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf", #not recommended in description
        "thinking": False,
        "comment": "IQ3, 3.3GB, in library, workhorse, fast, limited censorship, does summaries well",
    },
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-Q6_K_L.gguf", #IQ4 didn't limit output to requested words
        "thinking": False,
        "comment": "Q6, 1.4GB, in library",
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q6_k.gguf",
        "thinking": False,
        "comment": "Q6, 1.5GB, in library, concise, can stop, precise",
    },
    {
        "repo_id": "janhq/Jan-v3.5-4B-gguf",
        "filename": "Jan-v3.5-4B-Q5_K_M.gguf", #Q4 loops
        "thinking": False,
        "comment": "Q5, 3.2GB, personality, kind of fun, fast, refuses",
    },
    {
        "repo_id": "bartowski/aya-expanse-8b-GGUF",
        "filename": "aya-expanse-8b-Q6_K_L.gguf",
        "thinking": False,
        "comment": "Q6, 6.9GB, for translation",
    },
    {
        "repo_id": "MaziyarPanahi/aya-expanse-8b-abliterated-GGUF",
        "filename": "aya-expanse-8b-abliterated.Q5_K_M.gguf",
        "comment": "Q5, 5.8GB, abliterated",
    },
    {
        "repo_id": "MaziyarPanahi/mistral-small-3.1-24b-instruct-2503-hf-GGUF",
        "filename": "mistral-small-3.1-24b-instruct-2503-hf.Q3_K_M.gguf",
        "comment": "Q3, 11.5GB, big",
    },
    {
        "repo_id": "MaziyarPanahi/gpt-oss-20b-Derestricted-GGUF",
        "filename": "gpt-oss-20b-Derestricted.Q3_K_M.gguf",
        "thinking": True,
        "comment": "Q3, 12.9GB, maybe too big, MoE",
    },
    {
        "repo_id": "MaziyarPanahi/Mistral-Small-Instruct-2409-GGUF",
        "filename": "Mistral-Small-Instruct-2409.IQ4_XS.gguf",
        "comment": "IQ4, 11.9GB, 22B, maybe too big",
    },
    {
        "repo_id": "MaziyarPanahi/phi-4-GGUF",
        "filename": "phi-4.Q5_K_M.gguf", #or Q4_K_M 9GB if Q5 too slow
        "thinking": False,
        "comment": "Q5, 10.6GB, 14B, censored, slow, a tad boring",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-it-Claude-4.6-4.8-Opus-GGUF",
        "filename": "gemma4-opus48-Q4_K_M.gguf", #Q6_K 9.8GB
        "comment": "Q4, 7.4GB",
    },
    {
        "repo_id": "nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF",
        "filename": "NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf", #only one
        "comment": "Q4, 2.8GB",
    },
    {
        "repo_id": "MaziyarPanahi/NVIDIA-Nemotron-Nano-12B-v2-GGUF",
        "filename": "NVIDIA-Nemotron-Nano-12B-v2.Q2_K.gguf", #Q3_K_M 6GB, Q5_K_M 8.8GB, Q6_K 10.1GB
        "thinking": True,
        "comment": "Q2, 4.7GB, low quant seems coherent, does overthink on a difficult request",
    },
    {
        "repo_id": "dominguesm/NVIDIA-Nemotron-Nano-9B-v2-GGUF",
        "filename": "nemotron-nano-9b-v2-q2_k.gguf",
        "thinking": True,
        "comment": "Q2, 5GB, smaller quant of the below",
    },
    {
        "repo_id": "dominguesm/NVIDIA-Nemotron-Nano-9B-v2-GGUF",
        "filename": "nemotron-nano-9b-v2-q5_k_m.gguf", #better q4_k_s 6.2GB
        "thinking": True,
        "comment": "Q5, 7.1GB, no swap, worse code desc. than 12B, limited thinking, good summary, not fast",
    },
    {
        "repo_id": "VLTX/VertaLily-1.2-1B-GGUF",
        "filename": "VertaLily-1.2-1B-Q8_0-stable.gguf",
        "thinking": False,
        "comment": "Q8, 1.3GB, can stop, follows style, good translation",
    },
    {
        "repo_id": "VLTX/VertaLily-1.2-1B-GGUF",
        "filename": "VertaLily-1.2-1B-Q4_K_M-stable.gguf",
        "thinking": False,
        "comment": "Q4, 731MB, low quant of the above, insanely fast, censored, kind of wrong",
    },
    {
        "repo_id": "MaziyarPanahi/Phi-3.5-mini-instruct-GGUF",
        "filename": "Phi-3.5-mini-instruct.IQ4_XS.gguf", #or IQ3_XS
        "thinking": False,
        "comment": "IQ4, 2GB, seems to work, censored, keeps sending lineshifts",
    },
    {
        "repo_id": "second-state/dolphin-2.6-mistral-7B-GGUF",
        "filename": "dolphin-2.6-mistral-7b-Q5_K_M.gguf", #or Q4_K_M or Q6_K
        "thinking": False,
        "comment": "Q5, 5.1GB, in local-language-models",
    },
    {
        "repo_id": "bartowski/dolphin-2.9.3-mistral-7B-32k-GGUF",
        "filename": "dolphin-2.9.3-mistral-7B-32k-Q6_K_L.gguf", #smaller ones might fit Pi
        "thinking": False,
        "comment": "Q6, 6.3GB, good, does not refuse but boring",
    },
    {
        "repo_id": "unsloth/gemma-4-12b-it-GGUF",
        "filename": "gemma-4-12b-it-IQ4_XS.gguf", #Q6_K 9.8GB
        "thinking": True,
        "comment": "IQ4, 6.4GB",
    },
    {
        "repo_id": "jica98/qwen3.5-4B-super-coder",
        "filename": "qwen3.5-4B-super-coder.Q4_0.gguf",
        "thinking": True,
        "comment": "Q4, 2.6GB, bad at code description, fine at summaried chat",
    },
    {
        "repo_id": "DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF",
        "filename": "Qwen3.5-9B-The-Defiant-Fable-Uncnr-Heretic-NEO-MAX-IQ4_NL.gguf",
        "thinking": True,
        "comment": "IQ4, 6.6GB, seems to think too much",
    },
    {
        "repo_id": "unsloth/gemma-4-E2B-it-GGUF",
        "filename": "gemma-4-E2B-it-IQ4_NL.gguf", #check out Q6_K or Q5_K_M
        "thinking": False,
        "comment": "IQ4, 3GB, in library, fast, seems ok",
    },
    {
        "repo_id": "unsloth/gemma-4-E4B-it-GGUF",
        "filename": "gemma-4-E4B-it-Q5_K_S.gguf",
        "thinking": False,
        "comment": "Q5, 5.4GB, in library, fairly good, summarizes well",
    },
    {
        "repo_id": "nguyenmanhd93/phi-4-unsloth-bnb-4bit-gguf-Q4_K_M", #this is very obscure, maybe try the original unsloth/phi-4-unsloth-bnb-4bit
        "filename": "unsloth.Q4_K_M.gguf",
        "comment": "Q4, 8.9GB",
    },
    {
        "repo_id": "mradermacher/Arsh-V1-GGUF",
        "filename": "Arsh-V1.Q4_K_M.gguf",
        "comment": "Q4, 8.9GB",
    },
    {
        "repo_id": "openbmb/MiniCPM5-2B-GGUF",
        "filename": "MiniCPM5-2B-Q4_K_M.gguf", #Only other: Q8_0 is 2.7GB
        "thinking": True,
        "comment": "Q4, 1.6GB, seems coherent, not too much thinking",
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
        "comment": "Q5, 6.5GB, slow, too much thinking",
    },
    {
        "repo_id": "ornith-ai/Ornith-1.5-9B-GGUF",
        "filename": "Ornith-1.5-9B-Q5_K_M.gguf",
        "thinking": True,
        "comment": "Q5, 6.7GB, popular, not too much thinking, refusals, can't skip thinking",
    },
    {
        "repo_id": "MaziyarPanahi/Nemotron-Orchestrator-8B-GGUF",
        "filename": "Nemotron-Orchestrator-8B.Q5_K_M.gguf",
        "thinking": True,
        "comment": "Q5, 5.9GB, can skip thinking, fast",
    },
    {
        "repo_id": "bartowski/allura-forge_Llama-3.3-8B-Instruct-GGUF",
        #"filename": "allura-forge_Llama-3.3-8B-Instruct-Q5_K_M.gguf",
        "filename": "allura-forge_Llama-3.3-8B-Instruct-IQ4_NL.gguf",
        "thinking": False,
        #"comment": "Q5, 5.7GB, seems to work",
        "comment": "IQ4, 4.7GB, seems to work",
    },
    {
        "repo_id": "bartowski/gemma-2-9b-it-GGUF",
        "filename": "gemma-2-9b-it-IQ4_XS.gguf",
        "thinking": False,
        "comment": "IQ4, 5.2GB",
    },
    {
        "repo_id": "bartowski/Hermes-3-Llama-3.2-3B-GGUF",
        "filename": "Hermes-3-Llama-3.2-3B-IQ4_XS.gguf",
        "thinking": False,
        "comment": "IQ4, 1.8GB",
    },
    {
        "repo_id": "mradermacher/Ornith-1.5-9B-uncensored-GGUF",
        "filename": "Ornith-1.5-9B-uncensored.IQ4_XS.gguf",
        "thinking": True,
        "comment": "IQ4, 5.2GB, can't skip thinking, censored, gets done, fine summaries",
    },
    {
        "repo_id": "dealignai/Ornith-1.5-9B-UNCENSORED-GGUF",
        "filename": "Ornith-1.5-9B-CRACK-Q2_K.gguf", #several other ones exist and an IQ4
        "thinking": True,
        "comment": "Q2, 3.8GB, tiny quant test, appropriate thinking",
    },
    {
        "repo_id": "empero-ai/Qwen3.8-4B-Distill-GGUF",
        "filename": "Qwen3.8-4B-Q5_K_M.gguf",
        "thinking": True,
        "comment": "Q5, 3.2GB, popular, small, seems ok, not very fast, not too much thinking",
    },
    {
        "repo_id": "OBLITERATUS/Ornith-1.5-9B-OBLITERATED",
        "filename": "Ornith-1.5-9B-OBLITERATED-IQ4_XS.gguf",
        "comment": "IQ4, 5.4GB",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF",
        "filename": "gemma4-v2-Q4_K_M.gguf", #Q3 exists
        "comment": "Q4, 7.4GB",
    },
    {
        "repo_id": "AnkitAI/Parable-Qwen3-8B-Claude-Fable-5-GGUF",
        "filename": "Parable-Qwen3-8B-Claude-Fable-5-GGUF-Q4_K_M.gguf",
        "comment": "Q4, 5GB",
    },
    {
        "repo_id": "Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF",
        "filename": "Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M.gguf",
        "thinking": True,
        "comment": "Q4, 5.6GB, too much thinking",
    },
    {
        "repo_id": "MaziyarPanahi/DeepSeek-R1-0528-Qwen3-8B-GGUF",
        "filename": "DeepSeek-R1-0528-Qwen3-8B.Q2_K.gguf", #Q3_K_L, Q4_K_M
        "thinking": True,
        "comment": "Q2, 3.3GB",
    },
    {
        "repo_id": "CMSManhattan/JiRackUltra_14b",
        "filename": "JiRackUltra_14b_Q3_K_M.gguf", #Q4_K_M (9GB)
        "thinking": True,
        "comment": "Q3, 7.3GB, for CPU, limited thinking",
    },
    {
        "repo_id": "bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF",
        #"filename": "DeepSeek-Coder-V2-Lite-Instruct-IQ3_M.gguf",
        #"comment": "IQ3, 7.6GB",
        "filename": "DeepSeek-Coder-V2-Lite-Instruct-IQ2_XS.gguf",
        "comment": "IQ2, 5.8GB, smallest quant",
    },
    {
        "repo_id": "",
        "filename": "",
        "comment": "",
    },
]
