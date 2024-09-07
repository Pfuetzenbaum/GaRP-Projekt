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

class ErrorExportController:
    def __init__(self, main_window):
        self.main_window = main_window

    def export_errors(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Textdateien", "*.csv")])
            if file_path:
                with open(file_path, "w", encoding="utf-8") as f:
                    for error in self.main_window.error_list:
                        f.write(f"{error.getAffectedPart()},{error.getShortMessage()},{error.getLongMessage()},{error.getSentence()}\n")
                self.main_window.error_window.show_error_message("Erfolgreich exportiert", "Die Fehler wurden erfolgreich in eine Textdatei exportiert.")
        except Exception as e:
            self.main_window.error_window.show_error_message("Fehler beim Exportieren", str(e))
