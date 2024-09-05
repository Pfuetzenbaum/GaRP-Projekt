import customtkinter as ctk
import tkinter as tk
from tkinter import Menu, Text, ttk

from controller.file_controller import FileController
from controller.spellcheck_controller import SpellcheckController
from controller.error_export_controller import ErrorExportController

from settings.settings import Settings
from views.parser_settings_window import ParserSettingsWindow
from views.languagetool_settings_window import LanguageToolSettingsWindow
from views.except_words_window import ExceptWordsWindow
from integrations.dictionary_manager_gateway import DictionaryManagerGateway


class MainWindow:
    def __init__(self, root, error_window):
        self.root = root
        self.error_window = error_window

        self.settings = Settings()        
        self.dictionary_manager_gateway = DictionaryManagerGateway(self.settings)   
        self.spellcheck_controller = SpellcheckController(self, self.dictionary_manager_gateway)
        self.file_controller = FileController(self, self.settings)
        self.error_export_controller = ErrorExportController(self)

        self.error_list = []
        self.result_labels = []
        self.except_words = []
        self.extracted_text = ""

        self.create_widgets()

    def create_widgets(self):
        try:
            self.root.title("GaRP - das Tool zur Grammatik- und Rechtschreibprüfung von PDF-Dateien")
            self.root.geometry("1200x800")

            ctk.set_appearance_mode("system")
            ctk.set_default_color_theme("green")

            menu = Menu(self.root)
            self.root.config(menu=menu)

            file_menu = Menu(menu, tearoff=0)
            menu.add_cascade(label="Datei", menu=file_menu)
            file_menu.add_command(label="Öffnen", command=self.file_controller.upload_file)
            file_menu.add_separator()
            file_menu.add_command(label="Schließen", command=self.root.quit)

            settings_menu = Menu(menu, tearoff=0)
            menu.add_cascade(label="Einstellungen", menu=settings_menu)
            settings_menu.add_command(label="PDF-Parsing Einstellungen", command=self.open_parser_settings_window)
            settings_menu.add_command(label="Language Tool Einstellungen", command=self.open_lt_settings_window)

            help_menu = Menu(menu, tearoff=0)
            menu.add_cascade(label="Hilfe", menu=help_menu)

            self.left_frame = ctk.CTkFrame(self.root)
            self.left_frame.place(relwidth=0.7, relheight=1, relx=0, rely=0)
            
            self.right_frame = ctk.CTkFrame(self.root)
            self.right_frame.place(relwidth=0.3, relheight=1, relx=0.7, rely=0)
            
            self.upload_frame = ctk.CTkFrame(self.left_frame)
            self.upload_frame.pack(fill="x", pady=10, padx=20)

            upload_label = ctk.CTkLabel(self.upload_frame, text="PDF-Datei zur Überprüfung auswählen", font=('Arial', 14))
            upload_label.pack(side='left', padx=5)

            upload_button = ctk.CTkButton(self.upload_frame, text="Datei auswählen...", font=('Arial', 14), command=self.file_controller.upload_file)
            upload_button.pack(side='left', pady=10, padx=10)

            process_button = ctk.CTkButton(self.upload_frame, text="Datei verarbeiten", font=('Arial', 14), command=self.file_controller.process_file)
            process_button.pack(side='right', pady=10, padx=10)

            self.file_label = ctk.CTkLabel(self.upload_frame, text="Keine Datei ausgewählt", font=('Arial', 14))
            self.file_label.pack(side='left', padx=5)

            content_frame = ctk.CTkFrame(self.left_frame)
            content_frame.pack(pady=10, fill='both', expand=True, padx=20)

            content_label = ctk.CTkLabel(content_frame, text="PDF Inhalt", font=('Arial', 14))
            content_label.pack(anchor='w', pady=5, padx=10)

            self.pdf_content_textbox = Text(content_frame, height=10, wrap='word', borderwidth=1, relief='solid')
            self.pdf_content_textbox.pack(padx=5, pady=5, fill='both', expand=True)

            check_button = ctk.CTkButton(content_frame, text="Überprüfen", font=('Arial', 14), command=self.spellcheck_controller.check_spelling)
            check_button.pack(pady=5)

            except_word_button = ctk.CTkButton(content_frame, text="Zeichen entfernen", font=('Arial', 14), command=self.open_except_words)
            except_word_button.pack(side="right",padx=5, pady=5)

            self.error_tree = ttk.Treeview(self.right_frame)
            self.error_tree['columns'] = ('Fehler', 'Beschreibung')

            self.error_tree.column("#0", width=0, stretch=tk.NO)
            self.error_tree.column("Fehler", anchor=tk.W, width=150)
            self.error_tree.column("Beschreibung", anchor=tk.W, width=400)

            self.error_tree.heading("#0", text="", anchor=tk.W)
            self.error_tree.heading("Fehler", text="Fehler", anchor=tk.W)
            self.error_tree.heading("Beschreibung", text="Beschreibung", anchor=tk.W)

            self.error_tree.pack(fill="both", expand=True, padx=10, pady=10)

            export_button = ctk.CTkButton(self.right_frame, text="Fehler exportieren", font=('Arial', 14), command=self.error_export_controller.export_errors)
            export_button.pack(pady=10)

            self.root.state("zoomed")

        except Exception as e:
            self.error_window.show_error_message("Fehler beim Erstellen der Oberfläche", str(e))
    
    def open_parser_settings_window(self):
        ParserSettingsWindow(self.root, self)
    
    def open_lt_settings_window(self):
        LanguageToolSettingsWindow(self.root, self)

    def open_except_words(self):
        ExceptWordsWindow(self.root, self)