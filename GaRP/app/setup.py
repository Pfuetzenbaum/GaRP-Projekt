import sys
from cx_Freeze import setup, Executable

# Build options für cx_Freeze
build_exe_options = {
    "packages": ["os", "py4j", "customtkinter", "tkinter", "pdfminer"],
    "include_files": ["integrations/lib/demo-1.0_new.jar", "integrations/lib/Dictionary/CustomDictionaryGerman"],  # JAR-Datei inkludieren
    "include_msvcr": True  # Um Microsoft Visual C++ Redistributables zu includieren, falls nötig
}

# Festlegen der Basis für die ausführbare Datei
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # "Console" für Konsolenanwendungen, "Win32GUI" für GUI-Anwendungen

# Erstelle die setup-Konfiguration
setup(
    name="GaRP",
    version="1.0",
    description="GaRP Anwendung",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]  # "app/main.py" als Einstiegspunkt
)
