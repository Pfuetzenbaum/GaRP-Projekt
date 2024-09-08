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

class Settings:
    """
    Diese Klasse speichert die Konfigurationseinstellungen für die Anwendung.
    Die Einstellungen werden von verschiedenen Fenstern und Controllern verwendet, um die
    Funktionsweise der Anwendung zu steuern, wie z.B. das Parsing von PDF-Dateien und die Spracheinstellungen.
    """

    def __init__(self):
        """
        Konstruktor der Settings-Klasse. Initialisiert alle Standardeinstellungen.
        """
        # Grundeinstellung für das Parsing, entweder "structured" (strukturiert) oder "pagewise" (seitenweise)
        self.parsing_basic_setting = "structured"
        
        # Startseite und Endseite für das Parsing von PDF-Dateien
        self.starting_page = 1  # Die erste Seite, die im PDF geparst wird
        self.ending_page = 100  # Die letzte Seite, die im PDF geparst wird
        
        # Boolean, um zu überprüfen, ob die Schriftart beim Parsing berücksichtigt werden soll
        self.check_fontname = False
        
        # Anzahl der ersten und letzten Zeilen, die beim Parsing übersprungen werden sollen
        self.first_lines_to_skip = 0
        self.last_lines_to_skip = 0
        
        # Spracheinstellung für die Rechtschreib- und Grammatikprüfung (Standard ist "Deutsch")
        self.language = "Deutsch"

