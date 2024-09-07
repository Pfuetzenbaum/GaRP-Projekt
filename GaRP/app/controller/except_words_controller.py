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
    def __init__(self, except_words_window):
        self.except_words_window = except_words_window
    
    def add_except_word(self):
        word_to_except = self.except_words_window.except_words_entry.get()
        if word_to_except:
            self.except_words_window.main_window.except_words.append(word_to_except)
            self.except_words_window.except_words_entry.delete(0, 'end')
            self.update_except_words_list()

    def update_except_words_list(self):
        for widget in self.except_words_window.words_frame.winfo_children():
            widget.destroy()

        for i, word in enumerate(self.except_words_window.main_window.except_words):
            frame = ctk.CTkFrame(self.except_words_window.words_frame)
            frame.grid(row=i, column=0, sticky='ew')

            label = ctk.CTkLabel(frame, text=word)
            label.grid(row=0, column=0, sticky='w', padx=(0, 10)) 

            button = ctk.CTkButton(frame, text="Löschen", command=lambda word=word: self.remove_except_word(word))
            button.grid(row=0, column=3, sticky='e', padx=(10, 0))  
            button.configure(width=8, height=0.8) 

    def remove_except_word(self, word):
        self.except_words_window.main_window.except_words.remove(word)
        self.update_except_words_list()

    def execute_except_words(self):
        text = self.except_words_window.main_window.pdf_content_textbox.get("1.0", "end-1c")
        for word in self.except_words_window.main_window.except_words:
            text = text.replace(word, "")
        self.except_words_window.main_window.pdf_content_textbox.delete("1.0", "end")
        self.except_words_window.main_window.pdf_content_textbox.insert("1.0", text)
        self.except_words_window.except_words_window.destroy()
        
    def except_quotation_marks(self):
        text = self.except_words_window.main_window.pdf_content_textbox.get("1.0", "end-1c")
        text = text.replace("„", "")
        text = text.replace("“", "")
        text = text.replace("”", "")
        text = text.replace('"', '')
        self.except_words_window.main_window.pdf_content_textbox.delete("1.0", "end")
        self.except_words_window.main_window.pdf_content_textbox.insert("1.0", text)