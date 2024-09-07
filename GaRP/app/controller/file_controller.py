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

from tkinter import filedialog
import os

from integrations.pdfminer_text_extraction import extract_text_from_pdf_pagewise, extract_text_from_pdf_structured

class FileController:
    def __init__(self, main_window, settings):
        self.main_window = main_window
        self.settings = settings

    def upload_file(self):

        # Leere die error_tree
        self.main_window.error_tree.selection_clear()
        for item in self.main_window.error_tree.get_children():
            self.main_window.error_tree.delete(item)
        self.main_window.error_list = []

        try:
            # Leere die except_words Liste
            self.except_words = []
                
            # Aktualisiere die except_words Liste in der Oberfläche
            if hasattr(self, 'except_words_window'):
                self.except_words_window.update_except_words_list()

            self.file_path = filedialog.askopenfilename(filetypes=[("PDF-Dateien", "*.pdf"), ("Alle Dateien", "*.*")])
            if self.file_path:
                self.main_window.file_label.configure(text=f"{os.path.basename(self.file_path)}")
        except Exception as e:
            self.main_window.error_window.show_error_message("Fehler beim Hochladen der Datei", str(e))

    def process_file(self):

        # Leere die error_tree
        self.main_window.error_tree.selection_clear()
        for item in self.main_window.error_tree.get_children():
            self.main_window.error_tree.delete(item)
        self.main_window.error_list = []

        try:
                              
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
                
            self.main_window.pdf_content_textbox.delete("1.0", "end")
            self.main_window.pdf_content_textbox.insert("1.0", extracted_text)
            self.main_window.pdf_content_textbox.config(state="normal")
        except Exception as e:
            self.main_window.error_window.show_error_message("Fehler beim Verarbeiten der Datei", str(e))
