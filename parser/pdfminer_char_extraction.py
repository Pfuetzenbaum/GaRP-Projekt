from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTChar, LTTextLine, LTAnno

def extract_paragraphs_from_pdf(pdf_path):
    current_fontname = None
    current_size = 1
    text = ""

    for page_layout in extract_pages(pdf_path):
        for page in page_layout:
            if isinstance(page, LTTextBoxHorizontal):
                for text_line in page:
                    if isinstance(text_line, LTTextLine):
                        for character in text_line:
                            if isinstance(character, LTChar):

                                # Problembehandlung von ff und ffi
                                if character.get_text() == "ﬀ":
                                    text += "ff"
                                    continue
                                if character.get_text() == "ﬃ":
                                    text += "ffi"
                                    continue

                                # Wenn Fontname sich ändert oder die Schriftart sich um mehr als 20% ändert, dann füge einen Zeilenumbruch ein
                                # if character.fontname != current_fontname or abs(character.size - current_size) / current_size >= 0.2:
                                
                                if abs(character.size - current_size) / current_size >= 0.05:
                                    current_fontname = character.fontname
                                    current_size = character.size
                                    text += "\n\n" + character.get_text()
                                else:
                                    text += character.get_text()
                            elif isinstance(character, LTAnno):
                                text += " "                     
    return text
                                    


# Beispielaufruf
filename = "parser\\test_files\\sample04.pdf"
plain_text = extract_paragraphs_from_pdf(filename)

cleaned_text = plain_text.replace("- ", "")
cleaned_text = cleaned_text.replace(" ¨u", "ü")
cleaned_text = cleaned_text.replace(" ¨a", "ä")
cleaned_text = cleaned_text.replace(" ¨o", "ö")
cleaned_text = cleaned_text.replace("¨u", "ü")
cleaned_text = cleaned_text.replace("¨a", "ä")
cleaned_text = cleaned_text.replace("¨o", "ö")

file = "parser\\output_test.txt"
with open(file, "w", encoding="utf-8") as file:
    file.write(cleaned_text)