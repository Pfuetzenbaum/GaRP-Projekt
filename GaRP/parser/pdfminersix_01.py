from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTTextLine

def extract_text_from_pdf_pagewise(pdf_file, start_page, end_page):
    extracted_text = ""
    current_page = 0

    for single_page in extract_pages(pdf_file):
        current_page += 1
        if current_page < start_page:
            continue
        elif current_page > end_page:
            break
        for element in single_page:
            if isinstance(element, LTTextBoxHorizontal):
                for text_line in element:
                    if isinstance(text_line, LTTextLine):
                        extracted_text += text_line.get_text()
                        if extracted_text.endswith("- "):
                            extracted_text = extracted_text[:-2]
                        extracted_text = extracted_text.replace("  ", " ")
                        extracted_text = extracted_text.replace("\n", " ")
                        
        # Füge einen Seitenumbruch ein, dass jede Seite in einer neuen Zeile beginnt
        extracted_text += "Seitenumbruch einfügen"
    extracted_text = extracted_text.replace("Seitenumbruch einfügen", "\n")

    return extracted_text

def clean_text(text):
    cleaned_text = text.replace("- ", "")
    cleaned_text = cleaned_text.replace("¨u", "ü")
    cleaned_text = cleaned_text.replace("¨a", "ä")
    cleaned_text = cleaned_text.replace("¨o", "ö")
    cleaned_text = cleaned_text.replace("¨U", "Ü")
    cleaned_text = cleaned_text.replace("¨A", "Ä")
    cleaned_text = cleaned_text.replace("¨O", "Ö")
    cleaned_text = cleaned_text.replace("ﬃ", "fi")
    cleaned_text = cleaned_text.replace("ﬁ", "fi")
    cleaned_text = cleaned_text.replace("ﬀ", "ff")
    return cleaned_text

def save_text_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

# Main program
if __name__ == "__main__":
    pdf_file = "parser\\test_files\\sample01.pdf"
    start_page = 1
    end_page = 10
    output_file = "parser\\output_test.txt"

    extracted_text = extract_text_from_pdf_pagewise(pdf_file, start_page, end_page)
    cleaned_text = clean_text(extracted_text)
    save_text_to_file(cleaned_text, output_file)
