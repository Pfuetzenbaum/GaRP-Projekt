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

class ExceptWordsController:
    """
    Diese Klasse steuert die Verwaltung von Ausnahmewörtern, die von der Rechtschreib- und Grammatikprüfung
    ausgeschlossen werden sollen. Sie ermöglicht das Hinzufügen, Entfernen und Anwenden von Ausnahmewörtern.
    """

    def __init__(self, except_words_window):
        """
        Konstruktor für den ExceptWordsController.

        :param except_words_window: Referenz auf das Fenster, das die Ausnahmewörter verwaltet.
        """
        self.except_words_window = except_words_window  # Verbindung zum Fenster für Ausnahmewörter

    def add_except_word(self):
        """
        Fügt ein neues Wort zur Ausnahmeliste hinzu und aktualisiert die Liste im Fenster.
        """
        # Hole das eingegebene Wort aus dem Eingabefeld
        word_to_except = self.except_words_window.except_words_entry.get()

        # Wenn das Wort nicht leer ist, füge es der Liste hinzu
        if word_to_except:
            self.except_words_window.main_window.except_words.append(word_to_except)
            self.except_words_window.except_words_entry.delete(0, 'end')  # Lösche das Eingabefeld
            self.update_except_words_list()  # Aktualisiere die Anzeige der Liste

    def update_except_words_list(self):
        """
        Aktualisiert die Anzeige der Liste der Ausnahmewörter im Fenster.
        """
        # Entferne alle bestehenden Widgets in der words_frame, um die Liste zu aktualisieren
        for widget in self.except_words_window.words_frame.winfo_children():
            widget.destroy()

        # Füge jedes Ausnahmewort zur Anzeige hinzu
        for i, word in enumerate(self.except_words_window.main_window.except_words):
            frame = ctk.CTkFrame(self.except_words_window.words_frame)
            frame.grid(row=i, column=0, sticky='ew')

            # Zeige das Wort als Label an
            label = ctk.CTkLabel(frame, text=word)
            label.grid(row=0, column=0, sticky='w', padx=(0, 10))

            # Erstelle einen Löschen-Button, um das Wort aus der Liste zu entfernen
            button = ctk.CTkButton(frame, text="Löschen", command=lambda word=word: self.remove_except_word(word))
            button.grid(row=0, column=3, sticky='e', padx=(10, 0))
            button.configure(width=8, height=0.8)

    def remove_except_word(self, word):
        """
        Entfernt ein Wort aus der Ausnahmeliste und aktualisiert die Liste im Fenster.

        :param word: Das Wort, das aus der Liste entfernt werden soll.
        """
        # Entferne das Wort aus der Liste der Ausnahmewörter
        self.except_words_window.main_window.except_words.remove(word)
        self.update_except_words_list()  # Aktualisiere die Anzeige der Liste

    def execute_except_words(self):
        """
        Entfernt alle Ausnahmewörter aus dem PDF-Inhalt und aktualisiert das Textfeld.
        """
        # Hole den Text aus dem PDF-Inhaltsfeld
        text = self.except_words_window.main_window.pdf_content_textbox.get("1.0", "end-1c")

        # Entferne jedes Wort in der Ausnahmeliste aus dem Text
        for word in self.except_words_window.main_window.except_words:
            text = text.replace(word, "")

        # Aktualisiere das Textfeld mit dem bereinigten Text
        self.except_words_window.main_window.pdf_content_textbox.delete("1.0", "end")
        self.except_words_window.main_window.pdf_content_textbox.insert("1.0", text)

        # Schließe das Fenster zur Verwaltung der Ausnahmewörter
        self.except_words_window.except_words_window.destroy()

    def except_quotation_marks(self):
        """
        Entfernt alle Anführungszeichen aus dem PDF-Inhalt und aktualisiert das Textfeld.
        """
        # Hole den Text aus dem PDF-Inhaltsfeld
        text = self.except_words_window.main_window.pdf_content_textbox.get("1.0", "end-1c")

        # Entferne verschiedene Arten von Anführungszeichen
        text = text.replace("„", "")
        text = text.replace("“", "")
        text = text.replace("”", "")
        text = text.replace('"', '')

        # Aktualisiere das Textfeld mit dem bereinigten Text
        self.except_words_window.main_window.pdf_content_textbox.delete("1.0", "end")
        self.except_words_window.main_window.pdf_content_textbox.insert("1.0", text)
