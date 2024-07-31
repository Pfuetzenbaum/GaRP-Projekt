import customtkinter as ctk
from tkinter import filedialog, Menu, Text
import sys
import os
from tkinterdnd2 import DND_FILES, TkinterDnD

# Append the path to the top-level project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now the import should work
from GaRP.parser.pdfminer_text_extraction import extract_text_from_pdf_structured

# Default settings
settings = {
    "starting_page": 1,
    "ending_page": 100,
    "check_fontname": False,
    "first_lines_to_skip": 0
}

def check_spelling():
    # This function will handle the spell check logic
    # Call Java Function from Luis???
    pass

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    if file_path:
        process_file(file_path)

def process_file(file_path):
    extracted_text = extract_text_from_pdf_structured(
        file_path,
        starting_page=settings["starting_page"],
        ending_page=settings["ending_page"],
        check_fontname=settings["check_fontname"],
        first_lines_to_skip=settings["first_lines_to_skip"]
    )
    pdf_content_textbox.insert("end", extracted_text)

def open_settings_window():
    def save_settings():
        settings["starting_page"] = int(starting_page_entry.get())
        settings["ending_page"] = int(ending_page_entry.get())
        settings["check_fontname"] = check_fontname_var.get()
        settings["first_lines_to_skip"] = int(first_lines_to_skip_entry.get())
        settings_window.destroy()

    settings_window = ctk.CTkToplevel(root)
    settings_window.title("Einstellungen")
    settings_window.geometry("600x400")

    ctk.CTkLabel(settings_window, text="Starting Page:").pack(pady=5)
    starting_page_entry = ctk.CTkEntry(settings_window)
    starting_page_entry.insert(0, settings["starting_page"])
    starting_page_entry.pack(pady=5)

    ctk.CTkLabel(settings_window, text="Ending Page:").pack(pady=5)
    ending_page_entry = ctk.CTkEntry(settings_window)
    ending_page_entry.insert(0, settings["ending_page"])
    ending_page_entry.pack(pady=5)

    ctk.CTkLabel(settings_window, text="Check Font Name:").pack(pady=5)
    check_fontname_var = ctk.BooleanVar(value=settings["check_fontname"])
    check_fontname_checkbox = ctk.CTkCheckBox(settings_window, text="", variable=check_fontname_var)
    check_fontname_checkbox.pack(pady=5)

    ctk.CTkLabel(settings_window, text="First Lines to Skip:").pack(pady=5)
    first_lines_to_skip_entry = ctk.CTkEntry(settings_window)
    first_lines_to_skip_entry.insert(0, settings["first_lines_to_skip"])
    first_lines_to_skip_entry.pack(pady=5)

    ctk.CTkButton(settings_window, text="Save", command=save_settings).pack(pady=20)

# Main application window
root = ctk.CTk()
root.title("PDF Spell& Grammar Checker")
root.geometry("1200x800")

# Set the appearance mode and default color theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# Menu bar
menu = Menu(root)
root.config(menu=menu)
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Datei", menu=file_menu)
file_menu.add_command(label="Öffnen", command=upload_file)
file_menu.add_separator()
file_menu.add_command(label="Schließen", command=root.quit)

settings_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Einstellungen", menu=settings_menu)
settings_menu.add_command(label="Setting", command=open_settings_window)

help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Hilfe", menu=help_menu)

# Frame for uploading file
upload_frame = ctk.CTkFrame(root)
upload_frame.pack(pady=20, fill='x', padx=20)

upload_label = ctk.CTkLabel(upload_frame, text="Datei zur Rechtschreibprüfung hierhin ziehen oder Datei hinzufügen")
upload_label.pack(side='left', padx=10)

upload_button = ctk.CTkButton(upload_frame, text="Datei auswählen...", command=upload_file)
upload_button.pack(side='right', padx=10)

# Drag-and-drop field
# dnd_label = ctk.CTkLabel(upload_frame, text="Datei per Drag and Drop hier...", width=550, height=100, corner_radius=10)
# dnd_label.pack(pady=10, fill='x')
# dnd_label.drop_target_register(DND_FILES)
# dnd_label.dnd_bind('<<Drop>>', drop)


# Frame for PDF content
content_frame = ctk.CTkFrame(root)
content_frame.pack(pady=20, fill='both', expand=True, padx=20)

content_label = ctk.CTkLabel(content_frame, text="PDF Inhalt")
content_label.pack(anchor='w', pady=5)

pdf_content_textbox = Text(content_frame, height=10, wrap='word', borderwidth=1, relief='solid')
pdf_content_textbox.pack(pady=5, fill='both', expand=True)

check_button = ctk.CTkButton(content_frame, text="Überprüfen", command=check_spelling)
check_button.pack(pady=5)

# Frame for spell check results
result_frame = ctk.CTkFrame(root)
result_frame.pack(pady=20, fill='x', padx=20)

# Here you would dynamically add labels for each spelling mistake found
result_label_1 = ctk.CTkLabel(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_1.pack(anchor='w')
result_label_2 = ctk.CTkLabel(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_2.pack(anchor='w')
result_label_3 = ctk.CTkLabel(result_frame, text="\"...lorem ipsum...\"   Z.4-6")
result_label_3.pack(anchor='w')

# Start the application
root.mainloop()
