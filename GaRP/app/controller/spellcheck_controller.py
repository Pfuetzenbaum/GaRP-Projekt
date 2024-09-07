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

class SpellcheckController:

    def __init__(self, main_window, dictionary_manager_gateway):
        self.main_window = main_window
        self.settings = dictionary_manager_gateway.settings
        self.dictionary_manager_gateway = dictionary_manager_gateway

    def check_spelling(self):

        # Leere die error_tree
        self.main_window.error_tree.selection_clear()
        for item in self.main_window.error_tree.get_children():
            self.main_window.error_tree.delete(item)

        self.main_window.error_list = []

        #Alle Tags entfernen
        for tag in self.main_window.pdf_content_textbox.tag_names():
            self.main_window.pdf_content_textbox.tag_remove(tag, "1.0", "end")

        try:
            extracted_text = self.main_window.pdf_content_textbox.get("1.0", "end-1c")

            word_list = self.dictionary_manager_gateway.dictionary_manager.checkTextFiltered(extracted_text)

            # Füge die gefundenen Fehler zur Liste hinzu
            for word in word_list:

                affected_part = word.getAffectedPart()
                short_message = word.getShortMessage()
                long_message = word.getLongMessage()
                from_pos = word.getFromPos()
                to_pos = word.getToPos()

                # Füge den Fehler zur error_tree hinzu
                self.main_window.error_tree.insert('', 'end', values=(affected_part, long_message))
                self.main_window.error_list.append(word)

                # Binde die Auswahl-Events der error_tree neu, um sicherzustellen, dass sie korrekt funktionieren
                self.main_window.error_tree.bind('<<TreeviewSelect>>', self.show_spellcheck_details)
                           
                # Markiere den Fehler im Textfeld
                self.highlight_error(from_pos, to_pos, short_message)
                
        except Exception as e:
            self.main_window.error_window.show_error_message("Fehler beim Überprüfen der Rechtschreibung", str(e))
        
    
    def highlight_error(self, from_pos, to_pos, short_message):

        # Finden Sie die Zeile und Spalte des Fehlers im Textfeld
        lines = self.main_window.pdf_content_textbox.get("1.0", "end-1c").split("\n")
        line_length = 0
        line_number = 1
        for line in lines:
            if line_length + len(line) >= from_pos:
                break
            line_length += len(line) + 1
            line_number += 1

        # Berechnen Sie die Spalte des Fehlers in der Zeile
        column = from_pos - line_length

        if short_message == 'Rechtschreibfehler' or short_message == 'Spelling mistake':

            self.main_window.pdf_content_textbox.tag_remove("spelling_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            self.main_window.pdf_content_textbox.tag_add("spelling_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            
        else:
            self.main_window.pdf_content_textbox.tag_remove("other_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            self.main_window.pdf_content_textbox.tag_add("other_error", f"{line_number}.{column}", f"{line_number}.{column + (to_pos - from_pos)}")
            

    def show_spellcheck_details(self, event):
        try:
            selected_items = self.main_window.error_tree.selection()
            if selected_items:
                selected_item = selected_items[0]
                affected_part = self.main_window.error_tree.item(selected_item, 'values')[0]

                # Finde den entsprechenden Fehler in der error_list
                for error in self.main_window.error_list:
                    if error.getAffectedPart() == affected_part:
                        selected_error = error
                        break

                # Neues Fenster für detaillierte Fehlerbeschreibung
                spelling_error_window = ctk.CTkToplevel(self.main_window.root)
                spelling_error_window.title("Fehlerdetails")
                spelling_error_window.geometry("400x400")
                spelling_error_window.attributes("-topmost", True)  # Setze das Fenster auf die oberste Ebene

                error_details = ctk.CTkTextbox(spelling_error_window, wrap='word', border_width=1)
                error_details.insert("1.0", 
                                        f"Betroffener Teil: {affected_part}\n\n"
                                        f"Verbesserungvorschlag: {selected_error.getImprovement()}\n"
                                        f"Kurzmeldung: {selected_error.getShortMessage()}\n"
                                        f"Lange Meldung: {selected_error.getLongMessage()}\n\n"
                                        f"Betroffener Satz: {selected_error.getSentence()}\n")
                error_details.configure(state="disabled")
                error_details.pack(fill="both", expand=True, padx=10, pady=10)

                add_word_button = ctk.CTkButton(spelling_error_window, text="Dauerhaft zum Wörterbuch hinzufügen", font=('Arial', 14),
                                                command=lambda: self.add_word_and_disable_button(add_word_button, affected_part))
                add_word_button.pack(padx=10, pady=10)

                add_word_temporary_button = ctk.CTkButton(spelling_error_window, text="Für dieses Session ignorieren", font=('Arial', 14),
                                                        command=lambda: self.ignore_word_and_disable_button(add_word_temporary_button,affected_part))
                add_word_temporary_button.pack(padx=10, pady=10)

                if selected_error.getShortMessage() != 'Rechtschreibfehler' and selected_error.getShortMessage() != 'Spelling mistake':
                    add_word_button.configure(state="disabled")
                    add_word_temporary_button.configure(state="disabled")

        except Exception as e:
            self.main_window.error_window.show_error_message("Fehler bei der Anzeige von Fehlerdetails", str(e))

    def add_word_and_disable_button(self, button, word):
        self.dictionary_manager_gateway.dictionary_manager.addWord(word)
        button.configure(state="disabled")

    def ignore_word_and_disable_button(self, button, word):
        self.dictionary_manager_gateway.dictionary_manager.ignoreWordInSession(word)
        button.configure(state="disabled")
