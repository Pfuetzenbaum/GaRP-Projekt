import pdfplumber

# Pfadeinstellung zum PDF-Dokument
pdf_path = 'parser\\TestDokument.pdf'

# Öffne das PDF-Dokument mit pdfplumber
with pdfplumber.open(pdf_path) as pdf:
    # Durchlaufe jede Seite des Dokuments
    last_font = ""
    last_size = ""
    text = ""

    
    for page in pdf.pages:
        for char in page.chars:
            char_text = char.get("text")  # Holen des Textes des aktuellen Zeichens
            if char.get("fontname") == last_font and char.get("size") == last_size:
                # Überprüfe, ob char_text nicht None ist, bevor du ihn an den Text anhängst
                if char_text is not None:
                    text = text + char_text
            else:
                # Füge einen Zeilenumbruch am Ende der Seite hinzu
                text += "\n"
                # Füge den aktuellen Text zu text hinzu, füge dann eine neue Zeile hinzu
                if char_text is not None:
                    text = text + char_text
            last_font = char.get("fontname")
            last_size = char.get("size")
    file = "parser\\output_test.txt"
    with open(file, "w", encoding="utf-8") as file:
        file.write(text)


    # Durchlaufe jeden Text und die zugehörigen Textboxen
    # for text, box in zip(texts.split('\n'), boxes):
        # Extrahiere die Schriftgröße und Schriftart aus den Box-Attributen
        # print(box.get('top'))
        # font_size = box['size']
        # font_name = box['fontname']
        
        # # Gib die Schriftgröße, Schriftart und den Text aus
        # print(f"Schriftgröße: {font_size}, Schriftart: {font_name}, Text: {text}")
