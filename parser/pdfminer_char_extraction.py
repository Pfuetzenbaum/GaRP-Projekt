from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTChar, LTTextLine

def extract_paragraphs_from_pdf(pdf_path):
    current_fontname = None
    current_size = None
    text = ""

    for page_layout in extract_pages(pdf_path):
        for page in page_layout:
            if isinstance(page, LTTextBoxHorizontal):
                for text_line in page:
                    if isinstance(text_line, LTTextLine):
                        for character in text_line:
                            if isinstance(character, LTChar):
                                if character.fontname != current_fontname or character.size != current_size:
                                    current_fontname = character.fontname
                                    current_size = character.size
                                    text += "\n" + character.get_text()
                                else:
                                    if character.get_text() != "\n":
                                        text += character.get_text()
                                    if character.get_text() == "":
                                        print("Empty character")
    return text
                                    


# Beispielaufruf
filename = "parser\\test_files\\sample02.pdf"
plain_text = extract_paragraphs_from_pdf(filename)

file = "parser\\output_test.txt"
with open(file, "w", encoding="utf-8") as file:
    file.write(plain_text)