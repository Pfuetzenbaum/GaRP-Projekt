import fitz  # PyMuPDF

# Pfad zum PDF-Dokument
pdf_path = 'parser\\test_files\\sample05.pdf'

# PDF-Dokument öffnen
document = fitz.open(pdf_path)

# Anzahl der Seiten im Dokument
num_pages = document.page_count

print(f'Das Dokument hat {num_pages} Seiten.')

# Inhalt jeder Seite auslesen und drucken
for page_num in range(num_pages):
    page = document.load_page(page_num)
    text = page.get_text()
    print(f'Inhalt der Seite {page_num + 1}:')
    print(text)
    print('----------------------------------------')

# Dokument schließen
document.close()
