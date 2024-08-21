import customtkinter as ctk
from tkinter import filedialog, Menu, Text
import sys
import os

from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from GaRP.parser.pdfminer_text_extraction import extract_text_from_pdf_structured

settings = {
    "starting_page": 1,
    "ending_page": 100,
    "check_fontname": False,
    "first_lines_to_skip": 0,
    "last_lines_to_skip": 0
}

words_to_except = []
file_path = None


class ExceptWordsWindow:
    def __init__(self, root):
        self.root = root
        self.words_to_except = []
        self.except_words_window = ctk.CTkToplevel(self.root)
        self.except_words_window.title("Wörter entfernen")
        self.except_words_window.geometry("600x400")

        self.except_words_label = ctk.CTkLabel(self.except_words_window, text="Zu entfernendes Wort:")
        self.except_words_label.pack(padx=5, pady=5)

        self.except_words_entry = ctk.CTkEntry(self.except_words_window)
        self.except_words_entry.pack(padx=5, pady=5)

        self.save_button = ctk.CTkButton(self.except_words_window, text="Speichern", command=self.except_words_list)
        self.save_button.pack(side="bottom", padx=5, pady=20)

        self.process_button = ctk.CTkButton(self.except_words_window, text="Wörter entferen",command=self.except_words_list)
        self.process_button.pack(side="bottom", padx=5, pady=20)

        self.words_frame = ctk.CTkFrame(self.except_words_window)
        self.words_frame.pack(fill='both', expand=True, padx=5, pady=5)

        self.update_except_words_list()

        self.except_words_window.lift()
        self.except_words_window.focus_force()

    def except_words_list(self):
        word_to_except = self.except_words_entry.get()
        if word_to_except:
            self.words_to_except.append(word_to_except)
            self.except_words_entry.delete(0, 'end')
            self.update_except_words_list()

    def update_except_words_list(self):
        for widget in self.words_frame.winfo_children():
            widget.destroy()

        for word in self.words_to_except:
            ctk.CTkLabel(self.words_frame, text=word).pack(anchor='w')


