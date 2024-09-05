import customtkinter as ctk

class ErrorWindow:
    def __init__(self, root):
        self.root = root

    def show_error_message(self, title, message):
        error_window = ctk.CTkToplevel(self.root)
        error_window.title(title)
        error_window.geometry("400x200")
        error_window.attributes("-topmost", True)  # Setze das Fenster auf die oberste Ebene

        error_label = ctk.CTkLabel(error_window, text=message, wraplength=380)
        error_label.pack(padx=10, pady=10)