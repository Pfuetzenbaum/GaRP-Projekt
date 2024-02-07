from pdfminer.high_level import extract_text

def extract_text_and_headings(pdf_path, num_header_lines, num_footer_lines, start_page, end_page):
    extracted_text = ""
    for page_num in range(start_page - 1, end_page):
        text = extract_text(pdf_path, page_numbers=[page_num])
        
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
    # text = text.replace('-\n\n', '') 
    # text = text.replace('\n\n', '')

    return text

def bundle_paragraphs(text):
    formated_text =''
    text = text.split('\n\n')
    
    for paragraph in text:
        if '♀' in paragraph:
            paragraph = paragraph.replace('\n','')
            formated_text += paragraph + '\n\n'
        else:
            paragraph = paragraph.replace('\n','')
            formated_text += paragraph + '\n\n'

    return formated_text



def main():
    pdf_file = 'C:\\Visual Studio Code\\VSC\\Sonstiges\\pdf_parser\\TestDokument_Robin.pdf'
    num_header_lines = 0
    num_footer_lines = 0
    start_page = 1
    end_page = 2

    extracted_text = extract_text_and_headings(pdf_file, num_header_lines, num_footer_lines, start_page, end_page)
    optimized_text = optimize_extracted_text(extracted_text)
    optimized_text = remove_hyphen(optimized_text)
    optimized_text = bundle_paragraphs(optimized_text)

    print("Extrahierter Text:")
    print(optimized_text)

if __name__ == "__main__":
    main()
