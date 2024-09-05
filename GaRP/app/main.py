import customtkinter as ctk
from views.main_window import MainWindow
from views.error_window import ErrorWindow


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.file_path = None
        error_window = ErrorWindow(self.root)  # Initialisiere ErrorWindow hier
        
        try:
            self.main_window = MainWindow(self.root, error_window)
        except Exception as e:
            self.error_window.show_error_message("Fehler beim Initialisieren des Programms", str(e))  # Verwende self.error_window hier


if __name__ == "__main__":
    root = ctk.CTk()
    app = MainApplication(root)
    root.mainloop()
