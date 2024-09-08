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

class ErrorWindow:
    """
    Diese Klasse stellt ein Fenster zur Anzeige von Fehlermeldungen bereit.
    Es wird ein einfaches Popup-Fenster erstellt, das eine Fehlermeldung anzeigt.
    """

    def __init__(self, root):
        """
        Konstruktor der ErrorWindow-Klasse.
        
        :param root: Das übergeordnete Tkinter-Hauptfenster, auf dem das Fehlerfenster basiert.
        """
        self.root = root

    def show_error_message(self, title, message):
        """
        Zeigt ein Fehler-Popup-Fenster mit einem Titel und einer Nachricht an.
        
        :param title: Der Titel des Fehlerfensters (z. B. der Fehlername).
        :param message: Die Fehlermeldung, die im Fenster angezeigt werden soll.
        """
        # Erstelle ein Toplevel-Fenster für die Fehlermeldung
        error_window = ctk.CTkToplevel(self.root)
        error_window.title(title)  # Setze den Fenstertitel auf den Fehlernamen
        error_window.geometry("400x200")  # Bestimme die Größe des Fensters
        error_window.attributes("-topmost", True)  # Stelle sicher, dass das Fenster im Vordergrund bleibt

        # Erstelle ein Label zur Anzeige der Fehlermeldung, mit einer maximalen Textbreite (wraplength)
        error_label = ctk.CTkLabel(error_window, text=message, wraplength=380)
        error_label.pack(padx=10, pady=10)  # Platziere das Label mit etwas Abstand zum Rand des Fensters
