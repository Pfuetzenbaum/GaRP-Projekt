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

import sys
from cx_Freeze import setup, Executable

# Build options für cx_Freeze
build_exe_options = {
    "packages": ["os", "py4j", "customtkinter", "tkinter", "pdfminer"],
    "include_files": ["integrations/lib/demo-1.0.jar", "integrations/lib/Dictionary/CustomDictionaryGerman", "integrations/lib/Dictionary/CustomDictionaryEnglish"],  # JAR-Datei inkludieren
    "optimize": 2,
    "include_msvcr": False  # Um Microsoft Visual C++ Redistributables zu includieren, falls nötig
}

# Festlegen der Basis für die ausführbare Datei
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # "Console" für Konsolenanwendungen, "Win32GUI" für GUI-Anwendungen

# Erstelle die setup-Konfiguration
setup(
    name="GaRP",
    version="1.0",
    description="GaRP - das Tool zur Grammatik- und Rechtschreibprüfung von PDF-Dateien",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon="icon.ico")]  # "app/main.py" als Einstiegspunkt
)
