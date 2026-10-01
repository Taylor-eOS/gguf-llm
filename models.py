MODELS = [
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "thinking": False,
        "filename": "gemma4-coding-Q4_K_M.gguf", #seems right
        "comment": "Q4, 7.4GB, in library, works well, does most requests, short answers, swaps but ok",
        #"filename": "gemma4-coding-Q3_K_M.gguf", #for speed, not in library
        #"comment": "Q4, 6.1GB, works well, does most requests",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF",
        "thinking": False,
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf", #only one
        "comment": "Q4, 7.4GB, seems to work, good code description, good advice, few DL, not fast, history",
    },
    {
        "repo_id": "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF",
        "thinking": False,
        #"filename": "qwen2.5-coder-7b-instruct-q5_k_m.gguf", #Q5 might be worth it
        #"comment": "Q5, 5.4GB, useful, short responses, old, funny, history, unoriginal, refusal",
        "filename": "qwen2.5-coder-7b-instruct-q4_k_m.gguf",
        "comment": "Q4, 4.7GB, useful, short responses, old, funny, history, unoriginal, refusal",
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF",
        "thinking": True,
        "filename": "Qwopus3.5-9B-coder-Exp-Q4_K_M.gguf",
        "comment": "Q4, 5.2GB, class leader, good responses, too much thinking, few dl",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-8B-A1B-GGUF",
        "thinking": True,
        "filename": "LFM2.5-8B-A1B-Q4_K_M.gguf",
        "comment": "Q4, 5.2GB, MoE, ok answers",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-2.6B-GGUF",
        "thinking": True,
        "filename": "LFM2.5-2.6B-Q5_K_M.gguf",
        "comment": "Q5, 1.9GB, popular, sub-4GB agentic tool-use, small, finishes thinking, nonsense summary",
    },
    #{
    #    "repo_id": "LiquidAI/LFM2.5-230M-GGUF",
    #    "thinking": False,
    #    "filename": "LFM2.5-230M-Q8_0.gguf",
    #    "comment": "Q8, 247MB, too small, stops, refuses most, incoherent",
    #},
    {
        "repo_id": "bartowski/ibm-granite_granite-4.1-8b-GGUF",
        "thinking": False,
        #"filename": "ibm-granite_granite-4.1-8b-IQ4_NL.gguf",
        #"comment": "IQ4, 5.2GB, concise, good translation",
        "filename": "ibm-granite_granite-4.1-8b-Q4_K_M.gguf",
        "comment": "Q4, 5.5GB, in library, concise, good translation",
    },
    {
        "repo_id": "DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF",
        "thinking": False,
        "filename": "L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q4_k_s.gguf",
        "comment": "Q4, 10.7GB, big, ?",
    },
    {
        "repo_id": "squ11z1/Mythos-nano",
        "thinking": True,
        "filename": "mythos-nano-Q4_K_M.gguf",
        "comment": "Q4, 1.9GB, 3B, small",
    },
    {
        "repo_id": "DreamFast/gemma-3-12b-it-heretic-v2",
        "thinking": False,
        "filename": "gguf/gemma-3-12b-it-heretic-v2-Q4_K_M.gguf",
        "comment": "Q4, 7.3GB, didn't refuse, slow, verbose, swaps, interesting",
    },
    {
        "repo_id": "DreamFast/qwen3-8b-heretic",
        "thinking": True,
        "filename": "gguf/qwen3-8b-heretic-Q4_K_M.gguf",
        "comment": "Q4, 5GB, very agreeable, ok thinking, good summaries, brief, old",
    },
    {
        "repo_id": "mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF",
        "thinking": False,
        "filename": "meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf", #seems to make similar responses as Q6 but that was more censored
        "comment": "Q4, 4.9GB, clever, not overly censored",
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "thinking": False,
        #"filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf", #not recommended in descr
        #"comment": "IQ3, 3.3GB, workhorse, limited censorship, good summaries",
        "filename": "Mistral-7B-Instruct-v0.3-Q3_K_S.gguf",
        "comment": "Q3, 3.8GB, in library, workhorse, limited censorship",
    },
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "thinking": False,
        "filename": "SmolLM2-1.7B-Instruct-Q6_K_L.gguf",
        "comment": "Q6, 1.4GB, in library, small, good, didn't refuse, limited creativity",
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q6_k.gguf",
        "comment": "Q6, 1.5GB, in library, too small, concise, can stop, refuses joke, old",
        "thinking": False,
    },
    {
        "repo_id": "janhq/Jan-v3.5-4B-gguf",
        "thinking": False,
        "filename": "Jan-v3.5-4B-Q5_K_M.gguf", #Q4 loops
        "comment": "Q5, 3.2GB, personality, kind of fun",
    },
    {
        "repo_id": "bartowski/aya-expanse-8b-GGUF",
        "thinking": False,
        #"filename": "aya-expanse-8b-Q6_K_L.gguf",
        #"comment": "Q6, 6.9GB, translation, brief, didn't refuse, avoidant, useful",
        "filename": "aya-expanse-8b-Q5_K_M.gguf",
        "comment": "Q5, 5.8GB, translation, brief, didn't refuse, avoidant, useful",
    },
    {
        "repo_id": "mradermacher/aya-expanse-8b-abliterated-i1-GGUF",
        "thinking": False,
        #"filename": "aya-expanse-8b-abliterated.i1-IQ4_XS.gguf",
        #"comment": "IQ4, 4.6GB",
        "filename": "aya-expanse-8b-abliterated.i1-Q4_K_M.gguf",
        "comment": "Q4, 5.1GB, some French, not slow, useful, long context, unoriginal",
    },
    {
        "repo_id": "MaziyarPanahi/mistral-small-3.1-24b-instruct-2503-hf-GGUF",
        "thinking": False,
        "filename": "mistral-small-3.1-24b-instruct-2503-hf.Q3_K_M.gguf",
        "comment": "Q3, 11.5GB, big, works, not fast, gets authors right, sanitized",
    },
    {
        "repo_id": "unsloth/gpt-oss-20b-GGUF",
        "thinking": True,
        "filename": "gpt-oss-20b-UD-Q4_K_XL.gguf", #only UD that fits
        "comment": "UD-Q4, 11.9GB, big, popular, fast, tags, limited thinking, refuses dirty joke, loops", #promising
    },
    {
        "repo_id": "MaziyarPanahi/gpt-oss-20b-Derestricted-GGUF",
        "thinking": True,
        "filename": "gpt-oss-20b-Derestricted.Q3_K_M.gguf",
        "comment": "Q3, 12.9GB, big, MoE",
    },
    {
        "repo_id": "MaziyarPanahi/phi-4-GGUF",
        "thinking": False,
        #"filename": "phi-4.Q5_K_M.gguf",
        #"comment": "Q5, 10.6GB, 14B, big, a tad boring, swaps, slow but useful, didn't refuse all",
        "filename": "phi-4.Q4_K_M.gguf", #several others
        "comment": "Q4, 9GB, 14B, a tad boring, didn't refuse all",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-it-Claude-4.6-4.8-Opus-GGUF",
        "thinking": True,
        "filename": "gemma4-opus48-Q4_K_M.gguf", #other ones are Q2_K 4.8GB and Q6_K 9.8GB
        "comment": "Q4, 7.4GB",
    },
    {
        "repo_id": "MaziyarPanahi/NVIDIA-Nemotron-Nano-12B-v2-GGUF",
        "thinking": True,
        "filename": "NVIDIA-Nemotron-Nano-12B-v2.Q2_K.gguf", #Q4_K_M 7.5GB, Q5_K_M 8.8GB
        "comment": "Q2, 4.7GB, low-q test, seems coherent, didn't refuse, overthinks, may skip thinking", #small low-q test
        #"filename": "NVIDIA-Nemotron-Nano-12B-v2.Q3_K_L.gguf", #better, Q3_K_M 6GB
        #"comment": "Q3, 6.4GB, didn't refuse",
    },
    {
        "repo_id": "dominguesm/NVIDIA-Nemotron-Nano-9B-v2-GGUF",
        "thinking": True,
        #"filename": "nemotron-nano-9b-v2-q2_k.gguf", #q5_k_m 7.1GB
        #"comment": "Q2, 5GB, worse code descr than 12B, good summary, ok thinking, no swap, didn't refuse",
        "filename": "nemotron-nano-9b-v2-q4_k_s.gguf", #better
        "comment": "Q4, 6.2GB, good summary, ok thinking, didn't refuse",
    },
    {
        "repo_id": "nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF",
        "thinking": True,
        "filename": "NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf", #only one
        "comment": "Q4, 2.8GB, small, ok thinking, works, restricted",
    },
    {
        "repo_id": "VLTX/VertaLily-1.2-1B-GGUF",
        "thinking": False,
        "filename": "VertaLily-1.2-1B-Q8_0-stable.gguf", #Q4 is overly censored and kind of wrong, no others
        "comment": "Q8, 1.3GB, small, can stop, follows style, good translation",
    },
    {
        "repo_id": "MaziyarPanahi/Phi-3.5-mini-instruct-GGUF",
        "thinking": False,
        #"filename": "Phi-3.5-mini-instruct.IQ4_XS.gguf",
        #"comment": "IQ4, 2GB, 3.8B, small, seems to work, uneven censorship, lineshift spam",
        "filename": "Phi-3.5-mini-instruct.Q4_K_M.gguf",
        "comment": "Q4, 2.4GB, 3.8B, small, seems to work, uneven censorship",
    },
    {
        "repo_id": "dphn/Dolphin3.0-Llama3.1-8B-GGUF",
        "thinking": False,
        #"filename": "Dolphin3.0-Llama3.1-8B-Q6_K.gguf", #small ones might fit Pi
        #"comment": "Q6, 6.6GB, in separate script, uncensored, not boring",
        "filename": "Dolphin3.0-Llama3.1-8B-Q4_K_M.gguf",
        "comment": "Q4, 4.9GB, in separate script, uncensored, not boring",
    },
    {
        "repo_id": "second-state/dolphin-2.6-mistral-7B-GGUF",
        "thinking": False,
        "filename": "dolphin-2.6-mistral-7b-Q5_K_M.gguf", #or Q4_K_M or Q6_K
        "comment": "Q5, 5.1GB, in local",
    },
    {
        "repo_id": "bartowski/dolphin-2.9.3-mistral-7B-32k-GGUF",
        "thinking": False,
        #"filename": "dolphin-2.9.3-mistral-7B-32k-IQ4_XS.gguf", #Q6 6.3GB was good
        #"comment": "IQ4, 3.9GB, doesn't refuse, boring",
        "filename": "dolphin-2.9.3-mistral-7B-32k-Q4_K_L.gguf", #Q5_K_L 5.5GB
        "comment": "Q4, 4.7GB, doesn't refuse, boring",
    },
    {
        "repo_id": "unsloth/gemma-4-12b-it-GGUF",
        "thinking": True,
        "filename": "gemma-4-12b-it-Q4_K_M.gguf",
        "comment": "Q4, 7.1GB",
    },
    {
        "repo_id": "jica98/qwen3.5-4B-super-coder",
        "thinking": True,
        "filename": "qwen3.5-4B-super-coder.Q4_0.gguf",
        "comment": "Q4, 2.6GB, small, bad code description, fine summaried chat",
    },
    {
        "repo_id": "DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF",
        "thinking": True,
        #"filename": "Qwen3.5-9B-The-Defiant-Fable-Uncnr-Heretic-NEO-MAX-IQ4_NL.gguf",
        #"comment": "IQ4, 6.6GB, thinks too much",
        "filename": "Qwen3.5-9B-The-Defiant-Fable-Uncnr-Heretic-NEO-MAX-MTP-Q4_K_M.gguf",
        "comment": "Q4, 7GB, thinks too much",
    },
    {
        "repo_id": "unsloth/gemma-4-E2B-it-GGUF",
        "thinking": False,
        #"filename": "gemma-4-E2B-it-IQ4_NL.gguf",
        #"comment": "IQ4, 3GB, small, good workhorse",
        "filename": "gemma-4-E2B-it-UD-Q4_K_XL.gguf",
        "comment": "UD-Q4, 3.2GB, small, in library, good workhorse",
    },
    {
        "repo_id": "unsloth/gemma-4-E4B-it-GGUF",
        "thinking": False,
        #"filename": "gemma-4-E4B-it-IQ4_NL.gguf", #UD-IQ3_XXS 3.7GB
        #"comment": "IQ4, 4.8GB, good workhorse, summarizes well",
        "filename": "gemma-4-E4B-it-UD-Q4_K_XL.gguf",
        "comment": "UD-Q4, 5.1GB, in library, good workhorse",
    },
    {
        "repo_id": "shafire/Zero-Gemma4-E4B-OpenZero-GGUF",
        "thinking": False,
        "filename": "Zero-Gemma4-E4B-OpenZero-Q5_K_M-F16-Merged.gguf", #only one
        "comment": "Q5, 5.9GB, few dl, image-text model, works, loops",
    },
    {
        "repo_id": "HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive",
        "thinking": False,
        "filename": "Gemma-4-E4B-Uncensored-HauhauCS-Aggressive-Q4_K_M.gguf", #Q3_K_P 4.9GB, Q4_K_P 5.4GB, Q5_K_P 5.8GB (P = perfect)
        "comment": "Q4, 5.3GB, popular, fast, hilarious, sarcastic, wrong details, can program",
    },
    {
        "repo_id": "RusteddDDD/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive",
        "thinking": False,
        "filename": "Gemma-4-E4B-Uncensored-HauhauCS-Aggressive-Q5_K_P.gguf", #has same quants as above
        "comment": "Q5, 5.8GB, the above",
    },
    {
        "repo_id": "llmfan46/gemma-4-E4B-it-ultra-uncensored-heretic-GGUF",
        #"thinking": False,
        "filename": "gemma-4-E4B-it-ultra-uncensored-heretic-Q4_K_M.gguf", #smallest one
        "comment": "Q4, 5.3GB",
    },
    {
        "repo_id": "nguyenmanhd93/phi-4-unsloth-bnb-4bit-gguf-Q4_K_M",
        #"thinking": False,
        "filename": "unsloth.Q4_K_M.gguf",
        "comment": "Q4, 8.9GB, big-ish, very few DL",
    },
    {
        "repo_id": "mradermacher/Arsh-V1-GGUF",
        #"thinking": False,
        "filename": "Arsh-V1.Q4_K_M.gguf",
        "comment": "Q4, 8.9GB, big-ish",
    },
    {
        "repo_id": "openbmb/MiniCPM5-2B-GGUF",
        "thinking": True,
        "filename": "MiniCPM5-2B-Q4_K_M.gguf", #Only other: Q8_0 is 2.7GB
        "comment": "Q4, 1.6GB, small, seems coherent, ok thinking",
    },
    {
        "repo_id": "empero-ai/Qwen3.8-9B-Distill-GGUF",
        "thinking": True,
        "filename": "Qwen3.8-9B-Q4_K_M.gguf", #Q5 6.5GB was slow & too much thinking
        "comment": "Q4, 5.8GB",
    },
    {
        "repo_id": "ornith-ai/Ornith-1.5-9B-GGUF",
        "thinking": True,
        #"filename": "Ornith-1.5-9B-Q5_K_M.gguf",
        #"comment": "Q5, 6.7GB, popular, good long text, quite restricted, annoyingly opinionated",
        "filename": "Ornith-1.5-9B-Q4_K_M.gguf",
        "comment": "Q4, 5.8GB, popular, good long text, quite restricted, annoyingly opinionated",
    },
    {
        "repo_id": "MaziyarPanahi/Nemotron-Orchestrator-8B-GGUF",
        "thinking": True,
        "filename": "Nemotron-Orchestrator-8B.Q5_K_M.gguf",
        "comment": "Q5, 5.9GB, can skip thinking, loops nonsense to limit",
    },
    {
        "repo_id": "bartowski/allura-forge_Llama-3.3-8B-Instruct-GGUF",
        "thinking": False,
        "filename": "allura-forge_Llama-3.3-8B-Instruct-Q5_K_M.gguf",
        "comment": "Q5, 5.7GB",
        #"filename": "allura-forge_Llama-3.3-8B-Instruct-IQ4_NL.gguf",
        #"comment": "IQ4, 4.7GB, seems to work",
    },
    {
        "repo_id": "bartowski/gemma-2-9b-it-GGUF",
        "thinking": False,
        #"filename": "gemma-2-9b-it-IQ4_XS.gguf",
        #"comment": "IQ4, 5.2GB, restricted",
        "filename": "gemma-2-9b-it-Q4_K_M.gguf",
        "comment": "Q4, 5.7GB, restricted",
    },
    {
        "repo_id": "bartowski/Hermes-3-Llama-3.2-3B-GGUF",
        "thinking": False,
        #"filename": "Hermes-3-Llama-3.2-3B-IQ4_XS.gguf",
        #"comment": "IQ4, 1.8GB, small, fast",
        "filename": "Hermes-3-Llama-3.2-3B-Q5_K_M.gguf",
        "comment": "Q5, 2.3GB, small",
    },
    {
        "repo_id": "mradermacher/Ornith-1.5-9B-uncensored-GGUF",
        "thinking": True,
        #"filename": "Ornith-1.5-9B-uncensored.IQ4_XS.gguf",
        #"comment": "IQ4, 5.2GB, fine summaries, gets done",
        "filename": "Ornith-1.5-9B-uncensored.Q4_K_M.gguf",
        "comment": "Q4, 5.6GB, fine summaries, gets done",
    },
    {
        "repo_id": "dealignai/Ornith-1.5-9B-UNCENSORED-GGUF",
        "thinking": True,
        #"filename": "Ornith-1.5-9B-CRACK-Q2_K.gguf",
        #"comment": "Q2, 3.8GB, likeable, keeps thinking",
        "filename": "Ornith-1.5-9B-CRACK-Q3_K_M.gguf", #Q4 5.6GB
        "comment": "Q3, 4.6GB, likeable",
    },
    {
        "repo_id": "empero-ai/Qwen3.8-4B-Distill-GGUF",
        "thinking": True,
        "filename": "Qwen3.8-4B-Q5_K_M.gguf", #Q4_K_M 2.8GB
        "comment": "Q5, 3.2GB, small, popular, seems ok, ok thinking",
    },
    {
        "repo_id": "OBLITERATUS/Ornith-1.5-9B-OBLITERATED",
        "thinking": True,
        "filename": "Ornith-1.5-9B-OBLITERATED-Q4_K_M.gguf", #IQ4 went insane
        "comment": "Q4, 5.8GB, much thinking, not censored, good",
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF",
        "thinking": True,
        "filename": "Qwopus3.5-9B-Coder-MTP-Q4_K_M.gguf", #Q3 4.7GB, Q5 6.6
        "comment": "Q4, 5.8GB, works, thinking loops",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF",
        "thinking": True,
        "filename": "gemma4-v2-Q4_K_M.gguf", #Q3_K_M 6.1GB
        "comment": "Q4, 7.4GB",
    },
    {
        "repo_id": "AnkitAI/Parable-Qwen3-8B-Claude-Fable-5-GGUF",
        "thinking": True,
        "filename": "Parable-Qwen3-8B-Claude-Fable-5-GGUF-Q4_K_M.gguf",
        "comment": "Q4, 5GB, old",
    },
    {
        "repo_id": "Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF",
        "thinking": True,
        "filename": "Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M.gguf",
        "comment": "Q4, 5.6GB, too much thinking",
    },
    {
        "repo_id": "MaziyarPanahi/DeepSeek-R1-0528-Qwen3-8B-GGUF",
        "thinking": True,
        "filename": "DeepSeek-R1-0528-Qwen3-8B.Q2_K.gguf", #Q3_K_L 4.4GB, Q4_K_M %GB
        "comment": "Q2, 3.3GB, old", #try as a small quant fast thinking deepseek or move up
    },
    {
        "repo_id": "bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF",
        "thinking": True,
        "filename": "DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf", #or try Q3_K_L 8.5GB
        "comment": "Q4, 10.4GB, big, says less thinking",
    },
    {
        "repo_id": "CMSManhattan/JiRackUltra_14b",
        "thinking": True,
        "filename": "JiRackUltra_14b_Q3_K_M.gguf",
        "comment": "Q3, 7.3GB, for CPU, limited thinking",
        #"filename": "JiRackUltra_14b_Q4_K_M.gguf", #try this
        #"comment": "Q4, 9GB, for CPU, limited thinking",
    },
    {
        "repo_id": "HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF",
        "thinking": True,
        "filename": "Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-Q2_K_P.gguf", #only one small enough
        "comment": "Q2, 10.7GB, big",
    },
    #{
    #    "repo_id": "ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF",
    #    "thinking": True,
    #    "filename": "Swift-1.5-Qwen3.8-27B-GSQ-RCO-IQ3_XXS-mtp.gguf", #they're all IQ
    #    "comment": "IQ3, 10.4GB, big, MTP, slow, funny, ok thinking, takes forever, can't cancel",
    #},
    {
        "repo_id": "bartowski/ukisai_Swift-1.5-Qwen3.8-27b-GGUF",
        "thinking": True,
        "filename": "ukisai_Swift-1.5-Qwen3.8-27b-Q2_K.gguf", #only Q that fits
        "comment": "Q2, 10.8GB, big, funny",
    },
    #{
    #    "repo_id": "JonathanColetti/Qwen3.8-27B-Uncensored-GGUF",
    #    "thinking": True,
    #    "filename": "Qwen3.8-27B-Uncensored-IQ2_M.gguf", #all Q are too big
    #    "comment": "IQ2, 10.6GB, big, MTP, popular, ok thinking, not fast, good full segment, thinks to limit",
    #},
    {
        "repo_id": "bartowski/Altworld_Hemmingway-1-GGUF",
        "thinking": True,
        #"filename": "Altworld_Hemmingway-1-IQ2_M.gguf",
        #"comment": "IQ2, 10.5GB, big, MTP, faster, overthinking, slow",
        "filename": "Altworld_Hemmingway-1-Q2_K.gguf", #only Q small enough
        "comment": "Q2, 10.8GB, big, MTP, faster, overthinking",
    },
    {
        "repo_id": "unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF",
        "thinking": False,
        "filename": "Qwen3-30B-A3B-Instruct-2507-UD-TQ1_0.gguf", #try if UD-Q3_K_XL 13.8GB can be made to run, UD-Q2_K_XL 11.8GB
        "comment": "UD-TQ1, 8GB, fast, can da, good, loops, bland, old",
    },
    {
        "repo_id": "unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF",
        "thinking": False,
        "filename": "Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_M.gguf",
        "comment": "UD-IQ2, 10.8GB, big, popular, fast, fine analysis, old, bland", #speed test this
        #"filename": "Qwen3-Coder-30B-A3B-Instruct-UD-Q2_K_XL.gguf",
        #"comment": "UD-Q2, 11.8GB, big, popular, fine analysis, old",
        #"filename": "Qwen3-Coder-30B-A3B-Instruct-UD-Q3_K_XL.gguf",
        #"comment": "UD-Q3, 13.8GB, big, popular, fine analysis, old",
    },
    {
        "repo_id": "unsloth/Qwen3-Coder-30B-A3B-Instruct-1M-GGUF",
        "thinking": False,
        "filename": "Qwen3-Coder-30B-A3B-Instruct-1M-UD-Q2_K_XL.gguf", #no other good option
        "comment": "Q2, 11.8GB, big",
    },
    {
        "repo_id": "mradermacher/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated-i1-GGUF",
        #"thinking": False,
        "filename": "Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated.i1-Q2_K.gguf",
        "comment": "Q2, 11.3GB",
    },
    {
        "repo_id": "CMSManhattan/JiRackDeltaNet_27b",
        "thinking": True,
        "filename": "JiRackDeltaNet_27b.Q2_K.gguf", #only one small enough
        "comment": "Q2, 10.9GB, big, good long-text analysis, precise, repeats, loops to limit",
    },
    {
        "repo_id": "bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF",
        "thinking": True,
        "filename": "Qwen3.6-27B-MTP-pi-tune-Q2_K.gguf", #Q3_K_S 12.3GB
        "comment": "Q2, 10.9GB, big, too much thinking",
    },
    {
        "repo_id": "unsloth/Qwen3.8-27B-GGUF",
        "thinking": True,
        "filename": "Qwen3.8-27B-UD-Q2_K_XL.gguf", #only Q small enough
        "comment": "UD-Q2, 9.8GB, big, says it can skip thinking",
    },
    {
        "repo_id": "tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF",
        "thinking": True,
        "filename": "Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf",
        "comment": "Q4, 8.5GB",
    },
    {
        "repo_id": "DevQuasar/amd.Instella-MoE-16B-A3B-Think-GGUF",
        "thinking": True,
        "filename": "Q4_K_M/amd.Instella-MoE-16B-A3B-Think.f16.gguf.Q4_K_M.gguf", #or go Q3 8.2GB
        "comment": "Q4, 10.5GB, experimental",
    },
    {
        "repo_id": "huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF",
        "thinking": True,
        #"filename": "Huihui-Qwen3.8-27B-abliterated-Q2_K.gguf",
        #"comment": "Q2, 10.9GB, works, ok thinking, not fast",
        "filename": "Huihui-Qwen3.8-27B-abliterated-UD-Q3_K_XL.gguf", #if this is too big use the next one
        "comment": "Q3, 13.3GB",
        #"filename": "Huihui-Qwen3.8-27B-abliterated-UD-Q2_K_XL.gguf",
        #"comment": "Q2, 10GB",
    },
    {
        "repo_id": "XeyonAI/Helcyon-Solara-2-14b-v2.0-GGUF",
        #"thinking": False,
        "filename": "Helcyon-Solara-2-14B-v2.0-Q4_K_M.gguf",
        "comment": "Q4, 8.2GB, personality",
    },
    {
        "repo_id": "MaziyarPanahi/solar-pro-preview-instruct-GGUF",
        #"thinking": False,
        "filename": "solar-pro-preview-instruct.Q3_K_M.gguf", #many others
        "comment": "Q3, 10.7GB",
    },
    {
        "repo_id": "MaziyarPanahi/Mistral-Small-24B-Instruct-2501-GGUF",
        #"thinking": False,
        "filename": "Mistral-Small-24B-Instruct-2501.Q3_K_M.gguf",
        "comment": "Q3, 11.5GB",
    },
    {
        "repo_id": "JetBrains/Mellum2-12B-A2.5B-Instruct-GGUF-Q4_K_M",
        #"thinking": False,
        "filename": "Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf", #only one
        "comment": "Q4, 8.1GB",
    },
    {
        "repo_id": "bartowski/Qwen2.5-Coder-14B-Instruct-abliterated-GGUF",
        #"thinking": False, #probably
        "filename": "Qwen2.5-Coder-14B-Instruct-abliterated-Q4_K_M.gguf", #many others
        "comment": "Q4, 9GB, old",
    },
    {
        "repo_id": "MN-Violet-Lotus-12B.Q4_K_M.gguf",
        #"thinking": False,
        "filename": "MN-Violet-Lotus-12B.Q4_K_M.gguf",
        "comment": "Q4, 7.4GB",
    },
    {
        "repo_id": "unsloth/GLM-4.7-Flash-REAP-23B-A3B-GGUF",
        #"thinking": False,
        "filename": "GLM-4.7-Flash-REAP-23B-A3B-Q3_K_M.gguf", #Q4 is too big, Q3_K_S 10.3GB
        "comment": "Q3, 11.3GB",
    },
    {
        "repo_id": "",
        #"thinking": False,
        "filename": "",
        "comment": "",
    },
    {
        "repo_id": "",
        #"thinking": False,
        "filename": "",
        "comment": "",
    },
]
