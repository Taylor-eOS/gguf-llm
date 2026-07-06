N_THREADS = 6
N_CTX = 4 * 1024
MAX_TOKENS = 2 * 1024
PRINT_PROCESSING_PROMPT = False
SYSTEM_INSTRUCTION = " [Write continuously.]"
BASE = 'Role: You are a sequential text processing tool that is run from a script. Output only the requested text itself. Do not add any other explanations or comments.'
REQUESTS = [
    'Condense this book segment into a simple and clear encapsulation. Present the central causal mechanism while omitting less important details. Compress a summary of the main point. Infer the underlying meaning instead of restating what the text said. Write for a reader that gets an entire book of similar segments summarized separately, wanting to extract the gist of each segment. Assume the context is known and does not have to be repeated. Do not sanitize contrarian aspects. Apply the same narrative voice as the original content. Omit introductory phrases like “the takeaway is”.',
    'Write this segment into a slightly less difficult language, while preserving exactly the same meaning, nuance, tone, implications, qualifications, and level of detail. Leave sentences unchanged unless they contain wording that is unusually complex, formal, or cumbersome for an adult general reader. Replace heavily burdened vocabulary or excessively difficult words when more common alternatives would express the same meaning. Split sentences that are overloaded with multiple distinct ideas, but do not summarize or remove information. Do not make the writing simpler than necessary. The goal is only to smooth excessive complexity. When a choice is uncertain, preserve the original wording. It should be readable for a general audience. Never use em dashes or snaily parenthetical insertions.',
    'Comment on the ideas in this segment from a book. The point is not to repeat or summarize the content, but to provide constructive criticism.',
    'Write this segment into different words, so it means the same but is not immediately recognizable as the same text.',
]
CODE_TASK = "Task: Briefly summarize what this code does in one sentece."

