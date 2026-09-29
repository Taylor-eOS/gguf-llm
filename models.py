MODELS = [
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "filename": "gemma4-coding-Q4_K_M.gguf", #seems right, or go Q3 6.1GB
        "comment": "Q4, 7.4GB, in library, orig. gemma, works well, does most requests, swaps but ok",
        "thinking": False,
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF",
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf", #only one
        "comment": "Q4, 7.4GB, seems to work, good code description, good advice, few dl, not fast, history",
        "thinking": False,
    },
    {
        "repo_id": "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF",
        "filename": "qwen2.5-coder-7b-instruct-q5_k_m.gguf",
        "comment": "Q5, 5.4GB, useful, short responses, funny, history, old",
        #"filename": "qwen2.5-coder-7b-instruct-q4_k_m.gguf",
        #"comment": "Q4, 4.7GB, useful, short responses, old",
        "thinking": False,
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF",
        "filename": "Qwopus3.5-9B-coder-Exp-Q4_K_M.gguf",
        "comment": "Q4, 5.2GB, class leader, good responses, too much thinking, few dl",
        "thinking": True,
    },
    {
        "repo_id": "LiquidAI/LFM2.5-8B-A1B-GGUF",
        "filename": "LFM2.5-8B-A1B-Q4_K_M.gguf",
        "comment": "Q4, 5.2GB, MoE, ok answers",
        "thinking": True,
    },
    {
        "repo_id": "LiquidAI/LFM2.5-2.6B-GGUF",
        "filename": "LFM2.5-2.6B-Q5_K_M.gguf",
        "comment": "Q5, 1.9GB, popular, sub-4GB agentic tool-use, small, finishes thinking, nonsense summary",
        "thinking": True,
    },
    {
        "repo_id": "LiquidAI/LFM2.5-230M-GGUF",
        "filename": "LFM2.5-230M-Q8_0.gguf",
        "comment": "Q8, 247MB, too small, stops, refuses most, incoherent",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/ibm-granite_granite-4.1-8b-GGUF",
        #"filename": "ibm-granite_granite-4.1-8b-IQ4_NL.gguf",
        #"comment": "IQ4, 5.2GB, concise, good translation",
        "filename": "ibm-granite_granite-4.1-8b-Q4_K_M.gguf",
        "comment": "Q4, 5.5GB, in library, concise, good translation",
        "thinking": False,
    },
    {
        "repo_id": "DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF",
        "filename": "L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q4_k_s.gguf",
        "comment": "Q4, 10.7GB, big, ?",
        "thinking": False,
    },
    {
        "repo_id": "squ11z1/Mythos-nano",
        "filename": "mythos-nano-Q4_K_M.gguf",
        "comment": "Q4, 1.9GB, 3B, small",
        "thinking": True,
    },
    {
        "repo_id": "DreamFast/gemma-3-12b-it-heretic-v2",
        "filename": "gguf/gemma-3-12b-it-heretic-v2-Q4_K_M.gguf",
        "comment": "Q4, 7.3GB, doesn't refuse, slow, verbose, swaps",
        "thinking": False,
    },
    {
        "repo_id": "DreamFast/qwen3-8b-heretic",
        "filename": "gguf/qwen3-8b-heretic-Q4_K_M.gguf",
        "comment": "Q4, 5GB, very agreeable, ok thinking, good summaries, old",
        "thinking": True,
    },
    {
        "repo_id": "mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF",
        "filename": "meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf", #seems to make similar responses as Q6 but that was more censored
        "comment": "Q4, 4.9GB, clever, not overly censored",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        #"filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf", #not recommended in descr
        #"comment": "IQ3, 3.3GB, workhorse, limited censorship, good summaries",
        "filename": "Mistral-7B-Instruct-v0.3-Q3_K_S.gguf",
        "comment": "Q3, 3.8GB, in library, workhorse, limited censorship",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-Q6_K_L.gguf",
        "comment": "Q6, 1.4GB, in library, good small, didn't refuse, limited creativity",
        "thinking": False,
    },
    #{
    #    "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
    #    "filename": "qwen2.5-1.5b-instruct-q6_k.gguf",
    #    "comment": "Q6, 1.5GB, in library, too small, concise, can stop, refuses joke, old",
    #    "thinking": False,
    #},
    {
        "repo_id": "janhq/Jan-v3.5-4B-gguf",
        "filename": "Jan-v3.5-4B-Q5_K_M.gguf", #Q4 loops
        "comment": "Q5, 3.2GB, personality, kind of fun",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/aya-expanse-8b-GGUF",
        #"filename": "aya-expanse-8b-Q6_K_L.gguf",
        #"comment": "Q6, 6.9GB, translation, brief, didn't refuse, avoidant, useful",
        "filename": "aya-expanse-8b-Q5_K_M.gguf",
        "comment": "Q5, 5.8GB, translation, brief, didn't refuse, avoidant, useful",
        "thinking": False,
    },
    {
        "repo_id": "mradermacher/aya-expanse-8b-abliterated-i1-GGUF",
        #"filename": "aya-expanse-8b-abliterated.i1-IQ4_XS.gguf",
        #"comment": "IQ4, 4.6GB",
        "filename": "aya-expanse-8b-abliterated.i1-Q4_K_M.gguf",
        "comment": "Q4, 5.1GB",
        #"thinking": ,
    },
    {
        "repo_id": "MaziyarPanahi/mistral-small-3.1-24b-instruct-2503-hf-GGUF",
        "filename": "mistral-small-3.1-24b-instruct-2503-hf.Q3_K_M.gguf",
        "comment": "Q3, 11.5GB, big",
        #"thinking": ,
    },
    {
        "repo_id": "unsloth/gpt-oss-20b-GGUF",
        "filename": "gpt-oss-20b-UD-Q4_K_XL.gguf", #only UD that fits
        "comment": "UD-Q4, 11.9GB, popular",
        "thinking": True,
    },
    {
        "repo_id": "MaziyarPanahi/gpt-oss-20b-Derestricted-GGUF",
        "filename": "gpt-oss-20b-Derestricted.Q3_K_M.gguf",
        "comment": "Q3, 12.9GB, big, MoE",
        "thinking": True,
    },
    {
        "repo_id": "MaziyarPanahi/phi-4-GGUF",
        #"filename": "phi-4.Q5_K_M.gguf",
        #"comment": "Q5, 10.6GB, 14B, big, a tad boring, swaps, slow but useful, didn't refuse all",
        "filename": "phi-4.Q4_K_M.gguf", #several others
        "comment": "Q4, 9GB, 14B, a tad boring, didn't refuse all",
        "thinking": False,
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-it-Claude-4.6-4.8-Opus-GGUF",
        "filename": "gemma4-opus48-Q4_K_M.gguf", #other ones are Q2_K 4.8GB and Q6_K 9.8GB
        "comment": "Q4, 7.4GB",
        #"thinking": ,
    },
    {
        "repo_id": "nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF",
        "filename": "NVIDIA-Nemotron3-Nano-4B-Q4_K_M.gguf", #only one
        "comment": "Q4, 2.8GB, small",
        #"thinking": ,
    },
    {
        "repo_id": "MaziyarPanahi/NVIDIA-Nemotron-Nano-12B-v2-GGUF",
        "filename": "NVIDIA-Nemotron-Nano-12B-v2.Q2_K.gguf", #Q3_K_M 6GB, Q5_K_M 8.8GB
        "comment": "Q2, 4.7GB, seems coherent, overthinks, didn't refuse",
        #"filename": "NVIDIA-Nemotron-Nano-12B-v2.Q3_K_L.gguf", #better
        #"comment": "Q3, 6.4GB, didn't refuse",
        "thinking": True,
    },
    {
        "repo_id": "dominguesm/NVIDIA-Nemotron-Nano-9B-v2-GGUF",
        "filename": "nemotron-nano-9b-v2-q2_k.gguf", #q5_k_m 7.1GB
        "comment": "Q2, 5GB, worse code descr than 12B, good summary, ok thinking, no swap, didn't refuse",
        #"filename": "nemotron-nano-9b-v2-q4_k_s.gguf", #better
        #"comment": "Q4, 6.2GB, good summary, ok thinking, didn't refuse",
        "thinking": True,
    },
    {
        "repo_id": "VLTX/VertaLily-1.2-1B-GGUF",
        "filename": "VertaLily-1.2-1B-Q8_0-stable.gguf", #Q4 is overly censored and kind of wrong, no others
        "comment": "Q8, 1.3GB, small, can stop, follows style, good translation",
        "thinking": False,
    },
    {
        "repo_id": "MaziyarPanahi/Phi-3.5-mini-instruct-GGUF",
        #"filename": "Phi-3.5-mini-instruct.IQ4_XS.gguf",
        #"comment": "IQ4, 2GB, 3.8B, small, seems to work, uneven censorship, lineshift spam",
        "filename": "Phi-3.5-mini-instruct.Q4_K_M.gguf",
        "comment": "Q4, 2.4GB, 3.8B, small, seems to work, uneven censorship",
        "thinking": False,
    },
    {
        "repo_id": "dphn/Dolphin3.0-Llama3.1-8B-GGUF",
        #"filename": "Dolphin3.0-Llama3.1-8B-Q6_K.gguf", #small ones might fit Pi
        #"comment": "Q6, 6.6GB, in separate script, uncensored, not boring",
        "filename": "Dolphin3.0-Llama3.1-8B-Q4_K_M.gguf",
        "comment": "Q4, 4.9GB, in separate script, uncensored, not boring",
        "thinking": False,
    },
    {
        "repo_id": "second-state/dolphin-2.6-mistral-7B-GGUF",
        "filename": "dolphin-2.6-mistral-7b-Q5_K_M.gguf", #or Q4_K_M or Q6_K
        "comment": "Q5, 5.1GB, in local",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/dolphin-2.9.3-mistral-7B-32k-GGUF",
        #"filename": "dolphin-2.9.3-mistral-7B-32k-IQ4_XS.gguf", #Q6 6.3GB was good
        #"comment": "IQ4, 3.9GB, doesn't refuse, boring",
        "filename": "dolphin-2.9.3-mistral-7B-32k-Q4_K_L.gguf", #Q5_K_L 5.5GB
        "comment": "Q4, 4.7GB, doesn't refuse, boring",
        "thinking": False,
    },
    {
        "repo_id": "unsloth/gemma-4-12b-it-GGUF",
        "filename": "gemma-4-12b-it-Q4_K_M.gguf",
        "comment": "Q4, 7.1GB",
        "thinking": True,
    },
    {
        "repo_id": "jica98/qwen3.5-4B-super-coder",
        "filename": "qwen3.5-4B-super-coder.Q4_0.gguf",
        "comment": "Q4, 2.6GB, small, bad code description, fine summaried chat",
        "thinking": True,
    },
    {
        "repo_id": "DavidAU/Qwen3.5-9B-The-Defiant-Fable-Uncensored-Heretic-NEO-IMATRIX-MAX-MTP-GGUF",
        #"filename": "Qwen3.5-9B-The-Defiant-Fable-Uncnr-Heretic-NEO-MAX-IQ4_NL.gguf",
        #"comment": "IQ4, 6.6GB, thinks too much",
        "filename": "Qwen3.5-9B-The-Defiant-Fable-Uncnr-Heretic-NEO-MAX-MTP-Q4_K_M.gguf",
        "comment": "Q4, 7GB, thinks too much",
        "thinking": True,
    },
    {
        "repo_id": "unsloth/gemma-4-E2B-it-GGUF",
        #"filename": "gemma-4-E2B-it-IQ4_NL.gguf",
        #"comment": "IQ4, 3GB, small, good workhorse",
        "filename": "gemma-4-E2B-it-UD-Q4_K_XL.gguf",
        "comment": "UD-Q4, 3.2GB, small, in library, good workhorse",
        "thinking": False,
    },
    {
        "repo_id": "unsloth/gemma-4-E4B-it-GGUF",
        #"filename": "gemma-4-E4B-it-IQ4_NL.gguf", #UD-IQ3_XXS 3.7GB
        #"comment": "IQ4, 4.8GB, good workhorse, summarizes well",
        "filename": "gemma-4-E4B-it-UD-Q4_K_XL.gguf",
        "comment": "UD-Q4, 5.1GB, in library, good workhorse",
        "thinking": False,
    },
    {
        "repo_id": "shafire/Zero-Gemma4-E4B-OpenZero-GGUF",
        "filename": "Zero-Gemma4-E4B-OpenZero-Q5_K_M-F16-Merged.gguf", #only one
        "comment": "Q5, 5.9GB, few dl, image-text model",
        #"thinking": ,
    },
    {
        "repo_id": "HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive",
        "filename": " Gemma-4-E4B-Uncensored-HauhauCS-Aggressive-Q4_K_M.gguf",
        "comment": "Q4, 5.3GB, popular",
        #"thinking": ,
    },
    {
        "repo_id": "HauhauCS/Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-MTP-GGUF",
        "filename": " Qwen3.8-27B-Uncensored-HauhauCS-Aggressive-Q2_K_P.gguf", #only one small enough
        "comment": "Q2, 10.7GB, big",
        "thinking": True,
    },
    {
        "repo_id": "nguyenmanhd93/phi-4-unsloth-bnb-4bit-gguf-Q4_K_M",
        "filename": "unsloth.Q4_K_M.gguf",
        "comment": "Q4, 8.9GB, very obscure",
        #"thinking": ,
    },
    {
        "repo_id": "mradermacher/Arsh-V1-GGUF",
        "filename": "Arsh-V1.Q4_K_M.gguf",
        "comment": "Q4, 8.9GB",
        #"thinking": ,
    },
    {
        "repo_id": "openbmb/MiniCPM5-2B-GGUF",
        "filename": "MiniCPM5-2B-Q4_K_M.gguf", #Only other: Q8_0 is 2.7GB
        "comment": "Q4, 1.6GB, small, seems coherent, ok thinking",
        "thinking": True,
    },
    {
        "repo_id": "empero-ai/Qwen3.8-9B-Distill-GGUF",
        "filename": "Qwen3.8-9B-Q4_K_M.gguf", #Q5 6.5GB was slow & too much thinking
        "comment": "Q4, 5.8GB",
        "thinking": True,
    },
    {
        "repo_id": "ornith-ai/Ornith-1.5-9B-GGUF",
        "filename": "Ornith-1.5-9B-Q5_K_M.gguf", #Q4 5.8GB is probably better
        "comment": "Q5, 6.7GB, popular, good long text, quite restricted, annoyingly opinionated",
        "thinking": True,
    },
    {
        "repo_id": "MaziyarPanahi/Nemotron-Orchestrator-8B-GGUF",
        "filename": "Nemotron-Orchestrator-8B.Q5_K_M.gguf",
        "comment": "Q5, 5.9GB, can skip thinking",
        "thinking": True,
    },
    {
        "repo_id": "bartowski/allura-forge_Llama-3.3-8B-Instruct-GGUF",
        "filename": "allura-forge_Llama-3.3-8B-Instruct-Q5_K_M.gguf",
        "comment": "Q5, 5.7GB",
        #"filename": "allura-forge_Llama-3.3-8B-Instruct-IQ4_NL.gguf",
        #"comment": "IQ4, 4.7GB, seems to work",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/gemma-2-9b-it-GGUF",
        #"filename": "gemma-2-9b-it-IQ4_XS.gguf",
        #"comment": "IQ4, 5.2GB, restricted",
        "filename": "gemma-2-9b-it-Q4_K_M.gguf",
        "comment": "Q4, 5.7GB, restricted",
        "thinking": False,
    },
    {
        "repo_id": "bartowski/Hermes-3-Llama-3.2-3B-GGUF",
        #"filename": "Hermes-3-Llama-3.2-3B-IQ4_XS.gguf",
        #"comment": "IQ4, 1.8GB, small, fast",
        "filename": "Hermes-3-Llama-3.2-3B-Q5_K_M.gguf",
        "comment": "Q5, 2.3GB, small",
        "thinking": False,
    },
    {
        "repo_id": "mradermacher/Ornith-1.5-9B-uncensored-GGUF",
        #"filename": "Ornith-1.5-9B-uncensored.IQ4_XS.gguf",
        #"comment": "IQ4, 5.2GB, fine summaries, gets done",
        "filename": "Ornith-1.5-9B-uncensored.Q4_K_M.gguf",
        "comment": "Q4, 5.6GB, fine summaries, gets done",
        "thinking": True,
    },
    {
        "repo_id": "dealignai/Ornith-1.5-9B-UNCENSORED-GGUF",
        #"filename": "Ornith-1.5-9B-CRACK-Q2_K.gguf",
        #"comment": "Q2, 3.8GB, likeable, keeps thinking",
        "filename": "Ornith-1.5-9B-CRACK-Q3_K_M.gguf", #Q4 5.6GB
        "comment": "Q3, 4.6GB, likeable",
        "thinking": True,
    },
    {
        "repo_id": "empero-ai/Qwen3.8-4B-Distill-GGUF",
        "filename": "Qwen3.8-4B-Q5_K_M.gguf", #Q4_K_M 2.8GB
        "comment": "Q5, 3.2GB, small, popular, seems ok, ok thinking",
        "thinking": True,
    },
    {
        "repo_id": "OBLITERATUS/Ornith-1.5-9B-OBLITERATED",
        "filename": "Ornith-1.5-9B-OBLITERATED-Q4_K_M.gguf", #IQ4 went insane
        "comment": "Q4, 5.8GB, much thinking, not censored, good",
        "thinking": True,
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-MTP-GGUF",
        "filename": "Qwopus3.5-9B-Coder-MTP-Q4_K_M.gguf", #Q3 4.7GB, Q5 6.6
        "comment": "Q4, 5.8GB, works, thinking loops",
        "thinking": True,
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF",
        "filename": "gemma4-v2-Q4_K_M.gguf", #Q3_K_M 6.1GB
        "comment": "Q4, 7.4GB",
        "thinking": True,
    },
    {
        "repo_id": "AnkitAI/Parable-Qwen3-8B-Claude-Fable-5-GGUF",
        "filename": "Parable-Qwen3-8B-Claude-Fable-5-GGUF-Q4_K_M.gguf",
        "comment": "Q4, 5GB, old",
        "thinking": True,
    },
    {
        "repo_id": "Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash-GGUF",
        "filename": "Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M.gguf",
        "comment": "Q4, 5.6GB, too much thinking",
        "thinking": True,
    },
    {
        "repo_id": "MaziyarPanahi/DeepSeek-R1-0528-Qwen3-8B-GGUF",
        "filename": "DeepSeek-R1-0528-Qwen3-8B.Q2_K.gguf", #Q3_K_L 4.4GB, Q4_K_M %GB
        "comment": "Q2, 3.3GB, old", #try as a small quant fast thinking deepseek or move up
        "thinking": True,
    },
    {
        "repo_id": "bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF",
        "filename": "DeepSeek-Coder-V2-Lite-Instruct-Q4_K_M.gguf", #or try Q3_K_L 8.5GB
        "comment": "Q4, 10.4GB, big, says less thinking",
        "thinking": True,
    },
    {
        "repo_id": "CMSManhattan/JiRackUltra_14b",
        "filename": "JiRackUltra_14b_Q3_K_M.gguf",
        "comment": "Q3, 7.3GB, for CPU, limited thinking",
        #"filename": "JiRackUltra_14b_Q4_K_M.gguf", #try this
        #"comment": "Q4, 9GB, for CPU, limited thinking",
        "thinking": True,
    },
    #{
    #    "repo_id": "ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF",
    #    "filename": "Swift-1.5-Qwen3.8-27B-GSQ-RCO-IQ3_XXS-mtp.gguf", #they're all IQ
    #    "comment": "IQ3, 10.4GB, big, MTP, slow, 100%, funny, ok thinking, takes forever, can't cancel",
    #    "thinking": True,
    #},
    {
        "repo_id": "bartowski/ukisai_Swift-1.5-Qwen3.8-27b-GGUF",
        "filename": "ukisai_Swift-1.5-Qwen3.8-27b-Q2_K.gguf", #only Q that fits
        "comment": "Q2, 10.8GB, big, funny",
        "thinking": True,
    },
    #{
    #    "repo_id": "JonathanColetti/Qwen3.8-27B-Uncensored-GGUF",
    #    "filename": "Qwen3.8-27B-Uncensored-IQ2_M.gguf", #all Q are too big
    #    "comment": "IQ2, 10.6GB, big, MTP, popular, ok thinking, not fast, good full segment, thinks to limit",
    #    "thinking": True,
    #},
    {
        "repo_id": "bartowski/Altworld_Hemmingway-1-GGUF",
        #"filename": "Altworld_Hemmingway-1-IQ2_M.gguf",
        #"comment": "IQ2, 10.5GB, big, MTP, faster, overthinking, slow",
        "filename": "Altworld_Hemmingway-1-Q2_K.gguf", #only Q small enough
        "comment": "Q2, 10.8GB, big, MTP, faster, overthinking",
        "thinking": True,
    },
    {
        "repo_id": "unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF",
        "filename": "Qwen3-30B-A3B-Instruct-2507-UD-TQ1_0.gguf",
        "comment": "UD-TQ1, 8GB, fast, can da, good, loops, bland, old",
        "thinking": False,
    },
    {
        "repo_id": "MaziyarPanahi/Qwen3-30B-A3B-GGUF",
        "filename": "Qwen3-30B-A3B.Q2_K.gguf",
        "comment": "Q2, 11.3GB, old",
        #"thinking": , #says it can switch seamlessly
    },
    {
        "repo_id": "unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF",
        "filename": "Qwen3-Coder-30B-A3B-Instruct-UD-IQ2_M.gguf",
        "comment": "UD-IQ2, 10.8GB, big, feels fast, good, old",
        "thinking": False,
    },
    {
        "repo_id": "CMSManhattan/JiRackDeltaNet_27b",
        "filename": "JiRackDeltaNet_27b.Q2_K.gguf", #only one small enough
        "comment": "Q2, 10.9GB, big, 100%, very good analysis, precise, repeats, thinks to limit",
        "thinking": True,
    },
    {
        "repo_id": "bytkim/Qwen3.6-27B-MTP-pi-tune-GGUF",
        "filename": "Qwen3.6-27B-MTP-pi-tune-Q2_K.gguf", #Q3_K_S 12.3GB
        "comment": "Q2, 10.9GB, big, too much thinking",
        "thinking": True,
    },
    {
        "repo_id": "unsloth/Qwen3.8-27B-GGUF",
        "filename": "Qwen3.8-27B-UD-Q2_K_XL.gguf", #only Q small enough
        "comment": "UD-Q2, 9.8GB, big, says it can skip thinking",
        "thinking": True,
    },
    {
        "repo_id": "tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF",
        "filename": "Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf",
        "comment": "Q4, 8.5GB",
        "thinking": True,
    },
    {
        "repo_id": "FINAL-Bench/POCKET-26B-GGUF",
        "filename": "POCKET-26B-Q2_K.gguf", #only one small enough
        "comment": "Q2, 11.1GB, big, korean",
        #"thinking": ,
    },
    {
        "repo_id": "DevQuasar/amd.Instella-MoE-16B-A3B-Think-GGUF",
        "filename": "Q4_K_M/amd.Instella-MoE-16B-A3B-Think.f16.gguf.Q4_K_M.gguf", #or go Q3 8.2GB
        "comment": "Q4, 10.5GB, experimental",
        "thinking": True,
    },
    {
        "repo_id": "huihui-ai/Huihui-Qwen3.8-27B-abliterated-GGUF",
        "filename": "Huihui-Qwen3.8-27B-abliterated-Q2_K.gguf", #try it out and remove if it's loopy
        "comment": "Q2, 10.9GB",
        #"thinking": ,
    },
    {
        "repo_id": "XeyonAI/Helcyon-Solara-2-14b-v2.0-GGUF",
        "filename": "Helcyon-Solara-2-14B-v2.0-Q4_K_M.gguf",
        "comment": "Q4, 8.2GB, personality",
        #"thinking": ,
    },
    {
        "repo_id": "MaziyarPanahi/solar-pro-preview-instruct-GGUF",
        "filename": "solar-pro-preview-instruct.Q3_K_M.gguf", #many others
        "comment": "Q3, 10.7GB",
        #"thinking": ,
    },
    {
        "repo_id": "MaziyarPanahi/Mistral-Small-24B-Instruct-2501-GGUF",
        "filename": "Mistral-Small-24B-Instruct-2501.Q3_K_M.gguf",
        "comment": "Q3, 11.5GB",
        #"thinking": ,
    },
    {
        "repo_id": "JetBrains/Mellum2-12B-A2.5B-Instruct-GGUF-Q4_K_M",
        "filename": "Mellum2-12B-A2.5B-Instruct-Q4_K_M.gguf", #only one
        "comment": "Q4, 8.1GB",
        #"thinking": ,
    },
    {
        "repo_id": "",
        "filename": "",
        "comment": "",
        #"thinking": ,
    },
]
