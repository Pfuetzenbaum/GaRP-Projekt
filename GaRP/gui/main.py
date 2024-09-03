import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, Menu, Text, Listbox, ttk
import sys
import os


from py4j.java_gateway import JavaGateway, GatewayParameters
from settings import Settings
from except_words_window import ExceptWordsWindow
from parser_settings_window import ParserSettingsWindow
from languagetool_settings_window import LanguageToolSettingsWindow

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from GaRP.parser.pdfminer_text_extraction import extract_text_from_pdf_structured, extract_text_from_pdf_pagewise

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25333))

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.file_path = None
        self.create_widgets()
        self.result_labels = []
        self.settings = Settings()
        self.except_words = []
        self.extracted_text = ""
        self.dictionary_manager_german = gateway.entry_point.getDictionaryManagerGerman()
        self.dictionary_manager_english = gateway.entry_point.getDictionaryManagerEnglish()

        self.dictionary_manager = self.get_dictionary_manager(self.settings.language)

    def get_dictionary_manager(self, language):
        if language == "Deutsch":
            return self.dictionary_manager_german
        elif language == "Englisch":
            return self.dictionary_manager_english
        else:
            raise ValueError("Ungültige Sprache")





    def create_widgets(self):
        try:
            self.root.title("PDF Rechtschreib- & Grammatikprüfung")
            #self.root.wm_attributes("-top", True)

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
            settings_menu.add_command(label="PDF-Parsing Einstellungen", command=self.open_parser_settings_window)
            settings_menu.add_command(label="Language Tool Einstellungen", command=self.open_lt_settings_window)

            help_menu = Menu(menu, tearoff=0)
            menu.add_cascade(label="Hilfe", menu=help_menu)

            self.left_frame = ctk.CTkFrame(self.root)
            self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

            self.right_frame = ctk.CTkFrame(self.root)
            self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

            self.upload_frame = ctk.CTkFrame(self.left_frame)
            self.upload_frame.pack(fill="x", pady=10, padx=20)

            upload_label = ctk.CTkLabel(self.upload_frame, text="Datei zur Rechtschreibprüfung hinzufügen", font=('Arial', 14))
            upload_label.pack(side='left', padx=5)

            upload_button = ctk.CTkButton(self.upload_frame, text="Datei auswählen...", font=('Arial', 14), command=self.upload_file)
            upload_button.pack(side='left', pady=10, padx=10)

            process_button = ctk.CTkButton(self.upload_frame, text="Datei verarbeiten", font=('Arial', 14), command=self.process_file)
            process_button.pack(side='right', pady=10, padx=10)

            self.file_label = ctk.CTkLabel(self.upload_frame, text="Keine Datei ausgewählt", font=('Arial', 14))
            self.file_label.pack(side='left', padx=5)

            content_frame = ctk.CTkFrame(self.left_frame)
            content_frame.pack(pady=10, fill='both', expand=True, padx=20)

            content_label = ctk.CTkLabel(content_frame, text="PDF Inhalt", font=('Arial', 14))
            content_label.pack(anchor='w', pady=5, padx=10)

            self.pdf_content_textbox = Text(content_frame, height=10, wrap='word', borderwidth=1, relief='solid')
            self.pdf_content_textbox.pack(padx=5, pady=5, fill='both', expand=True)

            check_button = ctk.CTkButton(content_frame, text="Überprüfen", font=('Arial', 14), command=self.check_spelling)
            check_button.pack(pady=5)

            except_word_button = ctk.CTkButton(content_frame, text="Wörter entfernen", font=('Arial', 14), command=self.open_except_words)
            except_word_button.pack(side="right", pady=5)

            #self.error_listbox = Listbox(self.right_frame)
            #self.error_listbox.pack(fill="both", expand=True, padx=10, pady=10)
            #self.error_listbox.bind('<<ListboxSelect>>', self.show_spellcheck_details)

            self.error_tree = ttk.Treeview(self.right_frame)
            self.error_tree['columns'] = ('Fehler', 'Beschreibung')

            self.error_tree.column("#0", width=0, stretch=tk.NO)
            self.error_tree.column("Fehler", anchor=tk.W, width=150)
            self.error_tree.column("Beschreibung", anchor=tk.W, width=400)

            self.error_tree.heading("#0", text="", anchor=tk.W)
            self.error_tree.heading("Fehler", text="Fehler", anchor=tk.W)
            self.error_tree.heading("Beschreibung", text="Beschreibung", anchor=tk.W)

            self.error_tree.pack(fill="both", expand=True, padx=10, pady=10)

            export_button = ctk.CTkButton(self.right_frame, text="Fehler exportieren", font=('Arial', 14), command=self.export_errors)
            export_button.pack(pady=10)

        except Exception as e:
            self.show_error_message("Fehler beim Erstellen der Oberfläche", str(e))

    def upload_file(self):

        # Leere die error_tree
        self.error_tree.selection_clear()
        for item in self.error_tree.get_children():
            self.error_tree.delete(item)

        try:
            # Leere die except_words Liste
            self.except_words = []
                
            # Aktualisiere die except_words Liste in der Oberfläche
            if hasattr(self, 'except_words_window'):
                self.except_words_window.update_except_words_list()

            self.file_path = filedialog.askopenfilename(filetypes=[("PDF-Dateien", "*.pdf"), ("Alle Dateien", "*.*")])
            if self.file_path:
                self.file_label.configure(text=f"Datei: {self.file_path}")
        except Exception as e:
            self.show_error_message("Fehler beim Hochladen der Datei", str(e))

    def process_file(self):

        # Leere die error_tree
        self.error_tree.selection_clear()
        for item in self.error_tree.get_children():
            self.error_tree.delete(item)

        try:
            if self.file_path:
                                
                if self.settings.parsing_basic_setting == "structured":
                    extracted_text = extract_text_from_pdf_structured(
                        self.file_path,
                        starting_page=self.settings.starting_page,
                        ending_page=self.settings.ending_page,
                        check_fontname=self.settings.check_fontname,
                        first_lines_to_skip=self.settings.first_lines_to_skip,
                        last_lines_to_skip=self.settings.last_lines_to_skip
                    )
                elif self.settings.parsing_basic_setting == "pagewise":
                    extracted_text = extract_text_from_pdf_pagewise(
                        self.file_path,
                        starting_page=self.settings.starting_page,
                        ending_page=self.settings.ending_page,
                        first_lines_to_skip=self.settings.first_lines_to_skip,
                        last_lines_to_skip=self.settings.last_lines_to_skip
                    )
                else:
                    raise ValueError("Ungültige Parsing-Grundeinstellung")
                
                self.pdf_content_textbox.delete("1.0", "end")
                self.pdf_content_textbox.insert("1.0", extracted_text)
                self.pdf_content_textbox.config(state="normal")
            else:
                error_window = ctk.CTkToplevel(self.root)
                error_window.title("Fehler")
                error_window.geometry("200x100")
                ctk.CTkLabel(error_window, text="Keine Datei ausgewählt!").pack(padx=5, pady=5)
        except Exception as e:
            self.show_error_message("Fehler beim Verarbeiten der Datei", str(e))

    def check_spelling(self):

        #self.error_listbox.delete(0, 'end')

        # Leere die error_tree
        self.error_tree.selection_clear()
        for item in self.error_tree.get_children():
            self.error_tree.delete(item)

        #Alle Tags entfernen
        for tag in self.pdf_content_textbox.tag_names():
            self.pdf_content_textbox.tag_remove(tag, "1.0", "end")

        try:
            extracted_text = self.pdf_content_textbox.get("1.0", "end-1c")

            word_list = self.dictionary_manager.checkTextFiltered(extracted_text)

            self.error_list = []

            # Füge die gefundenen Fehler zur Liste hinzu
            for word in word_list:

                affected_part = word.getAffectedPart()
                short_message = word.getShortMessage()
                long_message = word.getLongMessage()
                from_pos = word.getFromPos()
                to_pos = word.getToPos()

                # Füge den Fehler zur error_tree hinzu
                self.error_tree.insert('', 'end', values=(affected_part, long_message))
                self.error_list.append(word)

                # Binde die Auswahl-Events der error_tree neu, um sicherzustellen, dass sie korrekt funktionieren
                self.error_tree.bind('<<TreeviewSelect>>', self.show_spellcheck_details)
                           
                # Füge den Fehler zur Listbox hinzu (nur Kurzmeldung zur Übersicht)
                #self.error_listbox.insert('end', f"{affected_part} - {long_message}")
                #self.error_list.append(word)

                # Binde die Auswahl-Events der Listbox neu, um sicherzustellen, dass sie korrekt funktionieren
                #self.error_listbox.bind('<<ListboxSelect>>', self.show_spellcheck_details)

                # Markiere den Fehler im Textfeld
                self.highlight_error(from_pos, to_pos, short_message)
                
        except Exception as e:
            self.show_error_message("Fehler beim Überprüfen der Rechtschreibung", str(e))
        
    
    def highlight_error(self, from_pos, to_pos, short_message):

        # Finden Sie die Zeile und Spalte des Fehlers im Textfeld
        lines = self.pdf_content_textbox.get("1.0", "end-1c").split("\n")
        line_length = 0
        line_number = 1
        for line in lines:
            if line_length + len(line) >= from_pos:
                break
            line_length += len(line) + 1
            line_number += 1

        # Berechnen Sie die Spalte des Fehlers in der Zeile
        column = from_pos - line_length

         # Markieren Sie den Fehler im Textfeld
        self.pdf_content_textbox.tag_config("spelling_error", background="#FF0000") #Rot
        self.pdf_content_textbox.tag_config("other_error", background="#FFA07A") #Orange

        if short_message == 'Rechtschreibfehler' or short_message == 'Spelling mistake':

            self.pdf_content_textbox.tag_remove("spelling_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            self.pdf_content_textbox.tag_add("spelling_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            
        else:

            self.pdf_content_textbox.tag_remove("other_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            self.pdf_content_textbox.tag_add("other_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            

    def show_spellcheck_details(self, event):
        try:
            selected_items = self.error_tree.selection()
            if len(selected_items) > 0:
                selected_item = self.error_tree.selection()[0]
                affected_part = self.error_tree.item(selected_item, 'values')[0]

                # Finde den entsprechenden Fehler in der error_list
                for error in self.error_list:
                    if error.getAffectedPart() == affected_part:
                        selected_error = error
                        break

                # Neues Fenster für detaillierte Fehlerbeschreibung
                spelling_error_window = ctk.CTkToplevel(self.root)
                spelling_error_window.title("Fehlerdetails")
                spelling_error_window.geometry("400x400")
                spelling_error_window.attributes("-topmost", True)  # Setze das Fenster auf die oberste Ebene

                error_details = ctk.CTkTextbox(spelling_error_window, wrap='word', border_width=1)
                error_details.insert("1.0", f"Verbesserung: {selected_error.getImprovement()}\n"
                                        f"Betroffener Teil: {affected_part}\n"
                                        f"Kurzmeldung: {selected_error.getShortMessage()}\n"
                                        f"Lange Meldung: {selected_error.getLongMessage()}\n"
                                        f"betroffener Satz: {selected_error.getSentence()}\n"
                                        f"From Pos: {selected_error.getFromPos()}\n"
                                        f"To Pos: {selected_error.getToPos()}")
                error_details.configure(state="disabled")
                error_details.pack(fill="both", expand=True, padx=10, pady=10)

                add_word_button = ctk.CTkButton(spelling_error_window, text="Dauerhaft hinzufügen", font=('Arial', 14),
                                                command=lambda: self.add_word_and_disable_button(add_word_button, affected_part))
                add_word_button.pack(padx=10, pady=10)

                add_word_temporary_button = ctk.CTkButton(spelling_error_window, text="Für dieses Session ignorieren", font=('Arial', 14),
                                                        command=lambda: self.dictionary_manager.ignoreWordInSession(affected_part))
                add_word_temporary_button.pack(padx=10, pady=10)

        except Exception as e:
            self.show_error_message("Fehler bei der Anzeige von Fehlerdetails", str(e))

    def add_word_and_disable_button(self, button, word):
        self.dictionary_manager.addWord(word)
        button.configure(state="disabled")

    def show_error_message(self, title, message):
        error_window = ctk.CTkToplevel(self.root)
        error_window.title(title)
        error_window.geometry("400x200")
        error_window.attributes("-topmost", True)  # Setze das Fenster auf die oberste Ebene

        error_label = ctk.CTkLabel(error_window, text=message, wraplength=380)
        error_label.pack(padx=10, pady=10)
        
    def export_errors(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    for error in self.error_list:
                        f.write(f"{error.getAffectedPart()},{error.getShortMessage()},{error.getLongMessage()},{error.getSentence()}\n")
                self.show_error_message("Erfolgreich exportiert", "Die Fehler wurden erfolgreich in eine Textdatei exportiert.")
        except Exception as e:
            self.show_error_message("Fehler beim Exportieren", str(e))

    def open_parser_settings_window(self):
        ParserSettingsWindow(self.root, self)
    
    def open_lt_settings_window(self):
        LanguageToolSettingsWindow(self.root, self)

    def open_except_words(self):
        ExceptWordsWindow(self.root, self)



if __name__ == "__main__":
    root = ctk.CTk()
    app = MainApplication(root)
    root.mainloop()