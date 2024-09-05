import customtkinter as ctk

class ExceptWordsWindow:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app
        self.except_words_window = ctk.CTkToplevel(self.root)
        self.except_words_window.title("Wörter entfernen")
        self.except_words_window.geometry("600x400")
        

        self.except_words_label = ctk.CTkLabel(self.except_words_window, text="Zu entfernendes Wort:")
        self.except_words_label.grid(row=0, column=0, columnspan=1,padx=5, pady=5)

        self.except_words_entry = ctk.CTkEntry(self.except_words_window)
        self.except_words_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self.except_words_entry.bind("<Return>", lambda event: self.add_except_word())

        self.words_frame = ctk.CTkFrame(self.except_words_window)
        self.words_frame.grid(row=1, column=0, sticky="nsw", padx=5, pady=5)

        self.process_button = ctk.CTkButton(self.except_words_window, text="Wort zur Liste hinzufügen", command=self.add_except_word)
        self.process_button.grid(row=0, column=3, columnspan=2, padx=5, pady=20)

        self.save_button = ctk.CTkButton(self.except_words_window, text="Speichern & Datei neu verarbeiten", command=self.execute_except_words)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

        self.except_quotation_marks_button = ctk.CTkButton(self.except_words_window, text="Anführungszeichen entfernen", command=self.except_quotation_marks)
        self.except_quotation_marks_button.grid(row=4, column=2, columnspan=3, padx=5, pady=20)

        self.update_except_words_list()

        self.except_words_window.attributes("-topmost", True)  # Setze das Fenster auf die oberste Ebene


    def add_except_word(self):
        word_to_except = self.except_words_entry.get()
        if word_to_except:
            self.main_app.except_words.append(word_to_except)
            self.except_words_entry.delete(0, 'end')
            self.update_except_words_list()

    def update_except_words_list(self):
        for widget in self.words_frame.winfo_children():
            widget.destroy()

        for i, word in enumerate(self.main_app.except_words):
            frame = ctk.CTkFrame(self.words_frame)
            frame.grid(row=i, column=0, sticky='ew')

            label = ctk.CTkLabel(frame, text=word)
            label.grid(row=0, column=0, sticky='w', padx=(0, 10)) 

            button = ctk.CTkButton(frame, text="Löschen", command=lambda word=word: self.remove_except_word(word))
            button.grid(row=0, column=3, sticky='e', padx=(10, 0))  
            button.configure(width=8, height=0.8)  # Make the button smaller

    def remove_except_word(self, word):
        self.main_app.except_words.remove(word)
        self.update_except_words_list()

    def execute_except_words(self):
        text = self.main_app.pdf_content_textbox.get("1.0", "end-1c")
        for word in self.main_app.except_words:
            text = text.replace(word, "")
        self.main_app.pdf_content_textbox.delete("1.0", "end")
        self.main_app.pdf_content_textbox.insert("1.0", text)
        self.except_words_window.destroy()
        
    def except_quotation_marks(self):
        text = self.main_app.pdf_content_textbox.get("1.0", "end-1c")
        text = text.replace("„", "")
        text = text.replace("“", "")
        text = text.replace("”", "")
        text = text.replace('"', '')
        self.main_app.pdf_content_textbox.delete("1.0", "end")
        self.main_app.pdf_content_textbox.insert("1.0", text)