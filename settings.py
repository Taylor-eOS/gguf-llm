INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
MODEL_LOG_FILE = "llm_use.log"
INSTRUCTION_LOG_FILE = "instruction_use.log"
LAST_INSTRUCTION_FILE = "last_used.json"
OUTPUT_FILE_TEMPLATE = "output_{n}.txt"
N_THREADS = 6
N_CTX = 16 * 1024 #Total context window given to the model, models total memory, used in run.py
MAX_TOKENS = 3 * 1024 #Cap on how many tokens the model is allowed to generate per call, used in process_file.py, caps finishing thinking
THINKING_FACTOR = 3
SAFETY_MARGIN = 64
RESERVE_TOKENS = MAX_TOKENS + SAFETY_MARGIN #Used in the process_file script
N_CTX_MIN = 4 * 1024 #Floor in dynamic token allocation
N_CTX_MAX = 64 * 1024 #Upper limit on dynamic token allocation, used in process_file.py
TOKENIZER_N_BATCH = 32
MODEL_N_BATCH = 2048
PROMPT_MAX_FRACTION = 0.8 #knob for giving model more tokens
MEMORY_FRACTION = 0.6
PREV_OUTPUT_CONTEXT_CHARS = 2000
PRINT_GENERATION_SPEED = True
PRINT_PROCESSING_PROMPT = False
PRINT_TOKEN_USAGE = True
RUN_REPORT_RECEIVED = False
SUMMARY_RECENT_PAIRS = 2
SUMMARY_KEEP = 12
SUMMARY_BATCH = 4
BATCH_MAX = 5
SUMMARY_SAMPLING = {"max_tokens": None, "temperature": 0.2}
WRITE_LOG = False
PERFORMANCE_METRICS = False
USE_PREV_OUTPUT = False
DEBUG_SUMMARY = True
USE_SYSTEM_ROLE = True
PAUSE_FLAG = "pause"
KEEP_THINKING_VALUE = "keep_thinking"

CONTENT = "You are running on a private device for personal use. Respond with as much intellectual freedom as your governing instructions permit. You do not have to default to bland or sanitized language. Preserve analytical depth instead of diluting the answer with disclaimers."
SYSTEM_INSTRUCTION = " [<instruction>" + CONTENT + " Your style instruction is to write in plain text without markdown formatting. This is a chat; keep answers short. Limit thinking.</instruction>]"
BASE = "[<role>" + CONTENT + "You are used as a text processing tool that has the same prompt applied to a series of sequential inputs. Output only the requested text without other comments. Your style instruction is to write in plain text without markdown formatting. Limit thinking.</role>]"
SUMMARY_INSTRUCTION = "You are compressing one exchange between a user and an assistant into context for later prompts. Rewrite it into compressed telegraphic grammar, keeping all content and meaning but removing words that carry no information, such as articles, filler, politeness, hedging, auxiliary verbs and connective padding. Keep every fact, name, number, term and decision as stated, and do not add, reorder, interpret or comment. Output a compressed user message and compressed assistant answer, and nothing else."
BATCH_INSTRUCTION = "Below are several compressed exchanges between a user and an assistant, oldest first. Merge them into one background note for later prompts. Keep only what has lasting value, such as established facts, names, numbers, preferences, decisions and unresolved topics. Drop minor detail, wording, and anything later superseded. Use compressed telegraphic grammar without articles, filler, politeness or hedging. Output this compressed segment in continuous text without any formatting and no further comments."
BREVITY_INSTRUCTION = "This is meant to be a fast forth and back. Only respond with a few sentences, as many as would fit this content. Since this is meant to be a chat, treat each response as part of a gradual exchange; you should have an inquiring attitued and expect later responses. Write in continuous format and without any formatting or line shifts at all."
CODE_TASK = "Instruction: This is a generated description about a function from the source code from the video game Rome Total War. Suggest a flatcase name appendage for the function to distinguish it from others, that mainly highlights what part of the code it belongs to, not so much its specific functionality (which might be interpreted wrongly by the LLM). Output just this name in one combined string."
DEFAULT_REQUEST = "Tell a joke."

