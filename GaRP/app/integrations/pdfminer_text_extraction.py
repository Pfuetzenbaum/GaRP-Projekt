"""Copyright (C) 2024 Gantert, Schneider, Sewald

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/> """

# Importieren der notwendigen Bibliotheken
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTChar, LTTextLine
import re

# Funktion zum Extrahieren von Text aus einer PDF-Datei strukturiert
def extract_text_from_pdf_structured(pdf_path, starting_page=1, ending_page=100, check_fontname=False, first_lines_to_skip=0, last_lines_to_skip=0):
    """
    Extrahiert Text aus einer PDF-Datei mit Struktur.

    Übergabeparameter:
        pdf_path (str): Pfad zur PDF-Datei
        starting_page (int): Erste Seite, die extrahiert werden soll
        ending_page (int): Letzte Seite, die extrahiert werden soll
        check_fontname (bool): Ob der Fontname überprüft werden soll
        first_lines_to_skip (int): Anzahl der ersten Zeilen, die übersprungen werden sollen
        last_lines_to_skip (int): Anzahl der letzten Zeilen, die übersprungen werden sollen

    Rückgabe:
        str: Extrahierter und bereinigter Text
    """
    # Initialisieren der Variablen
    current_fontname = None
    current_size = 1.0
    extracted_text = ""

    current_page = 0

    # Behandlung von Ligaturen und Aufzählungszeichen, Liste erweiterbar
    special_chars = {
        "ﬃ": "ffi",
        "ﬁ": "fi",
        "ﬄ": "ffl",        
        "ﬂ": "fl",
        "ﬅ": "ft",
        "ﬀ": "ff",
        "•": "\n•",
    }

    # Durchlaufen aller Seiten der PDF-Datei
    for page in extract_pages(pdf_path):
        current_page += 1  
        # Überspringen von Seiten, die nicht extrahiert werden sollen
        if current_page < starting_page:
            continue  
        elif current_page > ending_page:
            break
        
        current_line = 0
        # Ermitteln der Gesamtzahl der Zeilen auf der aktuellen Seite
        total_lines = len([elem for elem in page if isinstance(elem, LTTextBoxHorizontal)])

        # Durchlaufen aller Elemente auf der Seite
        for page_element in page:
            # Überprüfen, ob das Element ein Textfeld ist
            if isinstance(page_element, LTTextBoxHorizontal):
                # Überspringen von Zeilen am Seitenanfang
                if current_line < first_lines_to_skip:
                    current_line += 1
                    continue 

                # Überspringen von Zeilen am Seitenende
                elif current_line >= total_lines - last_lines_to_skip:
                    break

                current_line += 1

                # Durchlaufen aller Textzeilen im Textfeld
                for text_line in page_element:
                    # Überprüfen, ob die Textzeile eine LTTextLine-Instanz ist
                    if isinstance(text_line, LTTextLine):
                        # Durchlaufen aller Zeichen (LTChar) in der Textzeile
                        for character in text_line:
                            # Überprüfen, ob das Zeichen ein LTChar-Objekt ist
                            if isinstance(character, LTChar):

                                # Ersetzen von Ligaturen bereits zu diesem Zeitpunkt
                                # Ansonsten kann es zu Problemen bei der nachträglichen Verarbeitung der Schriftart kommen kann
                                # Sofern ein Zeichen in der Liste der Sonderzeichen enthalten ist, wird es behandelt und übersprungen
                                if character.get_text() in special_chars:
                                    extracted_text += special_chars.get(character.get_text(), "")
                                    continue
                                
                                # Überprüfen, ob der Fontname berücksichtigt werden soll
                                if check_fontname:
                                    # Aufrufen der Funktion zum Überprüfen des Fontnamens und der Schriftgröße
                                    current_char, current_fontname, current_size = handle_font_change(character, current_fontname, current_size)
                                else:
                                    # Aufrufen der Funktion zum Überprüfen der Schriftgröße
                                    current_char, current_size = handle_size_change(character, current_size)

                                # Hinzufügen des aktuellen Zeichens zum extrahierten Text
                                extracted_text += current_char

                            # Leerzeichen und Zeilenumbrüche entsprechen nicht der LTChar-Klasse, sondern der LTAnno-Klasse
                            # Überprüfen, ob das Zeichen ein Leerzeichen ist
                            elif character.get_text() == " ":
                                extracted_text += " "
                            
                            # Überprüfen, ob das Zeichen ein Zeilenumbruch ist
                            elif character.get_text() == "\n":
                                # Wenn vor dem Zeilenumbruch bereits ein Bindestricht steht, wird dieser entfernt
                                # Dabei handelt es sich um eine Silbentrennung, welche den Fließtext stört
                                if extracted_text.endswith("-"):
                                    # Entfernen des Bindestrichs, indem das aktuell letzte Zeichen entfernt wird
                                    extracted_text = extracted_text[:-1]
                                else:
                                    # Wenn es sich nicht um eine Silbentrennung handelt, wird ein Leerzeichen hinzugefügt
                                    extracted_text += " "

    # Entfernen der ersten beiden Zeichen des extrahierten Textes, da diese gesetzt werden aufgrund der Änderung der Schriftgröße
    extracted_text = extracted_text[2:]

    # Aufrufen der Funktion zum Bereinigen des Textes
    cleaned_text = clean_text(extracted_text)

    # Rückgabe des bereinigten Textes
    return cleaned_text

