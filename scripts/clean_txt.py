import os
import re

input_folder = "extracted_text"
output_folder = "cleaned_text"

os.makedirs(output_folder, exist_ok=True)

for root, dirs, files in os.walk(input_folder):

    for filename in files:

        if filename.endswith(".txt"):

            input_path = os.path.join(root, filename)

            with open(
                input_path,
                "r",
                encoding="utf-8"
            ) as file:

                text = file.read()

            # Cleaning operations
            text = re.sub(r"Page\s+\d+", "", text)
            text = re.sub(r"-{3,}", "", text)
            text = text.replace("\t", " ")
            text = re.sub(r"\s+", " ", text)

            # Preserve folder structure
            relative_path = os.path.relpath(root, input_folder)
            save_folder = os.path.join(output_folder, relative_path)

            os.makedirs(save_folder, exist_ok=True)

            output_path = os.path.join(save_folder, filename)

            with open(
                output_path,
                "w",
                encoding="utf-8"
            ) as output:

                output.write(text)

            print(f"{filename} Cleaned")

print("All Files Cleaned Successfully")