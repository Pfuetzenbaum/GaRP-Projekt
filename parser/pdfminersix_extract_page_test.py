import PyPDF2

from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar

def extract_pages_content(pdf_file):
    page_text = []
    line_format = []
    for pagenum, page in enumerate(extract_pages(pdf_file)):
        for element in page:
            if isinstance(element, LTTextContainer):
                (line_text, format_per_line) = text_extraction(element)
                page_text.append(line_text)
                line_format.append(format_per_line)
    
    print(page_text)


def text_extraction(element):
    line_text = element.get_text()

    line_formats = []

    for text_line in element:
        for character in text_line:
            if isinstance(character, LTChar):
                line_formats.append(character.fontname)
                line_formats.append(character.size)
    format_per_line = list(set(line_formats))

    return line_text, format_per_line


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

    extract_pages_content(pdf_file_1)

    # Speichern des Textes in eine .txt mit UTF-8 Codierung
    # file = "parser\\output_test.txt"
    # with open(file, "w", encoding="utf-8") as file:
    #     file.write(text)



if __name__ == "__main__":
    main()