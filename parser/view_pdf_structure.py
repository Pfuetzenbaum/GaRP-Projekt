from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextBoxHorizontal, LTChar, LTTextContainer


# Initialisierung des Seitenzählers
current_page = 0  

start_page = 5
end_page = 6

# Initialisierung der Text Variable
extracted_text = " "
pdf_file = "C:\\Visual Studio Code\\GaRP\\GaRP-Projekt\\parser\\test_files\PA2_Version_7_0.pdf"

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
        print(element)