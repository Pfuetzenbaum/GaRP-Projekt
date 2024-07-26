from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTTextLine

# Initialisierung des Seitenzählers
current_page = 0  

start_page = 6
end_page = 7

# Initialisierung der Text Variable
extracted_text = ""
pdf_file = "parser\\test_files\\sample03.pdf"
# pdf_file = "C:\\Visual Studio Code\\GaRP\\GaRP-Projekt\\parser\\test_files\TestDokument.pdf"


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

    extracted_text += "Leerzeichen einfügen"

    for element in single_page:
        if isinstance(element, LTTextBoxHorizontal):
            for text_line in element:
                if isinstance(text_line, LTTextLine):
                    extracted_text += text_line.get_text()
                    if extracted_text.endswith("- "):
                        extracted_text = extracted_text[:-2]
                    extracted_text = extracted_text.replace("  ", " ")
                    extracted_text = extracted_text.replace("\n", " ")

extracted_text = extracted_text.replace("Leerzeichen einfügen", "\n")


# # Folgend werden Bindestriche am Zeilenende entfernt
#     # Text in einzelne Zeilen aufteilen
#     lines = extracted_text.splitlines()
#     print(lines)

#     # Zeilenweise durchgehen und "-\n" oder "- \n" entfernen
#     cleaned_lines = []
#     for line in lines:
#         if line.endswith("- "):
#             cleaned_lines.append(line[:-2])
#         else:
#             if line.endswith("-"):
#                 cleaned_lines.append(line[:-1])
#             else:
#                 cleaned_lines.append(line)

# Bereinigten Text wieder zusammenfügen
# cleaned_text = ''.join(cleaned_lines)


cleaned_text = extracted_text.replace("- ", "")
cleaned_text = cleaned_text.replace(" ¨u", "ü")
cleaned_text = cleaned_text.replace(" ¨a", "ä")
cleaned_text = cleaned_text.replace(" ¨o", "ö")
cleaned_text = cleaned_text.replace("¨u", "ü")
cleaned_text = cleaned_text.replace("¨a", "ä")
cleaned_text = cleaned_text.replace("¨o", "ö")

file = "parser\\output_test.txt"
with open(file, "w", encoding="utf-8") as file:
    file.write(cleaned_text)