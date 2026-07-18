import fitz
import os

# Input and output folders
pdf_folder = "source_documents"
output_folder = "extracted_text"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Traverse all subfolders inside source_documents
for root, dirs, files in os.walk(pdf_folder):

    for filename in files:

        if filename.lower().endswith(".pdf"):

            pdf_path = os.path.join(root, filename)

            print(f"Processing: {pdf_path}")

            try:
                # Open PDF
                pdf = fitz.open(pdf_path)

                all_text = ""

                # Extract text from each page
                for page in pdf:
                    all_text += page.get_text()

                pdf.close()

                # Get relative path from source_documents
                relative_path = os.path.relpath(root, pdf_folder)

                # Create matching folder structure in extracted_text
                save_folder = os.path.join(output_folder, relative_path)
                os.makedirs(save_folder, exist_ok=True)

                # Create txt filename
                output_file = os.path.join(
                    save_folder,
                    filename.replace(".pdf", ".txt")
                )

                # Save extracted text
                with open(output_file, "w", encoding="utf-8") as file:
                    file.write(all_text)

                print(f"✓ Completed: {filename}")

            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")

print("\nAll PDFs Converted Successfully!")