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

import customtkinter as ctk  # Importiere CustomTkinter zur Erstellung moderner Tkinter-GUI-Widgets

class ParserSettingsWindow:
    """
    Diese Klasse repräsentiert das Fenster für die Einstellungen des PDF-Parsers.
    Hier kann der Nutzer verschiedene Parsing-Einstellungen ändern und speichern.
    """
    
    def __init__(self, root, main_app):
        """
        Konstruktor der ParserSettingsWindow-Klasse.
        
        :param root: Das Hauptfenster, auf dem das Einstellungsfenster basiert.
        :param main_app: Referenz zur Hauptanwendung, um Einstellungen zu lesen und zu speichern.
        """
        self.root = root
        self.main_app = main_app
        
        # Erstelle ein neues Fenster für die Einstellungen (Toplevel-Fenster)
        self.settings_window = ctk.CTkToplevel(self.root)
        self.settings_window.title("Parser Einstellungen")
        self.settings_window.geometry("400x600")  # Setze die Fenstergröße

        self.create_widgets()  # Initialisiere die Widgets

    def create_widgets(self):
        """
        Erstellt und platziert die Widgets im Einstellungsfenster.
        """
        
        # Label und Auswahlmenü für die Parsing-Grundeinstellung
        self.parsing_basic_setting_label = ctk.CTkLabel(self.settings_window, text="Parsing Grundeinstellung:")
        self.parsing_basic_setting_label.grid(row=0, column=0, padx=5, pady=5)

        # Initialisiere den Wert des Auswahlmenüs basierend auf den aktuellen Einstellungen
        self.parsing_basic_setting_var = ctk.StringVar(value=self.main_app.settings.parsing_basic_setting)
        if self.main_app.settings.parsing_basic_setting == "structured":
            self.parsing_basic_setting_var.set("Strukturiert")
        else:
            self.parsing_basic_setting_var.set("Seitenweise")
        
        # OptionMenü zur Auswahl der Parsing-Grundeinstellung
        self.parsing_basic_setting_optionmenu = ctk.CTkOptionMenu(self.settings_window, values=["Strukturiert", "Seitenweise"], variable=self.parsing_basic_setting_var)
        self.parsing_basic_setting_optionmenu.grid(row=0, column=1, padx=5, pady=5)

        # Label und Eingabefeld für die Startseite
        self.starting_page_label = ctk.CTkLabel(self.settings_window, text="Startseite:")
        self.starting_page_label.grid(row=1, column=0, padx=5, pady=5)

        self.starting_page_entry = ctk.CTkEntry(self.settings_window)
        self.starting_page_entry.insert(0, self.main_app.settings.starting_page)  # Setze den Standardwert auf die aktuelle Startseite
        self.starting_page_entry.grid(row=1, column=1, padx=5, pady=5)

        # Label und Eingabefeld für die Endseite
        self.ending_page_label = ctk.CTkLabel(self.settings_window, text="Endseite:")
        self.ending_page_label.grid(row=2, column=0, padx=5, pady=5)

        self.ending_page_entry = ctk.CTkEntry(self.settings_window)
        self.ending_page_entry.insert(0, self.main_app.settings.ending_page)  # Setze den Standardwert auf die aktuelle Endseite
        self.ending_page_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Checkbox zur Prüfung der Schriftart
        self.check_fontname_label = ctk.CTkLabel(self.settings_window, text="Schriftart prüfen:")
        self.check_fontname_label.grid(row=3, column=0, padx=5, pady=5)

        self.check_fontname_var = ctk.BooleanVar(value=self.main_app.settings.check_fontname)
        self.check_fontname_checkbox = ctk.CTkCheckBox(self.settings_window, text="", variable=self.check_fontname_var)
        self.check_fontname_checkbox.grid(row=3, column=1, padx=5, pady=5)

        # Eingabefelder für die Anzahl der zu überspringenden Zeilen am Anfang und Ende
        self.first_lines_to_skip_label = ctk.CTkLabel(self.settings_window, text="Erste zu überspringende Zeilen:")
        self.first_lines_to_skip_label.grid(row=4, column=0, padx=5, pady=5)

        self.first_lines_to_skip_entry = ctk.CTkEntry(self.settings_window)
        self.first_lines_to_skip_entry.insert(0, self.main_app.settings.first_lines_to_skip)
        self.first_lines_to_skip_entry.grid(row=4, column=1, padx=5, pady=5)

        self.last_lines_to_skip_label = ctk.CTkLabel(self.settings_window, text="Letzte zu überspringende Zeilen:")
        self.last_lines_to_skip_label.grid(row=5, column=0, padx=5, pady=5)

        self.last_lines_to_skip_entry = ctk.CTkEntry(self.settings_window)
        self.last_lines_to_skip_entry.insert(0, self.main_app.settings.last_lines_to_skip)
        self.last_lines_to_skip_entry.grid(row=5, column=1, padx=5, pady=5)

        # Speichern-Button, um die Änderungen zu übernehmen
        self.save_button = ctk.CTkButton(self.settings_window, text="Speichern", command=self.save_settings)
        self.save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=20)

        # Setze das Fenster immer in den Vordergrund
        self.settings_window.attributes("-topmost", True)

    def save_settings(self):
        """
        Speichert die vorgenommenen Einstellungen.
        Behandelt auch mögliche Eingabefehler wie ungültige Seitenzahlen.
        """
        try:
            # Übernehme die ausgewählte Parsing-Einstellung
            parsing_basic_setting = self.parsing_basic_setting_var.get()
            if parsing_basic_setting == "Strukturiert":
                self.main_app.settings.parsing_basic_setting = "structured"
            elif parsing_basic_setting == "Seitenweise":
                self.main_app.settings.parsing_basic_setting = "pagewise"

            # Übernehme die Werte für Start- und Endseiten sowie die zu überspringenden Zeilen
            self.main_app.settings.starting_page = int(self.starting_page_entry.get())
            self.main_app.settings.ending_page = int(self.ending_page_entry.get())
            self.main_app.settings.first_lines_to_skip = int(self.first_lines_to_skip_entry.get())
            self.main_app.settings.last_lines_to_skip = int(self.last_lines_to_skip_entry.get())

            # Wenn "Strukturiert" ausgewählt ist, prüfe auch die Schriftart
            if self.main_app.settings.parsing_basic_setting == "structured":
                self.main_app.settings.check_fontname = self.check_fontname_var.get()

            # Schließe das Einstellungsfenster
            self.settings_window.destroy()
        except ValueError as e:
            # Behandle ungültige Eingaben, wie z.B. nicht-numerische Werte
            error_message = "Ungültige Eingabe: {}".format(e)
            ctk.CTkMessagebox.show_error("Fehler", error_message)
        except Exception as e:
            # Behandle alle anderen unerwarteten Fehler
            error_message = "Ein unerwarteter Fehler ist aufgetreten: {}".format(e)
            ctk.CTkMessagebox.show_error("Fehler", error_message)
