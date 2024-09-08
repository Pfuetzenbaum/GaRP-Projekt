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

class LanguageToolSettingsWindow:
    """
    Diese Klasse repräsentiert das Einstellungsfenster für die LanguageTool-Konfiguration.
    Hier kann der Benutzer die Sprache für die Rechtschreib- und Grammatikprüfung auswählen.
    """

    def __init__(self, root, main_window):
        """
        Konstruktor der LanguageToolSettingsWindow-Klasse.
        
        :param root: Das übergeordnete Tkinter-Hauptfenster.
        :param main_window: Referenz auf das Hauptfenster, um Zugriff auf die Einstellungen zu haben.
        """
        self.root = root
        self.main_window = main_window
        
        # Erstelle ein neues Toplevel-Fenster für die LanguageTool-Einstellungen
        self.settings_window = ctk.CTkToplevel(self.root)
        self.settings_window.title("Language Tool Einstellungen")  # Setze den Fenstertitel
        self.settings_window.geometry("300x200")  # Setze die Fenstergröße
        self.settings_window.attributes("-topmost", True)  # Das Fenster bleibt immer im Vordergrund

        self.create_widgets()  # Erstelle und platziere die Widgets

    def create_widgets(self):
        """
        Erstellt und platziert die Widgets im LanguageTool-Einstellungsfenster.
        """
        # Label für die Sprachauswahl
        self.language_label = ctk.CTkLabel(self.settings_window, text="Sprache:")
        self.language_label.grid(row=0, column=0, padx=5, pady=5)  # Platziere das Label in der ersten Zeile

        # Dropdown-Menü für die Sprachauswahl
        self.language_var = ctk.StringVar()  # Erstelle eine Variable zur Speicherung der gewählten Sprache
        self.language_var.set(self.main_window.settings.language)  # Setze den Standardwert auf die aktuell eingestellte Sprache

        # OptionMenü für die Sprachauswahl (Deutsch oder Englisch)
        self.language_option_menu = ctk.CTkOptionMenu(self.settings_window, values=["Deutsch", "Englisch"], variable=self.language_var)
        self.language_option_menu.grid(row=0, column=1, padx=5, pady=5)  # Platziere das Dropdown-Menü neben dem Label

        # Button zum Speichern der Einstellungen
        save_button = ctk.CTkButton(self.settings_window, text="Speichern", command=self.save_settings)
        save_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)  # Platziere den Button unter den vorherigen Widgets

    def save_settings(self):
        """
        Speichert die ausgewählte Sprache und aktualisiert die Einstellungen in der Hauptanwendung.
        Schließt das Einstellungsfenster nach dem Speichern.
        """
        selected_language = self.language_var.get()  # Hole die ausgewählte Sprache aus dem Dropdown-Menü
        # Speichere die ausgewählte Sprache in den Einstellungen der Hauptanwendung
        self.main_window.settings.language = selected_language
        # Setze den entsprechenden Wörterbuch-Manager basierend auf der gewählten Sprache
        self.main_window.dictionary_manager_gateway.set_dictionary_manager(selected_language)
        self.settings_window.destroy()  # Schließe das Einstellungsfenster