# Funktion zum Extrahieren von Text aus einer PDF-Datei seitenweise
def extract_text_from_pdf_pagewise(pdf_path, starting_page=1, ending_page=100, first_lines_to_skip=0, last_lines_to_skip=0):
    """
    Extrahiert Text aus einer PDF-Datei seitenweise.

    Übergabeparameter:
        pdf_path (str): Pfad zur PDF-Datei
        starting_page (int): Erste Seite, die extrahiert werden soll
        ending_page (int): Letzte Seite, die extrahiert werden soll
        first_lines_to_skip (int): Anzahl der ersten Zeilen, die übersprungen werden sollen
        last_lines_to_skip (int): Anzahl der letzten Zeilen, die übersprungen werden sollen

    Rückgabe:
        str: Extrahierter und bereinigter Text
    """
    # Initialisieren der Variablen
    extracted_text = ""
    current_page = 0

    # Durchlaufen aller Seiten in der PDF-Datei
    for single_page in extract_pages(pdf_path):
        current_page += 1
        # Überspringen von Seiten, die nicht extrahiert werden sollen
        if current_page < starting_page:
            continue
        elif current_page > ending_page:
            break

        current_line = 0
        # Ermitteln der Gesamtzahl der Zeilen auf der aktuellen Seite
        total_lines = len([elem for elem in single_page if isinstance(elem, LTTextBoxHorizontal)])
        for element in single_page:
            # Überprüfen, ob das Element ein Textfeld ist
            if isinstance(element, LTTextBoxHorizontal):

                # Überspringen von Zeilen am Seitenanfang
                if current_line < first_lines_to_skip:
                    current_line += 1
                    continue 

                # Überspringen von Zeilen am Seitenanfang
                if current_line >= total_lines - last_lines_to_skip:
                    break

                current_line += 1

                # Durchlaufen aller Textzeilen im Textfeld
                for text_line in element:
                    # Überprüfen, ob die Textzeile eine LTTextLine-Instanz ist
                    if isinstance(text_line, LTTextLine):
                        # Hinzufügen des Textes der Textzeile zum extrahierten Text
                        extracted_text += text_line.get_text()

                        # Entfernen von Trennstrichen, doppelten Leerzeichen oder Zeilenumbrüchen am Zeilenende
                        if extracted_text.endswith("\n"):
                            extracted_text = extracted_text[:-1]
                            extracted_text += " "
                        
        # Hinzufügen eines Zeilenumbruchs zum extrahierten Text am Ende jeder Seite
        extracted_text = extracted_text + "\n"

    # Aufrufen der Funktion zum Bereinigen des Textes
    cleaned_text = clean_text(extracted_text)

    # Rückgabe des bereinigten Textes
    return cleaned_text

