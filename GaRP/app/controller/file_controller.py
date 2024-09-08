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

from tkinter import filedialog  # Importiere das Modul zur Dateiauswahl
import os  # Importiere das os-Modul für Dateipfade

# Importiere die Funktionen zur Textextraktion aus PDF-Dateien
from integrations.pdfminer_text_extraction import extract_text_from_pdf_pagewise, extract_text_from_pdf_structured

class FileController:
    """
    Diese Klasse steuert den Dateiupload und die Verarbeitung von PDF-Dateien.
    Sie interagiert mit den GUI-Komponenten des Hauptfensters und dem PDF-Parsing.
    """

    def __init__(self, main_window, settings):
        """
        Konstruktor für den FileController.

        :param main_window: Referenz auf das Hauptfenster der Anwendung, um auf die GUI-Elemente zuzugreifen.
        :param settings: Die Anwendungseinstellungen, die das Parsing steuern (z. B. Parsing-Modus und Seitenbereich).
        """
        self.main_window = main_window
        self.settings = settings  # Zugriff auf die Einstellungen der Anwendung

    def upload_file(self):
        """
        Öffnet einen Dateidialog, um eine PDF-Datei hochzuladen, und aktualisiert das Hauptfenster mit dem Dateinamen.
        """
        # Leere die aktuelle Auswahl und den Inhalt der Fehlerliste (error_tree)
        self.main_window.error_tree.selection_clear()
        for item in self.main_window.error_tree.get_children():
            self.main_window.error_tree.delete(item)
        self.main_window.error_list = []  # Leere die Liste der Fehler

        try:
            # Leere die Liste der Ausnahmewörter (except_words)
            self.except_words = []

            # Aktualisiere die Liste der Ausnahmewörter im entsprechenden Fenster, falls es geöffnet ist
            if hasattr(self, 'except_words_window'):
                self.except_words_window.update_except_words_list()

            # Öffne den Dateiauswahldialog und erlaube dem Benutzer, eine PDF-Datei auszuwählen
            self.file_path = filedialog.askopenfilename(filetypes=[("PDF-Dateien", "*.pdf"), ("Alle Dateien", "*.*")])
            
            # Wenn eine Datei ausgewählt wurde, aktualisiere das Label im Hauptfenster mit dem Dateinamen
            if self.file_path:
                self.main_window.file_label.configure(text=f"{os.path.basename(self.file_path)}")
        except Exception as e:
            # Zeige eine Fehlermeldung an, wenn beim Hochladen der Datei ein Fehler auftritt
            self.main_window.error_window.show_error_message("Fehler beim Hochladen der Datei", str(e))

    def process_file(self):
        """
        Verarbeitet die hochgeladene PDF-Datei und extrahiert den Text basierend auf den gewählten Einstellungen.
        Der extrahierte Text wird im Hauptfenster angezeigt.
        """
        # Leere die aktuelle Auswahl und den Inhalt der Fehlerliste (error_tree)
        self.main_window.error_tree.selection_clear()
        for item in self.main_window.error_tree.get_children():
            self.main_window.error_tree.delete(item)
        self.main_window.error_list = []  # Leere die Liste der Fehler

        try:
            # Wähle die Parsing-Methode basierend auf der Einstellung (structured oder pagewise)
            if self.settings.parsing_basic_setting == "structured":
                # Führe das strukturierte Parsing der PDF-Datei durch
                extracted_text = extract_text_from_pdf_structured(
                    self.file_path,
                    starting_page=self.settings.starting_page,
                    ending_page=self.settings.ending_page,
                    check_fontname=self.settings.check_fontname,
                    first_lines_to_skip=self.settings.first_lines_to_skip,
                    last_lines_to_skip=self.settings.last_lines_to_skip
                )
            elif self.settings.parsing_basic_setting == "pagewise":
                # Führe das seitenweise Parsing der PDF-Datei durch
                extracted_text = extract_text_from_pdf_pagewise(
                    self.file_path,
                    starting_page=self.settings.starting_page,
                    ending_page=self.settings.ending_page,
                    first_lines_to_skip=self.settings.first_lines_to_skip,
                    last_lines_to_skip=self.settings.last_lines_to_skip
                )
            else:
                raise ValueError("Ungültige Parsing-Grundeinstellung")  # Fehler bei einer ungültigen Einstellung
                
            # Lösche den Inhalt des Textfeldes im Hauptfenster und füge den extrahierten Text ein
            self.main_window.pdf_content_textbox.delete("1.0", "end")
            self.main_window.pdf_content_textbox.insert("1.0", extracted_text)
            self.main_window.pdf_content_textbox.config(state="normal")  # Setze den Zustand des Textfeldes auf editierbar
        except Exception as e:
            # Zeige eine Fehlermeldung an, wenn beim Verarbeiten der Datei ein Fehler auftritt
            self.main_window.error_window.show_error_message("Fehler beim Verarbeiten der Datei", str(e))
