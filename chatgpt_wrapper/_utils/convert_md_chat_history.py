# https://chat.openai.com/chat/effcc859-59e3-448d-8110-efcd823f4408
"""
I have a directory of .md (Markdown) files that each hold one our our previous chat histories.

The files begin with the Model used. i.e.:
Model: Default (GPT-3.5)

Then the file continues with the history of the prompts-responses. The prompts I sent, prefixed with the symbol ‘>’, then a single line with only ‘>’, then a line with ‘>1 / 1' like the following:
> is the example you have given me based on actual contracts you have knowledge of?
>
> 1 / 1

Then there is a single blank line, followed by a paragraph of output from you, followed by a single blank line then ‘1 / 1’ (that indicates your first response is complete). I.e.
As an AI language model, I do not have access to specific contracts or agreements between companies. However, the example I provided is based on common provisions and practices found in recruitment services agreements between recruitment companies and their clients. The language used in the agreement is similar to what one might expect to find in a typical recruitment services agreement, but it is not meant to be a substitute for legal advice. It is always recommended that both parties consult with legal counsel when drafting or reviewing any contract or agreement.

1 / 1

I’d like you to generate a Python script that ingests all of the Markdown files and then outputs a single .csv file that contains:
Name of Ingest file, Prompt Number, Prompt Test, Response.

Do you need anything clarified before we begin? Can you start by outputting the psudocode for me to review?
"""
import os
import csv

# Define the directory path where the markdown files are located
directory_path = "H:\My Drive\PERSONAL\Chat-GPT Conversation History"

# Create a list to hold the extracted data
data_list = []

# Loop through each markdown file in the directory
for file_name in os.listdir(directory_path):
    if file_name.endswith(".md"):

        # Extract the model name from the file
        with open(os.path.join(directory_path, file_name), "r", encoding="utf-8") as f:
            model_name = f.readline().strip().replace("Model: ", "")

        # Read the contents of the markdown file and split it into a list of lines
        with open(os.path.join(directory_path, file_name), "r", encoding="utf-8") as f:
            content = f.read()
            lines = content.split("\n")

        # Loop through each line in the markdown file and extract the prompts and responses
        prompt_num = 1
        for i, line in enumerate(lines):
            if line.startswith(">"):
                # Extract the prompt text
                prompt_text = line.replace(">", "").strip()

                # Extract the response text if it exists
                if len(lines) > i + 2:
                    response_text = lines[i + 2].strip()
                else:
                    response_text = ""

                # Add the data to the list
                data_list.append([file_name, model_name, prompt_num, prompt_text, response_text])

                # Increment the prompt number
                prompt_num += 1

# Write the data to a CSV file
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["File Name", "Model", "Prompt Number", "Prompt Text", "Response"])
    writer.writerows(data_list)