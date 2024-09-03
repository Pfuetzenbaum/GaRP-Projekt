import customtkinter as ctk

class ExceptWordsWindow:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app
        self.except_words_window = ctk.CTkToplevel(self.root)
        self.except_words_window.title("Wörter entfernen")
        self.except_words_window.geometry("600x400")
        

        self.except_words_label = ctk.CTkLabel(self.except_words_window, text="Zu entfernendes Wort:")
        self.except_words_label.pack(padx=5, pady=5)

        self.except_words_entry = ctk.CTkEntry(self.except_words_window)
        self.except_words_entry.pack(padx=5, pady=5)

        self.process_button = ctk.CTkButton(self.except_words_window, text="Wort zur Liste hinzufügen", command=self.add_except_word)
        self.process_button.pack(side="bottom", padx=5, pady=20)

        self.save_button = ctk.CTkButton(self.except_words_window, text="Speichern & Datei neu verarbeiten", command=self.execute_except_words)
        self.save_button.pack(side="bottom", padx=5, pady=20)

        self.except_quotation_marks_button = ctk.CTkButton(self.except_words_window, text="Anführungszeichen entfernen", command=self.except_quotation_marks)
        self.except_quotation_marks_button.pack(side="bottom", padx=5, pady=20)

        self.words_frame = ctk.CTkFrame(self.except_words_window)
        self.words_frame.pack(fill='both', expand=True, padx=5, pady=5)

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

        for word in self.main_app.except_words:
            ctk.CTkLabel(self.words_frame, text=word).pack(anchor='w')

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