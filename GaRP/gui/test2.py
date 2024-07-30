import tkinter as tk
from tkinter import filedialog, Text

import sys
import os

# Füge den Pfad zur obersten Ebene deines Projekts hinzu
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Jetzt sollte der Import funktionieren
from GaRP.parser.pdfminer_text_extraction import extract_text_from_pdf_structured


def check_spelling():
    # This function will handle the spell check logic
    pass

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        extracted_text= extract_text_from_pdf_structured(file_path)
        pdf_content_textbox.insert(tk.END, extracted_text)

# Main application window
root = tk.Tk()
root.title("PDF Spell Checker")

# Menu bar
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Datei", menu=file_menu)
file_menu.add_command(label="Open", command=upload_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Einstellungen", menu=edit_menu)

help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Hilfe", menu=help_menu)

# Frame for uploading file
upload_frame = tk.Frame(root, padx=10, pady=10)
upload_frame.pack(pady=20)

upload_label = tk.Label(upload_frame, text="Datei zur Rechtschreibprüfung hierhin ziehen oder Datei hinzufügen")
upload_label.pack()

upload_button = tk.Button(upload_frame, text="Upload File", command=upload_file)
upload_button.pack()

# Frame for PDF content
content_frame = tk.Frame(root, padx=10, pady=10)
content_frame.pack(pady=20)

content_label = tk.Label(content_frame, text="PDF Inhalt")
content_label.pack()

pdf_content_textbox = Text(content_frame, height=10, width=50)
pdf_content_textbox.pack()

check_button = tk.Button(content_frame, text="Überprüfen", command=check_spelling)
check_button.pack()

# Frame for spell check results
result_frame = tk.Frame(root, padx=10, pady=10)
result_frame.pack(pady=20)

# Here you would dynamically add labels for each spelling mistake found
result_label_1 = tk.Label(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_1.pack()
result_label_2 = tk.Label(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_2.pack()
result_label_3 = tk.Label(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_3.pack()

# Start the application
root.mainloop()
