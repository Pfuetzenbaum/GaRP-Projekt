import customtkinter as ctk
from tkinter import filedialog, Menu, Text
import sys
import os
from tkinterdnd2 import DND_FILES, TkinterDnD
from py4j.java_gateway import JavaGateway

gateway = JavaGateway() 

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

# Global variables
words_to_except = []
file_path = None

def check_spelling():
    # This function will handle the spell check logic
    # Call Java Function from Luis???
    pass

def open_except_words():
    def except_words_list():
        word_to_except = except_words_entry.get()
        if word_to_except:
            words_to_except.append(word_to_except)
            except_words_entry.delete(0, 'end')
            update_except_words_list()

    def update_except_words_list():
        # Clear the existing list before adding new labels
        for widget in words_frame.winfo_children():
            widget.destroy()
        
        for word in words_to_except:
            ctk.CTkLabel(words_frame, text=word).pack(anchor='w')

    except_words_window = ctk.CTkToplevel(root)
    except_words_window.title("Wörter entfernen")
    except_words_window.geometry("600x400")

    ctk.CTkLabel(except_words_window, text="Zu entfernendes Wort:").pack(padx=5, pady=5)
    except_words_entry = ctk.CTkEntry(except_words_window)
    except_words_entry.pack(padx=5, pady=5)

    ctk.CTkButton(except_words_window, text="Save", command=except_words_list).pack(side="bottom", padx=5, pady=20)

    words_frame = ctk.CTkFrame(except_words_window)
    words_frame.pack(fill='both', expand=True, padx=5, pady=5)

    update_except_words_list()

    except_words_window.lift()
    except_words_window.focus_force()

def upload_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
    if file_path:
        file_label.config(text=f"Selected file: {file_path}")

def process_file():
    if file_path:
        extracted_text = extract_text_from_pdf_structured(
            file_path,
            starting_page=settings["starting_page"],
            ending_page=settings["ending_page"],
            check_fontname=settings["check_fontname"],
            first_lines_to_skip=settings["first_lines_to_skip"]
        )
        pdf_content_textbox.delete("1.0", "end")
        pdf_content_textbox.insert("1.0", extracted_text)
    else:
        error_window = ctk.CTkToplevel(root)
        error_window.title("Fehler")
        error_window.geometry("200x100")
        ctk.CTkLabel(error_window, text="Keine Datei ausgewählt!").pack(padx=5, pady=5)

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

    ctk.CTkLabel(settings_window, text="Starting Page:").pack(padx=5, pady=5)
    starting_page_entry = ctk.CTkEntry(settings_window)
    starting_page_entry.insert(0, settings["starting_page"])
    starting_page_entry.pack(padx=5, pady=5)

    ctk.CTkLabel(settings_window, text="Ending Page:").pack(padx=5, pady=5)
    ending_page_entry = ctk.CTkEntry(settings_window)
    ending_page_entry.insert(0, settings["ending_page"])
    ending_page_entry.pack(padx=5, pady=5)

    ctk.CTkLabel(settings_window, text="Check Font Name:").pack(padx=5, pady=5)
    check_fontname_var = ctk.BooleanVar(value=settings["check_fontname"])
    check_fontname_checkbox = ctk.CTkCheckBox(settings_window, text="", variable=check_fontname_var)
    check_fontname_checkbox.pack(padx=5, pady=5)

    ctk.CTkLabel(settings_window, text="First Lines to Skip:").pack(padx=5, pady=5)
    first_lines_to_skip_entry = ctk.CTkEntry(settings_window)
    first_lines_to_skip_entry.insert(0, settings["first_lines_to_skip"])
    first_lines_to_skip_entry.pack(padx=5, pady=5)

    ctk.CTkButton(settings_window, text="Save", command=save_settings).pack(side="bottom", padx=5, pady=20)

    settings_window.lift()
    settings_window.focus_force()

# Main application window
root = TkinterDnD.Tk()
root.title("PDF Spell& Grammar Checker")
root.geometry("1200x800")

# Set the appearance mode and default color theme
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

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
settings_menu.add_command(label="Parsing Einstellungen", command=open_settings_window)

help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Hilfe", menu=help_menu)

# Frame for uploading file
upload_frame = ctk.CTkFrame(root)
upload_frame.pack(pady=10, fill='x', padx=20)

upload_label = ctk.CTkLabel(upload_frame, text="Datei zur Rechtschreibprüfung hierhin ziehen oder Datei hinzufügen", font=('Arial', 14))
upload_label.pack(side='left', padx=5)

upload_button = ctk.CTkButton(upload_frame, text="Datei auswählen...", font=('Arial', 14), command=upload_file)
upload_button.pack(side='left', pady=10, padx=10)

process_button = ctk.CTkButton(upload_frame, text="Datei verarbeiten", font=('Arial', 14), command=process_file)
process_button.pack(side='right', pady=10, padx=10)

file_label = ctk.CTkLabel(upload_frame, text="No file selected", font=('Arial', 14))
file_label.pack(side='left', padx=5)

# Drag-and-drop field
dnd_label = ctk.CTkLabel(upload_frame, text="Datei per Drag and Drop hier...", width=550, height=100, corner_radius=10)
dnd_label.pack(pady=10, fill='x')
dnd_label.drop_target_register(DND_FILES)
dnd_label.dnd_bind('<<Drop>>', lambda event: process_file(event.data))

# Frame for PDF content
content_frame = ctk.CTkFrame(root)
content_frame.pack(pady=10, fill='both', expand=True, padx=20)

content_label = ctk.CTkLabel(content_frame, text="PDF Inhalt", font=('Arial', 14))
content_label.pack(anchor='w', pady=5, padx=10)

pdf_content_textbox = Text(content_frame, height=10, wrap='word', borderwidth=1, relief='solid')
pdf_content_textbox.pack(padx=5, pady=5, fill='both', expand=True)

check_button = ctk.CTkButton(content_frame, text="Überprüfen", font=('Arial', 14), command=check_spelling)
check_button.pack(pady=5)

except_word_button = ctk.CTkButton(content_frame, text="Wörter entfernen", font=('Arial', 14), command=open_except_words)
except_word_button.pack(side="right", pady=5)

# Frame for spell check results
result_frame = ctk.CTkScrollableFrame(root)
result_frame.pack(pady=20, fill='x', padx=20)

# Here you would dynamically add labels for each spelling mistake found
result_label_1 = ctk.CTkLabel(result_frame, text="...lorem ipsum...")
result_label_1.pack(anchor='w')
result_label_2 = ctk.CTkLabel(result_frame, text="...lorem ipsum...")
result_label_2.pack(anchor='w')
result_label_3 = ctk.CTkLabel(result_frame, text="...lorem ipsum...")
result_label_3.pack(anchor='w')

# Start the application
root.mainloop()
