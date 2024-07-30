from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTChar, LTTextLine, LTAnno

def extract_text_from_pdf_structured(pdf_path, starting_page=1, ending_page=100, check_fontname=False, first_lines_to_skip=0):
    current_fontname = None
    current_size = 1.0
    text = ""

    # Initialisierung des Seitenzählers
    current_page = 0

    for page in extract_pages(pdf_path):
        
        # Erhöhe den Seitenzähler
        current_page += 1  
        if current_page < starting_page:
            # Springe zur nächsten Seite, wenn starting_page noch nicht erreicht ist
            continue  
        elif current_page > ending_page:
            # Beende Schleife, wenn ending_page überschritten wird
            break
        
        current_line = 0
        for page_element in page:
            if isinstance(page_element, LTTextBoxHorizontal):

                # Überspringe die ersten Zeilen der Seite
                if current_line < first_lines_to_skip:
                    current_line += 1
                    continue 

                for text_line in page_element:
                    if isinstance(text_line, LTTextLine):
                        for character in text_line:
                            if isinstance(character, LTChar):

                                # Problembehandlung von Ligaturen und Aufzählungszeichen
                                match character.get_text():
                                    case "ﬀ":
                                        text += "ff"
                                        continue
                                    case "ﬃ":
                                        text += "ffi"
                                        continue
                                    case "•":
                                        text += "\n•"
                                        continue
                                
                                if check_fontname == True:
                                    current_char, current_fontname, current_size = handle_font_change(character, current_fontname, current_size)
                                else:
                                    current_char, current_fontname, current_size = handle_size_change(character, current_fontname, current_size)

                                text += current_char

                            elif isinstance(character, LTAnno):
                                text += " "
    text = text[2:]
    return text

def extract_text_from_pdf_pagewise(pdf_file, starting_page=1, ending_page=100, first_lines_to_skip=0):
    extracted_text = ""
    current_page = 0

    for single_page in extract_pages(pdf_file):
        current_page += 1
        if current_page < starting_page:
            continue
        elif current_page > ending_page:
            break

        current_line = 0
        for element in single_page:
            if isinstance(element, LTTextBoxHorizontal):

                # Überspringe die ersten Zeilen der Seite
                if current_line < first_lines_to_skip:
                    current_line += 1
                    continue 

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

def handle_font_change(character, current_fontname, current_size):
    if character.fontname != current_fontname or abs(character.size - current_size) / current_size >= 0.1:
        current_fontname = character.fontname
        current_size = character.size
        return "\n\n" + character.get_text(), current_fontname, current_size
    else:
        return character.get_text(), current_fontname, current_size 

def handle_size_change(character, current_fontname, current_size):
    if abs(character.size - current_size) / current_size >= 0.1:
        current_fontname = character.fontname
        current_size = character.size
        return "\n\n" + character.get_text(), current_fontname, current_size
    else:
        return character.get_text(), current_fontname, current_size

def clean_text(cleaned_text):
    # Gedacht für Silbentrennung am Zeilenende
    # Problematisch, da es auch regulär in Texten vorkommen kann bsp.: Vor- und Nachteile
    cleaned_text = cleaned_text.replace("- ", "")

    # Behandlung von Umlauten aus Latex
    cleaned_text = cleaned_text.replace("¨u", "ü")
    cleaned_text = cleaned_text.replace("¨a", "ä")
    cleaned_text = cleaned_text.replace("¨o", "ö")
    cleaned_text = cleaned_text.replace("¨U", "Ü")
    cleaned_text = cleaned_text.replace("¨A", "Ä")
    cleaned_text = cleaned_text.replace("¨O", "Ö")

    # Behandlung von Ligaturen
    cleaned_text = cleaned_text.replace("ﬃ", "fi")
    cleaned_text = cleaned_text.replace("ﬁ", "fi")
    cleaned_text = cleaned_text.replace("ﬀ", "ff")
    return cleaned_text

def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    # Standardwerte für die Textextraktion
    output_file = "parser\\output_test.txt"  
    plain_text = ""

    # Einstellungen für die Textextraktion, abhängig von der PDF-Datei
    filename = "parser\\test_files\\BA_BR.pdf"
    starting_page = 8
    ending_page = 13
    
    # Anzahl der Zeilen, die zu Beginn jeder Seite übersprungen werden sollen
    first_lines_to_skip = 2

    # True: Strukturiert nach Schriftart und Schriftgröße
    # False: Unstrukturiert, nur Seitenweise Extraktion
    extract_structured = False

    # Notwendig, wenn extract_structured = True
    # True: Gruppierung nach Schriftart und Schriftgröße
    # False: Gruppierung nur nach Schriftgröße
    check_fontname = False

    if extract_structured:
        plain_text = extract_text_from_pdf_structured(filename, starting_page, ending_page, check_fontname, first_lines_to_skip)
    else:
        plain_text = extract_text_from_pdf_pagewise(filename, starting_page, ending_page, first_lines_to_skip)

    cleaned_text = clean_text(plain_text)
    save_text_to_file(cleaned_text, output_file)

if __name__ == "__main__":
    main()