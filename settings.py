N_THREADS = 6
N_CTX = 4 * 1024
MODELS = [
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF", #non-thinking, good, censored
        "filename": "gemma4-coding-Q4_K_M.gguf",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF", #non-thinking
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF", #non-thinking, good, censored
        "filename": "gemma4-coding-Q4_K_M.gguf",
    },
    {
        "repo_id": "deadbydawn101/RavenX-OpenFable-Coder-Gemma-4-12B-GGUF", #non-thinking
        "filename": "RavenX-OpenFable-Coder-Gemma-4-12B-Q4_K_M.gguf",
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF", #thinking
        "filename": "Qwopus3.5-9B-coder-Exp-Q4_K_M.gguf",
    },
    {
        "repo_id": "prithivMLmods/VibeThinker-3B-GGUF", #thinking, doesn't finish
        "filename": "VibeThinker-3B.Q4_K_M.gguf",
    },
    {
        "repo_id": "LiquidAI/LFM2.5-8B-A1B-GGUF", #thinking, fast MoE, refuses
        "filename": "LFM2.5-8B-A1B-Q4_K_M.gguf",
    },
    {
        "repo_id": "tvall43/Qwen3.6-14B-A3B-FableVibes-GGUF", #non-thinking, not tested
        "filename": "Qwen3.6-14B-A3B-FableVibes-Q4_K_M.gguf",
    },
    {
        "repo_id": "Qwen2.5-Coder-7B-Instruct-GGUF", #non-thinking, not tested
        "filename": "qwen2.5-coder-7b-instruct-q4_k_m.gguf",
    },
    {
        "repo_id": "bartowski/ibm-granite_granite-4.1-8b-GGUF", #non-thinking, not tested
        "filename": "ibm-granite_granite-4.1-8b-Q4_K_M.gguf",
    },
    {
        "repo_id": "DavidAU/Llama-3.2-8X3B-MOE-Dark-Champion-Instruct-uncensored-abliterated-18.4B-GGUF", #non-thinking, censored
        "filename": "L3.2-8X3B-MOE-Dark-Champion-Inst-18.4B-uncen-ablit_D_AU-Q4_k_s.gguf",
    },
    {
        "repo_id": "dphn/Dolphin3.0-Llama3.1-8B-GGUF", #general, not tested
        "filename": "Dolphin3.0-Llama3.1-8B-Q4_K_M.gguf",
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-it-Claude-4.6-4.8-Opus-GGUF", #not tested
        "filename": "gemma4-opus48-Q2_K.gguf"
        #"filename": "gemma4-opus48-Q4_K_M.gguf",
    },
    {
        "repo_id": "squ11z1/Mythos-nano", #thinking, fast, censored
        "filename": "mythos-nano-Q4_K_M.gguf",
    },
    {
        "repo_id": "DevQuasar/huihui-ai.Qwen3-8B-abliterated-GGUF", #thinking, can't stop, not that fast
        "filename": "huihui-ai.Qwen3-8B-abliterated.Q4_K_M.gguf",
    },
    {
        "repo_id": "DreamFast/gemma-3-12b-it-heretic-v2", #non-thinking, slow, verbose, uncensored
        "filename": "gguf/gemma-3-12b-it-heretic-v2-Q4_K_M.gguf",
    },
    {
        "repo_id": "DreamFast/qwen3-8b-heretic", #not tested
        "filename": "gguf/qwen3-8b-heretic-Q4_K_M.gguf",
    },
    {
        "repo_id": "mlabonne/Meta-Llama-3.1-8B-Instruct-abliterated-GGUF", #not tested
        "filename": "meta-llama-3.1-8b-instruct-abliterated.Q4_K_M.gguf",
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF", #workhorse, not abliterated, fast, non-thinking, limited censorship, 3.29GB
        "filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf"
        #"filename": "Mistral-7B-Instruct-v0.3-IQ4_NL.gguf",
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF", #for Pi, 1.12GB, concise, stops, precise
        "filename": "qwen2.5-1.5b-instruct-q4_k_m.gguf",
    },
    {
        "repo_id": "Andycurrent/Gemma-3-1B-it-GLM-4.7-Flash-Heretic-Uncensored-Thinking_GGUF", #806MB, very fast, repeats, thinks, can't stop
        "filename": "Gemma-3-1B-it-GLM-4.7-Flash-Heretic-Uncensored-Thinking_Q4_k_m.gguf",
    },
    {
        "repo_id": "janhq/Jan-v3.5-4B-gguf", #personality, 2.72GB, fast, non-thinking, refuses, kind of fun
        "filename": "Jan-v3.5-4B-Q4_K_M.gguf",
    },
    {
        "repo_id": "bartowski/aya-expanse-8b-GGUF", #for translation, not tested
        "filename": "aya-expanse-8b-IQ4_XS.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/aya-expanse-8b-abliterated-GGUF", #for translation, abliterated, Q5, not tested
        "filename": "aya-expanse-8b-abliterated.Q5_K_M.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/mistral-small-3.1-24b-instruct-2503-hf-GGUF", #big, slow, other one tested
        "filename": "mistral-small-3.1-24b-instruct-2503-hf.Q4_K_S.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/gpt-oss-20b-Derestricted-GGUF", #not tested
        "filename": "gpt-oss-20b-Derestricted.Q4_K_M.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/Qwen3-14B-GGUF", #not tested
        "filename": "Qwen3-14B.Q4_K_M.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/Mistral-Small-Instruct-2409-GGUF", #not tested
        "filename": "Mistral-Small-Instruct-2409.IQ4_XS.gguf",
    },
    {
        "repo_id": "MaziyarPanahi/phi-4-GGUF", #not tested
        "filename": "phi-4.Q4_K_M.gguf",
    },
    {
        "repo_id": "unsloth/GLM-4.7-Flash-REAP-23B-A3B-GGUF", #not tested
        "filename": "GLM-4.7-Flash-REAP-23B-A3B-IQ4_NL.gguf",
    },
    {
        "repo_id": "TheBloke/em_german_mistral_v01-GGUF", #not tested
        "filename": "em_german_mistral_v01.Q4_K_M.gguf"
    }
]