class SettingsWindow:
    def __init__(self, root):
        self.root = root
        self.settings_window = ctk.CTkToplevel(self.root)
        self.settings_window.title("Einstellungen")
        self.settings_window.geometry("400x600")

        self.starting_page_label = ctk.CTkLabel(self.settings_window, text="Startseite:")
        self.starting_page_label.grid(row=0, column=0, padx=5, pady=5)

        self.starting_page_entry = ctk.CTkEntry(self.settings_window)
        self.starting_page_entry.insert(0, settings["starting_page"])
        self.starting_page_entry.grid(row=0, column=1, padx=5, pady=5)

        self.ending_page_label = ctk.CTkLabel(self.settings_window, text="Endseite:")
        self.ending_page_label.pack(padx=5, pady=5)

        self.ending_page_entry = ctk.CTkEntry(self.settings_window)
        self.ending_page_entry.insert(0, settings["ending_page"])
        self.ending_page_entry.pack(padx=5, pady=5)

        self.check_fontname_label = ctk.CTkLabel(self.settings_window, text="Schriftart prüfen:")
        self.check_fontname_label.pack(padx=5, pady=5)

        self.check_fontname_var = ctk.BooleanVar(value=settings["check_fontname"])
        self.check_fontname_checkbox = ctk.CTkCheckBox(self.settings_window, text="", variable=self.check_fontname_var)
        self.check_fontname_checkbox.pack(padx=5, pady=5)

        self.first_lines_to_skip_label = ctk.CTkLabel(self.settings_window, text="Erste zu überspringende Zeilen:")
        self.first_lines_to_skip_label.pack(padx=5, pady=5)

        self.first_lines_to_skip_entry = ctk.CTkEntry(self.settings_window)
        self.first_lines_to_skip_entry.insert(0, settings["first_lines_to_skip"])
        self.first_lines_to_skip_entry.pack(padx=5, pady=5)

        self.last_lines_to_skip_label = ctk.CTkLabel(self.settings_window, text="Letzte zu überspringende Zeilen:")
        self.last_lines_to_skip_label.pack(padx=5, pady=5)

        self.last_lines_to_skip_entry = ctk.CTkEntry(self.settings_window)
        self.last_lines_to_skip_entry.insert(0, settings["last_lines_to_skip"])
        self.last_lines_to_skip_entry.pack(padx=5, pady=5)

        self.save_button = ctk.CTkButton(self.settings_window, text="Speichern", command=self.save_settings)
        self.save_button.pack(side="bottom", padx=5, pady=20)

        self.settings_window.lift()
        self.settings_window.focus_force()

    def save_settings(self):
        settings["starting_page"] = int(self.starting_page_entry.get())
        settings["ending_page"] = int(self.ending_page_entry.get())
        settings["check_fontname"] = self.check_fontname_var.get()
        settings["first_lines_to_skip"] = int(self.first_lines_to_skip_entry.get())
        settings["last_lines_to_skip"] = int(self.last_lines_to_skip_entry.get())
        self.settings_window.destroy()


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.file_path = None
        self.create_widgets()

    def create_widgets(self):
        self.root.title("PDF Rechtschreib- & Grammatikprüfung")
        self.root.geometry("1200x800")

        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("green")

        menu = Menu(self.root)
        self.root.config(menu=menu)

        file_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Datei", menu=file_menu)
        file_menu.add_command(label="Öffnen", command=self.upload_file)
        file_menu.add_separator()
        file_menu.add_command(label="Schließen", command=self.root.quit)

        settings_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Einstellungen", menu=settings_menu)
        settings_menu.add_command(label="Parsing Einstellungen", command=self.open_settings_window)

        help_menu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Hilfe", menu=help_menu)

        self.upload_frame = ctk.CTkFrame(self.root)
        self.upload_frame.pack(pady=10, fill='x', padx=20)

        upload_label = ctk.CTkLabel(self.upload_frame, text="Datei zur Rechtschreibprüfung hinzufügen", font=('Arial', 14))
        upload_label.pack(side='left', padx=5)

        upload_button = ctk.CTkButton(self.upload_frame, text="Datei auswählen...", font=('Arial', 14), command=self.upload_file)
        upload_button.pack(side='left', pady=10, padx=10)

        process_button = ctk.CTkButton(self.upload_frame, text="Datei verarbeiten", font=('Arial', 14), command=self.process_file)
        process_button.pack(side='right', pady=10, padx=10)

        self.file_label = ctk.CTkLabel(self.upload_frame, text="Keine Datei ausgewählt", font=('Arial', 14))
        self.file_label.pack(side='left', padx=5)

        content_frame = ctk.CTkFrame(self.root)
        content_frame.pack(pady=10, fill='both', expand=True, padx=20)

        content_label = ctk.CTkLabel(content_frame, text="PDF Inhalt", font=('Arial', 14))
        content_label.pack(anchor='w', pady=5, padx=10)

        self.pdf_content_textbox = Text(content_frame, height=10, wrap='word', borderwidth=1, relief='solid')
        self.pdf_content_textbox.pack(padx=5, pady=5, fill='both', expand=True)

        check_button = ctk.CTkButton(content_frame, text="Überprüfen", font=('Arial', 14), command=self.check_spelling)
        check_button.pack(pady=5)

        except_word_button = ctk.CTkButton(content_frame, text="Wörter entfernen", font=('Arial', 14), command=self.open_except_words)
        except_word_button.pack(side="right", pady=5)

        result_frame = ctk.CTkScrollableFrame(self.root)
        result_frame.pack(pady=20, fill='x', padx=20)

        result_label_1 = ctk.CTkLabel(result_frame, text="...lorem ipsum...")
        result_label_1.pack(anchor='w')
        result_label_2 = ctk.CTkLabel(result_frame, text="...lorem ipsum...")
        result_label_2.pack(anchor='w')
        result_label_3 = ctk.CTkLabel(result_frame, text="...lorem ipsum...")
        result_label_3.pack(anchor='w')

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF-Dateien", "*.pdf"), ("Alle Dateien", "*.*")])
        if self.file_path:
            self.file_label.configure(text=f"Datei: {self.file_path}")

    def process_file(self):
        if self.file_path:
            extracted_text = extract_text_from_pdf_structured(
                self.file_path,
                starting_page=settings["starting_page"],
                ending_page=settings["ending_page"],
                check_fontname=settings["check_fontname"],
                first_lines_to_skip=settings["first_lines_to_skip"],
                last_lines_to_skip=settings["last_lines_to_skip"]
            )
            self.pdf_content_textbox.delete("1.0", "end")
            self.pdf_content_textbox.insert("1.0", extracted_text)
        else:
            error_window = ctk.CTkToplevel(self.root)
            error_window.title("Fehler")
            error_window.geometry("200x100")
            ctk.CTkLabel(error_window, text="Keine Datei ausgewählt!").pack(padx=5, pady=5)

    def check_spelling(self):
        gateway.entry_point._methods.ch
        pass

    def open_settings_window(self):
        SettingsWindow(self.root)

    def open_except_words(self):
        ExceptWordsWindow(self.root)


if __name__ == "__main__":
    root = ctk.CTk()
    app = MainApplication(root)
    root.mainloop()