# Funktion zum Überprüfen des Fontnamens
def handle_font_change(character, current_fontname, current_size):
    """
    Überprüft den Fontnamen und die Schriftgröße und aktualisiert ihn wenn nötig.
    Bei Änderungen von mehr als 10% der Schriftgröße oder der Schriftart, wird ein Zeilenumbruch vor dem Zeichen hinzugefügt.

    Übergabeparameter:
        character (LTChar): Zeichen, das überprüft werden soll
        current_fontname (str): Aktueller Fontname
        current_size (float): Aktuelle Schriftgröße

    Rückgabe:
        tuple: Aktualisiertes Zeichen, Fontname und Schriftgröße
    """
    # Überprüfen, ob der Fontname sich geändert hat oder die Schriftgröße um mehr als 10% abweicht
    if character.fontname != current_fontname or abs(character.size - current_size) / current_size >= 0.1:
        # Aktualisieren des aktuellen Fontnamens und der Schriftgröße
        current_fontname = character.fontname
        current_size = character.size
        # Rückgabe des aktualisierten Zeichens, Fontnamens und Schriftgröße mit zwei Zeilenumbrüchen vor dem Zeichen
        return "\n\n" + character.get_text(), current_fontname, current_size
    else:
        # Rückgabe des Zeichens, Fontnamens und Schriftgröße ohne Änderungen
        return character.get_text(), current_fontname, current_size 

# Funktion zum Überprüfen der Schriftgröße
def handle_size_change(character, current_size):
    """
    Überprüft die Schriftgröße und aktualisiert sie wenn nötig.
    Bei Änderungen von mehr als 10% der Schriftgröße, wird ein Zeilenumbruch vor dem Zeichen hinzugefügt.

    Übergabeparameter:
        character (LTChar): Zeichen, das überprüft werden soll
        current_fontname (str): Aktueller Fontname
        current_size (float): Aktuelle Schriftgröße

    Rückgabe:
        tuple: Aktualisiertes Zeichen, Fontname und Schriftgröße
    """

    # Überprüfen, ob die Schriftgröße sich um mehr als 10% von der aktuellen Schriftgröße unterscheidet
    if abs(character.size - current_size) / current_size >= 0.1:
        # Aktualisieren des aktuellen Fontnamens und der Schriftgröße
        current_size = character.size
        # Rückgabe des aktualisierten Zeichens, Fontnamens und Schriftgröße mit zwei Zeilenumbrüchen vor dem Zeichen
        return "\n\n" + character.get_text(), current_size
    else:
        # Rückgabe des Zeichens, Fontnamens und Schriftgröße ohne Änderungen
        return character.get_text(), current_size 

# Funktion zum Bereinigen des Textes
def clean_text(cleaned_text):
    """
    Bereinigt den Text von unnötigen Zeichen.

    Übergabeparameter:
        cleaned_text (str): Text, der bereinigt werden soll

    Rückgabe:
        str: Bereinigter Text
    """
    # Behandlung von doppelten Leerzeichen, Umlauten und Ligaturen
    # Ersetzen von Mehrfachleerzeichen durch ein einzelnes Leerzeichen, aber keine Zeilenumbrüche
    cleaned_text = re.sub(r'[^\S\n]+', ' ', cleaned_text)

    # Behandlung von Fehlern bei Umlauten, wenn ¨ und uaoUOA darauffolgt
    cleaned_text = re.sub(r'¨([uaoUOA])', lambda m: {'u': 'ü', 'a': 'ä', 'o': 'ö', 'U': 'Ü', 'A': 'Ä', 'O': 'Ö'}[m.group(1)], cleaned_text)

    # Behandlung von Ligaturen
    cleaned_text = re.sub(r'[ﬃﬁ]', 'fi', cleaned_text)
    cleaned_text = re.sub(r'ﬀ', 'ff', cleaned_text)

    return cleaned_text

# Funktion zum Speichern des Textes in eine Datei
def save_text_to_file(text, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    output_file = "GaRP-Projekt\\GaRP\\app\\integrations\\output_test.txt"  

    filename = "GaRP-Projekt\\GaRP\\app\\integrations\\test_files\\BA_BR.pdf"
    starting_page = 7
    ending_page = 8
    
    first_lines_to_skip = 0

    last_lines_to_skip = 0

    extract_structured = True

    check_fontname = False

    if extract_structured:
        extracted_and_cleaned_text = extract_text_from_pdf_structured(filename, starting_page, ending_page, check_fontname, first_lines_to_skip, last_lines_to_skip)
    else:
        extracted_and_cleaned_text = extract_text_from_pdf_pagewise(filename, starting_page, ending_page, first_lines_to_skip, last_lines_to_skip)

    save_text_to_file(extracted_and_cleaned_text, output_file)

if __name__ == "__main__":
    main()