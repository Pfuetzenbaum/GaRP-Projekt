import customtkinter as ctk
from controller.except_words_controller import ExceptWordsController

class ExceptWordsWindow:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.except_words_controller = ExceptWordsController(self)
        self.except_words_window = ctk.CTkToplevel(self.root)
        self.except_words_window.title("Wörter entfernen")
        self.except_words_window.geometry("600x400")
        

        self.except_words_label = ctk.CTkLabel(self.except_words_window, text="Zu entfernendes Wort:")
        self.except_words_label.grid(row=0, column=0, columnspan=1,padx=5, pady=5)

        self.except_words_entry = ctk.CTkEntry(self.except_words_window)
        self.except_words_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self.except_words_entry.bind("<Return>", lambda event: self.except_words_controller.add_except_word())

        self.words_frame = ctk.CTkFrame(self.except_words_window)
        self.words_frame.grid(row=1, column=0, sticky="nsw", padx=5, pady=5)

        self.process_button = ctk.CTkButton(self.except_words_window, text="Wort zur Liste hinzufügen", command=self.except_words_controller.add_except_word)
        self.process_button.grid(row=0, column=3, columnspan=2, padx=5, pady=20)

        self.save_button = ctk.CTkButton(self.except_words_window, text="Speichern & Datei neu verarbeiten", command=self.except_words_controller.execute_except_words)
        self.save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

        self.except_quotation_marks_button = ctk.CTkButton(self.except_words_window, text="Anführungszeichen entfernen", command=self.except_words_controller.except_quotation_marks)
        self.except_quotation_marks_button.grid(row=4, column=2, columnspan=3, padx=5, pady=20)

        self.except_words_controller.update_except_words_list()

        self.except_words_window.attributes("-topmost", True)  # Setze das Fenster auf die oberste Ebene


    