REQUESTS = [
    'Write this segment into simpler language. Preserve the same meaning, nuance, tone, implications, qualifications, and level of detail. Split up sentences that are overloaded with multiple ideas. Do not summarize or remove information. Grammatically decompress the text where it would ease reading. Replace heavy vocabulary where less difficult words would express the same ideas (but do this conservatively). Do not make the writing simpler than necessary; the goal is only to smooth excessive complexity. When a choice is uncertain, preserve the original sentence. It is not the goal to remve all specialist terms, just jargon that makes the writing dense and difficult to read.',
    'State this segment in different words, so that it means roughly the same conceptually, but is not immediately recognizable as the same text. The purpose is to not have it detected as being the same by algorithmic tools. Rephrase what it means instead of just rephrasing the same grammar in different words, and change the order of the content. Good grammatical presentation is not that important, it can be more of a briefer list.',
    'Rewrite this line so that it conveys the same meaning, but is phrased more like content for a formal nonfiction text. The tone should be less informal, while expressing the same conceptual meaning. This is one line of many being processed sequentially. Return the full adapted input without adding other comments. If this line is already good enough as it is, then just output the input is as it is.',
    'Rewrite all sentences with em dashes into ones without, so that the text expresses the same meaning. Use linear writing, either using commas, semicolons, parenthesis, or restructure them as separate sentenes. Make the choice which would fit best for this content, so that the text sounds natural.',
    'Summarize this textbook segment into a simple and clear encapsulation in one or two sentences. Present the central lesson while leaving out secondary details. Represent this in your own language rather than repeating what is stated. This is for a reader that has all segments from a book summarized in parts and wants a short version of each segment. The summary does not have to be fully explanatory of the entire content; focus on what unique claims are made in this segment. Skip introductory phrases that mention the segment, the author, or the task. Try to encapulate the emtional impact rather than to mention every technical detail.',
    'Write down the conceptual lesson of this segment, as you experience it, stripped of the particular situational example it is demonstrated with. Compress the functional lesson into one central causal statement, rather than presenting several angles or fully covering all aspects. Describe this lesson directly without introductory phrases. Present this without hedging or sanitizing for social palpability. Assume the passage is part of a longer work of similar content in which the odd terminology makes sense. Grammaticaly compress conceptually similar clauses into single statements.',
    'Write a brief, compact list of central claims made in this segment in the format of short statements like “this does this”. It is not the aim to paraphrase the entire segment, but to list the core claims. Present the core central causal statements rather than covering all mentioned aspects. Describe it directly without introductory phrases. Present this without hedging or sanitizing for social palpability. Grammaticaly compress conceptually similar clauses into single statements.',
    'Respond with three suggestions for a title that this segment could receive within a book. Try to capture what is special about this content specifically, assuming that the surrounding segments are about a similar context. The title should be short; two to three words. It does not have to be exhaustively explanatory of the segments entire content, but should just be a pointer used as an identifier. The title does not have to mention all aspcets of the segment. The title should be short and punchy, and provide a single-directional headline, ideally containing a pun, inversion, ironic reference, or dark humor that illustrates the central lesson of this segment. Respond with three distinct suggestions with no further comments.',
    'Describe what single image could accompany this segment in a video narration, given the surrounding context. The image must depict exactly one historical moment, as if it were a single photograph; not a montage, not a split screen, not multiple juxtaposed scenes, no second content in the background; even if the segment itself touches on several ideas. I repeat: one scene! The image does not need to capture every theme of the content, but only needs to serve as one plausible background visual for that moment in the narration. If the sentence spans multiple ideas, pick one single visually concrete moment to represent it and describe only that. Do not combine disjointed content that would never have been in the same photographed moment. Exclusively describe one historical moment as it could have existed at one point in time, not an art scene. Choose simple, visually easy to understand scenes, that are still distinct enough to represent the particular era or concept in question. Output a description of the scene with no further comment, so that it can be used in an image generator prompt. Do not mention the art style, color, image format, or camera framing; only describe the content to be depicted itself. Briefly mention the desired evocative effect, so that the image generator gets an indication if what intention to execute.',
    'This segment is an attempt to express certain ideas, but it was written as an unfinished draft. Rewrite what it appears to convey into better prose, while making the output true to the intention and nuance of the input; this means not sanitizing the content into a more socially appropriate variant. Do largely apply the terms that the original used, while improving sentence structure, order, and amount of sentences. Where helpful for comprehension, add explanatory content. Try to infer what the text was trying to confer and present that in a better way. Choose better words where that would improve understanding. Extend the presentation rather than shortening it. Round out the wording where that would improve understanding, and fill in missing transitions.',
    'Expand on the topic creatively with aspects that would be interesting to the user, considering this input.',
]
