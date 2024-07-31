import tkinter as tk
from tkinter import filedialog, Text, ttk
import sys
import os
from tkinterdnd2 import DND_FILES, TkinterDnD

# Append the path to the top-level project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from GaRP.parser.pdfminer_text_extraction import extract_text_from_pdf_structured

def check_spelling():
    # This function will handle the spell check logic
    # Call Java Function from Luis???
    pass

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        process_file(file_path)

def process_file(file_path):
    extracted_text = extract_text_from_pdf_structured(file_path)
    pdf_content_textbox.insert(tk.END, extracted_text)

def drop(event):
    file_path = event.data
    process_file(file_path)

# Main application window
root = TkinterDnD.Tk()
root.title("PDF Spell& Grammar Checker")
root.geometry("1800x900")

style = ttk.Style()
style.theme_use("clam")

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
upload_frame = ttk.Frame(root, padding=(20, 10))
upload_frame.pack(pady=20, fill='x')

upload_label = ttk.Label(upload_frame, text="Datei zur Rechtschreibprüfung hierhin ziehen oder Datei hinzufügen")
upload_label.pack(side='left', padx=10)

upload_button = ttk.Button(upload_frame, text="Datei auswählen..", command=upload_file)
upload_button.pack(side='right', padx=10)

# Drag-and-drop field
dnd_label = ttk.Label(upload_frame, text="Drag and Drop...", relief="solid", padding=(10, 10))
dnd_label.pack(pady=10, fill='x')
dnd_label.drop_target_register(DND_FILES)
dnd_label.dnd_bind('<<Drop>>', drop)

# Frame for PDF content
content_frame = ttk.Frame(root, padding=(20, 10))
content_frame.pack(pady=20, fill='both', expand=True)

content_label = ttk.Label(content_frame, text="PDF Inhalt")
content_label.pack(anchor='w')

pdf_content_textbox = Text(content_frame, height=10, width=70, wrap='word', borderwidth=1, relief='solid')
pdf_content_textbox.pack(pady=5, fill='both', expand=True)

check_button = ttk.Button(content_frame, text="Überprüfen", command=check_spelling)
check_button.pack(pady=5)

# Frame for spell check results
result_frame = ttk.Frame(root, padding=(20, 10))
result_frame.pack(pady=20, fill='x')

# Here you would dynamically add labels for each spelling mistake found
result_label_1 = ttk.Label(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_1.pack(anchor='w')
result_label_2 = ttk.Label(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_2.pack(anchor='w')
result_label_3 = ttk.Label(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_3.pack(anchor='w')

# Start the application
root.mainloop()
