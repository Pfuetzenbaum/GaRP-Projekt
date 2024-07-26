import fitz  # PyMuPDF

def extract_text_and_headings(pdf_path, num_header_lines, num_footer_lines, start_page, end_page):
    extracted_text = ""
    with fitz.open(pdf_path) as pdf_document:
        for page_num in range(start_page - 1, end_page):
            page = pdf_document.load_page(page_num)
            text = page.get_text()
            
            # Ignoriere Header
            lines = text.split('\n')[num_header_lines:]
            
            # Ignoriere Footer, wenn num_footer_lines nicht 0 ist
            if num_footer_lines != 0:
                lines = lines[:-num_footer_lines]
            
            # Füge den verbleibenden Text zur gesamten extrahierten Textvariable hinzu
            extracted_text += '\n'.join(lines)
    return extracted_text

def optimize_extracted_text(extracted_text):
    bereinigter_text = extracted_text.replace(" ¨u", "ü")
    bereinigter_text = bereinigter_text.replace(" ¨a", "ä")
    bereinigter_text = bereinigter_text.replace(" ¨o", "ö")
    bereinigter_text = bereinigter_text.replace("¨u", "ü")
    bereinigter_text = bereinigter_text.replace("¨a", "ä")
    bereinigter_text = bereinigter_text.replace("¨o", "ö")
    return bereinigter_text

def remove_hyphen(text):
    # Bindestriche am Satzende entfernen
    text = text.replace('-\n', '')  

    # lines = text.split('\n')

    # for line in lines:
    #     if ".\n" in line:
    #         text = text.replace('\n', ' ')

    return text

def main():
    pdf_file = "c:\\Visual Studio Code\\VSC\\Sonstiges\\pdf_parser\\PA2_Version_7_0.pdf"
    num_header_lines = 1
    num_footer_lines = 0
    start_page = 6
    end_page = 7

    extracted_text = extract_text_and_headings(pdf_file, num_header_lines, num_footer_lines, start_page, end_page)
    optimized_text = optimize_extracted_text(extracted_text)
    fluent_text = remove_hyphen(optimized_text)

    print("Extrahierter Text:")
    print(fluent_text)

if __name__ == "__main__":
    main()
