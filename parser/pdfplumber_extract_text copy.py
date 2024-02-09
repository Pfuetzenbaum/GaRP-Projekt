import pdfplumber


def extract_text(pdf_file, start_page, end_page, num_header_lines, num_footer_lines):
    # Initialisierung des Seitenzählers
    current_page = 0  

    # Initialisierung der Text Variable
    full_text = ''

    # Öffnen des PDFs mit pdfplumber
    with pdfplumber.open(pdf_file) as pdf:
        # Iteration über jede einzelne Seite, welche extrahiert wird
        for current_page, single_page in enumerate(pdf.pages):
            # Erhöhe den Seitenzähler
            current_page += 1  
            if current_page < start_page:
                # Springe zur nächsten Seite, wenn start_page noch nicht erreicht ist
                continue  
            elif current_page > end_page:
                # Beende Schleife, wenn end_page überschritten wird
                break  

            # counter für Header Behandlung
            counter = 0
            for element in single_page.extract_text().split('\n'):
                #Übergebene Anzahl an Zeilen (Header) am Anfang einer Seite ignorieren
                counter += 1
                if counter <= num_header_lines:
                    continue

                # Zusammenfügen der einzelnen List-Elemente zu einem Absatz
                full_text += element + "\n\n"

    return full_text

def correct_text(text):
    # Entfernung von ” und “, da der Latex PDFCompiler die ” in einer Zwischenzeile speichert und dadurch nach dem Parsen in die falsche Zeile schiebt
    text = text.replace(" ”", "")
    text = text.replace("“", "")

    # Behandlung von ü, ö und ä, da durch Latex PDFComplier Umlaute fehlerhaft kopiert werden
    text = text.replace(" ¨u", "ü")
    text = text.replace(" ¨a", "ä")
    text = text.replace(" ¨o", "ö")
    text = text.replace("¨u", "ü")
    text = text.replace("¨a", "ä")
    text = text.replace("¨o", "ö")

    # Wörter, bei denen die Silbentrennung die Wörter in zwei Zeilen trennt, muss der Bindestrich am Zeilenende entfernt und mit dem Wort der nächsten Zeile verbunden werden
    text = text.replace("- ", "")

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
    start_page = 1
    end_page = 2

    # Extrahierung des Textes der PDF
    # Bündelung in jeweils passende Absätze im Fließtext
    text = extract_text(pdf_file_1, start_page, end_page, num_header_lines, num_footer_lines)

    # Manuelle Korrekturen des Fließtextes
    text = correct_text(text)

    # Speichern des Textes in eine .txt mit UTF-8 Codierung
    file = "parser\\output_test.txt"
    with open(file, "w", encoding="utf-8") as file:
        file.write(text)



if __name__ == "__main__":
    main()
