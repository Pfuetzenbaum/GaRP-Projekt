import pdfplumber

def extract_text_from_pdf(pdf_path, start_page, end_page):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        last_font = ""
        last_size = ""

        for page in pdf.pages:
            # Überspringe Seiten vor start_page
            if page.page_number < start_page:
                continue
            
            # Beende die Schleife, wenn end_page erreicht ist
            if page.page_number > end_page:
                break

            for char in page.chars:
                char_text = char.get("text")
                if char.get("fontname") == last_font and char.get("size") == last_size:
                    if char_text is not None:
                        text += char_text
                else:
                    # Füge einen Zeilenumbruch am Ende der Seite hinzu
                    text += "\n"
                    if char_text is not None:
                        text += char_text
                last_font = char.get("fontname")
                last_size = char.get("size")
        return text

        
def correct_text(text):
    # Entfernung von ” und “, da der Latex PDFCompiler die ” in einer Zwischenzeile speichert und dadurch nach dem Parsen in die falsche Zeile schiebt
    # text = text.replace(" ”", "")
    # text = text.replace("“", "")

    # Behandlung von ü, ö und ä, da durch Latex PDFComplier Umlaute fehlerhaft kopiert werden
    text = text.replace(" ¨u", "ü")
    text = text.replace(" ¨a", "ä")
    text = text.replace(" ¨o", "ö")
    text = text.replace("¨u", "ü")
    text = text.replace("¨a", "ä")
    text = text.replace("¨o", "ö")

    # Wörter, bei denen die Silbentrennung die Wörter in zwei Zeilen trennt, muss der Bindestrich am Zeilenende entfernt und mit dem Wort der nächsten Zeile verbunden werden
    text = text.replace("-\n", "")

    return text

def main():

    # Zwei unterschiedliche PDFs zum testen

    # Word -> PDF
    pdf_file_1 = 'parser\\TestDokument.pdf'
    # Latex -> PDF
    pdf_file_2 = 'parser\\PA2_Version_7_0.pdf'

    # Anzahl Header und Footer Zeilen
    num_header_lines = 0
    num_footer_lines = 0

    # Seiten, welche ausgelesen werden
    start_page = 6
    end_page = 8

    # Extrahierung des Textes der PDF
    # Bündelung in jeweils passende Absätze im Fließtext
    text = extract_text_from_pdf(pdf_file_2, start_page, end_page)

    # Manuelle Korrekturen des Fließtextes
    # text = correct_text(text)

    # Speichern des Textes in eine .txt mit UTF-8 Codierung
    file = "parser\\output_test.txt"
    with open(file, "w", encoding="utf-8") as file:
        file.write(text)



if __name__ == "__main__":
    main()
