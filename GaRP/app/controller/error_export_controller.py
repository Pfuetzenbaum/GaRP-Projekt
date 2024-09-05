from tkinter import filedialog

class ErrorExportController:
    def __init__(self, main_window):
        self.main_window = main_window

    def export_errors(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Textdateien", "*.txt")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    for error in self.main_window.error_list:
                        f.write(f"{error.getAffectedPart()},{error.getShortMessage()},{error.getLongMessage()},{error.getSentence()}\n")
                self.main_window.error_window.show_error_message("Erfolgreich exportiert", "Die Fehler wurden erfolgreich in eine Textdatei exportiert.")
        except Exception as e:
            self.main_window.error_window.show_error_message("Fehler beim Exportieren", str(e))
