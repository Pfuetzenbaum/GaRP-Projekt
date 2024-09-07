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
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.settings_window = ctk.CTkToplevel(self.root)
        self.settings_window.title("Language Tool Einstellungen")
        self.settings_window.geometry("300x200")
        self.settings_window.attributes("-topmost", True) # Setze das Fenster auf die oberste Ebene

        self.create_widgets()

    def create_widgets(self):
        self.language_label = ctk.CTkLabel(self.settings_window, text="Sprache:")
        self.language_label.grid(row=0, column=0, padx=5, pady=5)

        self.language_var = ctk.StringVar()
        self.language_var.set(self.main_window.settings.language)  # Setze den aktuell eingestellten Wert

        self.language_option_menu = ctk.CTkOptionMenu(self.settings_window, values=["Deutsch", "Englisch"], variable=self.language_var)
        self.language_option_menu.grid(row=0, column=1, padx=5, pady=5)

        save_button = ctk.CTkButton(self.settings_window, text="Speichern", command=self.save_settings)
        save_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def save_settings(self):
        selected_language = self.language_var.get()
        # Save the selected language to your settings or database
        self.main_window.settings.language = selected_language
        self.main_window.dictionary_manager_gateway.set_dictionary_manager(selected_language)
        self.settings_window.destroy()  # Close the settings window