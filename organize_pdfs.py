import os
import re
import shutil
import fitz 

def extract_keywords(pdf_path):
    keywords = set()
    with fitz.open(pdf_path) as doc:
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text("text")
            # Extract keywords using a simple regex
            keywords.update(re.findall(r'\b\w+\b', text.lower()))
    return keywords

def main(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            keywords = extract_keywords(pdf_path)

            # Ask the user for keywords
            user_keywords = input(f"Enter keywords for {filename} (comma-separated): ").split(',')

            for keyword in user_keywords:
                keyword_folder = os.path.join(output_folder, keyword.strip())
                if not os.path.exists(keyword_folder):
                    os.makedirs(keyword_folder)
                shutil.copy(pdf_path, keyword_folder)

if __name__ == "__main__":
    print("Scannig pdf.........")
    input_folder = "scanned_pdfs/"
    output_folder = "output/"
    main(input_folder, output_folder)
