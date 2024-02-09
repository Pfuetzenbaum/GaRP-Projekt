import pdfplumber

def extract_text_from_pdf(pdf_path, start_page, end_page):
    with pdfplumber.open(pdf_path) as pdf:
        words = []
        prev_font = None
        prev_size = None
        for counter, current_page in enumerate(pdf.pages): 
            if counter < start_page:
                # Springe zur nächsten Seite, wenn start_page noch nicht erreicht ist
                continue  
            elif counter > end_page:
                # Beende Schleife, wenn end_page überschritten wird
                break
            page_words = current_page.extract_text()
            for word in page_words:
                # font = word['fontname']
                # size = word['size']
                # text = word['text']
                # if font != prev_font or size != prev_size:
                #     words.append('\n')  # Füge neuen Absatz hinzu
                # words.append(text + ' ')
                # prev_font = font
                # prev_size = size

    # combined_text = ''.join(words)
    # return combined_text


def main():

    pdf = "parser\\TestDokument.pdf"
    print(extract_text_from_pdf(pdf, 0, 1))
    text = "tbd"

    # Speichern des Textes in eine .txt mit UTF-8 Codierung
    file = "parser\\output_test.txt"
    with open(file, "w", encoding="utf-8") as file:
        file.write(text)


if __name__ == "__main__":
    main()
