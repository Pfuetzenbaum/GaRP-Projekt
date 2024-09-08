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

from tkinter import filedialog  # Importiere das Modul zur Dateiauswahl

class ErrorExportController:
    """
    Diese Klasse steuert den Export der Fehlerliste in eine Textdatei (CSV-Format).
    Sie interagiert mit der Hauptanwendung, um die Fehlerliste zu exportieren und entsprechende Fehler zu behandeln.
    """

    def __init__(self, main_window):
        """
        Konstruktor für den ErrorExportController.

        :param main_window: Referenz auf das Hauptfenster der Anwendung, um auf die Fehlerliste zuzugreifen.
        """
        self.main_window = main_window  # Referenz auf das Hauptfenster, um auf GUI-Komponenten und Daten zuzugreifen

    def export_errors(self):
        """
        Exportiert die Fehlerliste in eine CSV-Datei.
        Öffnet einen Speicherdialog, in dem der Benutzer den Speicherort und den Dateinamen festlegen kann.
        """
        try:
            # Öffne einen Speicherdialog, in dem der Benutzer den Pfad für die CSV-Datei auswählen kann
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Textdateien", "*.csv")])
            
            # Wenn der Benutzer einen Dateipfad ausgewählt hat
            if file_path:
                # Öffne die Datei im Schreibmodus
                with open(file_path, "w", encoding="utf-8") as f:
                    # Schreibe jede Zeile der Fehlerliste in die CSV-Datei
                    for error in self.main_window.error_list:
                        f.write(f"{error.getAffectedPart()},{error.getShortMessage()},{error.getLongMessage()},{error.getSentence()}\n")
                
                # Zeige eine Erfolgsmeldung an, wenn der Export erfolgreich war
                self.main_window.error_window.show_error_message("Erfolgreich exportiert", "Die Fehler wurden erfolgreich in eine Textdatei exportiert.")
        
        except Exception as e:
            # Zeige eine Fehlermeldung an, falls beim Export ein Fehler auftritt
            self.main_window.error_window.show_error_message("Fehler beim Exportieren", str(e))

