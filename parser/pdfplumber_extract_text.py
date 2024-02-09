import pdfplumber

def extract_text_from_pdf(pdf_path, start_page, end_page):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for counter, current_page in enumerate(pdf.pages): 
            if counter < start_page:
                # Springe zur nächsten Seite, wenn start_page noch nicht erreicht ist
                continue  
            elif counter > end_page:
                # Beende Schleife, wenn end_page überschritten wird
                break
            page_text = current_page.extract_text()
            # Entferne doppelte Leerzeilen und füge Absätze hinzu
            paragraphs = [p.strip() for p in page_text.split("\n\n") if p.strip()]
            text += " ".join(paragraphs) + " "
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
    start_page = 0
    end_page = 1

    # Extrahierung des Textes der PDF
    # Bündelung in jeweils passende Absätze im Fließtext
    text = extract_text_from_pdf(pdf_file_1, start_page, end_page)

    # Manuelle Korrekturen des Fließtextes
    text = correct_text(text)

    # Speichern des Textes in eine .txt mit UTF-8 Codierung
    file = "parser\\output_test.txt"
    with open(file, "w", encoding="utf-8") as file:
        file.write(text)



if __name__ == "__main__":
    main()
