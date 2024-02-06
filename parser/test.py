from pdfminer.high_level import extract_text
import nltk
nltk.download('punkt')  # Ressourcen für Tokenisierung
from nltk.tokenize import sent_tokenize
import chardet
import re


def get_codec(pdf_file):
    with open(pdf_file, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']


def extract_text_from_pdf(pdf_file, start_page, end_page):
    pdf_text = extract_text(pdf_file, page_numbers=range(start_page, end_page))
    return pdf_text
    

def create_full_sentences(extracted_text):
    optimized_text = ''.join(char if char.isprintable() or char.isspace() else ' ' for char in extracted_text)
    full_sentences = sent_tokenize(optimized_text)

    return full_sentences


def optimize_extraced_text(extracted_text):
    bereinigter_text = extracted_text.replace("¨u", "ü")
    bereinigter_text = bereinigter_text.replace("¨a", "ä")
    bereinigter_text = bereinigter_text.replace("¨o", "ö")

    return bereinigter_text


def combine_text(final_sentences):
    complete_text = ' '.join(final_sentences)
    complete_text = complete_text.replace('-\n', '')  # Entferne Bindestriche am Zeilenende
    # complete_text = complete_text.replace('\n', ' ')  # Ersetze Zeilenumbrüche durch Leerzeichen

    return complete_text
    
    
def main():
    pdf_file = "VSC\Sonstiges\pdf_parser\PA2_Version_7_0.pdf"

    extracted_text = extract_text_from_pdf(pdf_file,5,7)
    optimized_text = optimize_extraced_text(extracted_text)
    final_sentences = create_full_sentences(optimized_text)
    final_text = combine_text(final_sentences)
    
    print(final_text)


if __name__ == '__main__':
    main()