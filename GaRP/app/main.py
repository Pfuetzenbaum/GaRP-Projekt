"""
Copyright (C) 2024 Gantert, Schneider, Sewald

Dieses Programm ist freie Software: Sie können es unter den Bedingungen
der GNU General Public License, wie von der Free Software Foundation veröffentlicht,
entweder Version 3 der Lizenz oder (nach Ihrer Wahl) jeder späteren Version
weitergeben und/oder modifizieren.

Dieses Programm wird in der Hoffnung verbreitet, dass es nützlich sein wird,
aber OHNE JEDE GEWÄHRLEISTUNG; sogar ohne die implizite Gewährleistung der
MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK. Siehe die
GNU General Public License für weitere Details.

Sie sollten eine Kopie der GNU General Public License zusammen mit diesem Programm
erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.
"""

import customtkinter as ctk  # Importiere das CustomTkinter-Modul zur Erstellung der GUI
from views.main_window import MainWindow  # Importiere die Hauptfensterklasse
from views.error_window import ErrorWindow  # Importiere die Fehlerfensterklasse


class MainApplication:
    """
    Diese Klasse stellt die Hauptanwendung dar, die das Hauptfenster und das Fehlerfenster verwaltet.
    """
    def __init__(self, root):
        """
        Konstruktor der MainApplication Klasse.
        Initialisiert die GUI und behandelt Fehler, die beim Erstellen der Hauptfenster auftreten könnten.
        
        :param root: Das Hauptfenster (root) der Anwendung
        """
        self.root = root
        self.error_window = ErrorWindow(self.root)  # Initialisiere das Fehlerfenster
        
        try:
            # Versuche, das Hauptfenster der Anwendung zu initialisieren
            self.main_window = MainWindow(self.root, self.error_window)
        except Exception as e:
            # Bei einem Fehler während der Initialisierung wird eine Fehlermeldung angezeigt
            self.error_window.show_error_message("Fehler beim Initialisieren des Programms", str(e))  


if __name__ == "__main__":
    """
    Der Einstiegspunkt der Anwendung.
    Erstellt das Hauptfenster und startet die Hauptanwendung im Haupt-Event-Loop.
    """
    root = ctk.CTk()  # Erstelle das Hauptfenster der Anwendung mit CustomTkinter
    app = MainApplication(root)  # Initialisiere die Hauptanwendung
    root.mainloop()  # Starte die Tkinter-Hauptschleife, um die GUI anzuzeigen
