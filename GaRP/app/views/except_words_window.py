"""Copyright (C) 2024 Gantert, Schneider, Sewald

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/> """

import customtkinter as ctk  
from controller.except_words_controller import ExceptWordsController  

class ExceptWordsWindow:
    """
    Diese Klasse erstellt ein Fenster zur Verwaltung von Wörtern, die von der Rechtschreibprüfung oder Verarbeitung ausgeschlossen werden sollen.
    """

    def __init__(self, root, main_window):
        """
        Konstruktor für das ExceptWordsWindow.
        
        :param root: Das übergeordnete Tkinter-Hauptfenster.
        :param main_window: Referenz auf das Hauptfenster, um Einstellungen und Daten zu aktualisieren.
        """
        self.root = root
        self.main_window = main_window
        # Initialisiere den Controller, der für die Bearbeitung der Ausnahmewörter zuständig ist
        self.except_words_controller = ExceptWordsController(self)
        
        # Erstelle das Toplevel-Fenster, das auf dem Hauptfenster basiert
        self.except_words_window = ctk.CTkToplevel(self.root)
        self.except_words_window.title("Wörter entfernen")  # Setze den Fenstertitel
        self.except_words_window.geometry("600x400")  # Setze die Fenstergröße

        # Label für das Eingabefeld zur Eingabe von Ausnahmewörtern
        self.except_words_label = ctk.CTkLabel(self.except_words_window, text="Zu entfernendes Wort:")
        self.except_words_label.grid(row=0, column=0, columnspan=1, padx=5, pady=5)

        # Eingabefeld für die Eingabe des zu entfernenden Wortes
        self.except_words_entry = ctk.CTkEntry(self.except_words_window)
        self.except_words_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        # Binde die Eingabetaste ("Return") an die Methode, um ein Wort hinzuzufügen
        self.except_words_entry.bind("<Return>", lambda event: self.except_words_controller.add_except_word())

        # Frame, um die hinzugefügten Ausnahmewörter anzuzeigen (wird später gefüllt)
        self.words_frame = ctk.CTkFrame(self.except_words_window)
        self.words_frame.grid(row=1, column=0, sticky="nsw", padx=5, pady=5)

        # Button, um das eingegebene Wort zur Liste der Ausnahmewörter hinzuzufügen
        self.process_button = ctk.CTkButton(self.except_words_window, text="Wort zur Liste hinzufügen", command=self.except_words_controller.add_except_word)
        self.process_button.grid(row=0, column=3, columnspan=2, padx=5, pady=20)

        # Button, um die Ausnahmewörter zu speichern und die Datei erneut zu verarbeiten
        self.save_button = ctk.CTkButton(self.except_words_window, text="Speichern & Datei neu verarbeiten", command=self.except_words_controller.execute_except_words)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

        # Button, um Anführungszeichen aus dem Text zu entfernen
        self.except_quotation_marks_button = ctk.CTkButton(self.except_words_window, text="Anführungszeichen entfernen", command=self.except_words_controller.except_quotation_marks)
        self.except_quotation_marks_button.grid(row=4, column=2, columnspan=3, padx=5, pady=20)

        # Aktualisiere die Liste der Ausnahmewörter beim Öffnen des Fensters
        self.except_words_controller.update_except_words_list()

        # Setze das Fenster in den Vordergrund
        self.except_words_window.attributes("-topmost", True)

