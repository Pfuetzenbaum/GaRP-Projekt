from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTChar, LTTextLine

def extract_text_from_pdf(start_page, end_page, pdf_file, output_file):
    # Initialisierung des Seitenzählers
    current_page = 0

    # Initialisierung der Text Variable
    extracted_text = ""

    # Iteration über jede einzelne Seite, welche extrahiert wird
    for single_page in extract_pages(pdf_file):
        # Erhöhe den Seitenzähler
        current_page += 1
        if current_page < start_page:
            # Springe zur nächsten Seite, wenn start_page noch nicht erreicht ist
            continue
        elif current_page > end_page:
            # Beende Schleife, wenn end_page überschritten wird
            break

        for element in single_page:
            if isinstance(element, LTTextBoxHorizontal):
                for horizontal_text_box in element:
                    if isinstance(horizontal_text_box, LTTextLine):
                        for text_line in horizontal_text_box:
                            extracted_text += str(text_line)+"\n"

    save_text_to_file(extracted_text, output_file)


def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)


# Beispielaufruf der Methode
start_page = 9
end_page = 9
pdf_file = "parser\\test_files\\PA2_Version_7_0.pdf"
output_file = "parser\\output_test.txt"

extract_text_from_pdf(start_page, end_page, pdf_file, output_file)
