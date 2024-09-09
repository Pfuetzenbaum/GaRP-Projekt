# GaRP – Grammatik- und Rechtschreibprüfung für PDF-Dateien

## Projektbeschreibung

GaRP ist ein Tool zur Rechtschreib- und Grammatikprüfung für PDF-Dateien, entwickelt als Semesterprojekt im Studiengang Wirtschaftsinformatik an der DHBW Ravensburg. Es ermöglicht das Extrahieren von Text aus PDF-Dateien und die Überprüfung auf Fehler mithilfe von [LanguageTool](https://languagetool.org). Ergebnisse der Prüfungen werden farblich markiert und als Liste zur Fehlerkorrektur exportierbar gemacht.

## Funktionsumfang

- **PDF-Text-Extraktion:** Möglichkeit, Text aus PDF-Dateien zu extrahieren und manuell zu bearbeiten.
- **Rechtschreib- und Grammatikprüfung:** Nutzung von LanguageTool zur Überprüfung des Textes.
- **Fehlerexport:** Speichern der Fehlerliste in einer Textdatei.
- **Wörterbuchmanagement:** Möglichkeit, Wörter zu einem permanenten Wörterbuch hinzuzufügen oder temporär für eine Sitzung zu ignorieren.

## Systemvoraussetzungen

- **Java Runtime Environment (JRE)** ab Version 8 (für die Java-Integration über Py4J).
- **Betriebssystem:** Windows, macOS oder Linux.
- **Python 3.12.1** oder höher (nur für Entwicklungszwecke).

## Installation

1. **Voraussetzungen installieren** (nur für Entwickler):

   - Installiere [Python 3.12.1](https://www.python.org/downloads/).
   - Installiere die erforderlichen Python-Bibliotheken mit:
     ```bash
     pip install -r requirements.txt
     ```
   - Stelle sicher, dass [Java Runtime Environment](https://www.java.com/download/) auf deinem System installiert ist.

2. **EXE-Datei verwenden**:
   - Lade das Verzeichnis (inkl. .exe-Datei) \app\build\GaRP-Anwendung herunter und stelle sicher, dass die JRE installiert ist.
   - Doppelklicke auf die main.exe, um die GaRP-Anwendung zu starten.

## Verwendung

1. **PDF-Datei auswählen**: Über den Button „Datei auswählen“ wird ein PDF-Dokument geladen.
2. **Text extrahieren**: Der Text des PDFs wird extrahiert und im Textfeld angezeigt.
3. **Prüfen**: Mit dem Button „Überprüfen“ werden Grammatik- und Rechtschreibfehler identifiziert und markiert.
4. **Fehler exportieren**: Die erkannten Fehler können als Textdatei exportiert werden.
5. **Wörterbuchverwaltung**: Gefundene Wörter können dauerhaft oder temporär zu einem Wörterbuch hinzugefügt werden.

## Architektur

- **GUI**: Entwickelt mit CustomTkinter für eine benutzerfreundliche Oberfläche.
- **PDF-Parsing**: Mithilfe von `pdfminer.six` werden Textinhalte aus PDF-Dateien extrahiert.
- **Sprache-Tools**: Integration von LanguageTool über Py4J zur Grammatik- und Rechtschreibprüfung.
- **Verzeichnisstruktur**:
  ```bash
  app/
    controller/
    integrations/
    settings/
    views/
  main.py
  ```

## Technologien

- **Python**: Version 3.12.1
- **Java**: Verwendet für LanguageTool-Integration
- **Py4J**: Schnittstelle zur Kommunikation zwischen Python und Java
- **pdfminer.six**: Für das PDF-Parsing
- **CustomTkinter**: Für die GUI-Entwicklung

## Bekannte Probleme

- **Parsing-Fehler**: Probleme bei der Extraktion von mathematischen Formeln oder speziellen Zeichen.
- **Fehlerhafte Sonderzeichen**: Bestimmte Umlaute und Sonderzeichen können bei bestimmten PDF-Formaten nicht korrekt extrahiert werden.

## Weiterentwicklung

- Zukünftige Erweiterungen könnten die Unterstützung weiterer Sprachen sowie die Verbesserung des PDF-Parsers beinhalten.

## Lizenz

Dieses Projekt steht unter der [GPL-Lizenz](LICENSE.txt).

## Autoren

- Luisgtr3
- Schneiderro
- Pfuetzenbaum
