from utils import is_cached, load_model, pick_model
import settings

input_file = "input.txt"
output_file = "output.txt"

def process_line(llm, line):
    parts = [
        f"Input content: \"{line}\"",
        settings.BASE,
        f"Task: {settings.REQUEST}\nProcessed:",
    ]
    prompt = "\n".join(parts)
    if settings.PRINT_PROCESSING_PROMPT:
        print(prompt)
    result = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=settings.MAX_TOKENS,
        temperature=0.7,
        top_p=0.9,
    )
    return result["choices"][0]["message"]["content"].strip()

def write_output(outfile, output):
    print(output)
    outfile.write(output + "\n")
    outfile.flush()

def process_segments(llm, infile, outfile):
    paragraph_lines = []
    for raw_line in infile:
        line = raw_line.rstrip("\n")
        if line.strip() == "":
            if paragraph_lines:
                write_output(outfile, process_line(llm, "\n".join(paragraph_lines)))
                paragraph_lines = []
            outfile.write("\n")
            outfile.flush()
        else:
            paragraph_lines.append(line)
    if paragraph_lines:
        write_output(outfile, process_line(llm, "\n".join(paragraph_lines)))

def process_lines(llm, infile, outfile):
    for raw_line in infile:
        line = raw_line.rstrip("\n")
        if line.strip() == "":
            outfile.write("\n")
            outfile.flush()
        else:
            write_output(outfile, process_line(llm, line))

def main():
    model = pick_model()
    llm = load_model(model)
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        if settings.SEGMENT_MODE:
            process_segments(llm, infile, outfile)
        else:
            process_lines(llm, infile, outfile)

if __name__ == "__main__":
    main()
