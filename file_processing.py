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
    if settings.PRINT:
        print(prompt)
    result = llm.create_chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=settings.MAX_TOKENS,
        temperature=0.7,
        top_p=0.9,
    )
    return result["choices"][0]["message"]["content"].strip()

def main():
    model = pick_model()
    llm = load_model(model)
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        if settings.SEGMENT_MODE:
            paragraph_lines = []
            for raw_line in infile:
                line = raw_line.rstrip("\n")
                if line.strip() == "":
                    if paragraph_lines:
                        paragraph = "\n".join(paragraph_lines)
                        output = process_line(llm, paragraph)
                        print(output)
                        outfile.write(output + "\n\n")
                        outfile.flush()
                        paragraph_lines = []
                    else:
                        outfile.write("\n")
                        outfile.flush()
                else:
                    paragraph_lines.append(line)
            if paragraph_lines:
                paragraph = "\n".join(paragraph_lines)
                output = process_line(llm, paragraph)
                print(output)
                outfile.write(output + "\n")
                outfile.flush()
        else:
            for raw_line in infile:
                line = raw_line.rstrip("\n")
                if line.strip() == "":
                    outfile.write("\n")
                    outfile.flush()
                else:
                    output = process_line(llm, line)
                    print(output)
                    outfile.write(output + "\n")
                    outfile.flush()

if __name__ == "__main__":
    main()
