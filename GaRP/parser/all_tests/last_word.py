import fitz  # PyMuPDF

def extract_last_word(pdf_file, site):
    # Öffne das PDF-Dokument
    pdf_document = fitz.open(pdf_file)
    page = pdf_document[site-1]
    text = page.get_text()
    words = text.split()
    last_word = words[-1] if words else None
    pdf_document.close()
    
    return last_word

def output(character, page_number):
    if character:
        print(f"Letzte Ausgabe auf Seite {page_number} ist: {character}")
    else:
        print(f"Die Seite {page_number} ist möglicherweise leer.")


def extract_last_character(pdf_file, site):
    pdf_dokument = fitz.open(pdf_file)
    seite = pdf_dokument[site-1]
    text = seite.get_text()
    last_character = text[-2] if text.strip() else None
    pdf_dokument.close()
    
    return last_character


def main():
    pdf_file = "VSC\Sonstiges\pdf_parser\PA2_Version_7_0.pdf"
    page_number = 10
    last_word = extract_last_word(pdf_file, page_number)
    last_character = extract_last_character(pdf_file, page_number)

    output(last_word, page_number)
    output(last_character, page_number)


if __name__ == '__main__':
    main()