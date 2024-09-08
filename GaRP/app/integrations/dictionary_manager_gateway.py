"""# Copyright (C) 2024 Gantert, Schneider, Sewald
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>"""
from py4j.java_gateway import JavaGateway, GatewayParameters  # Importiere die Py4J-Bibliothek, um Java-Methoden aus Python aufzurufen
import time  # Importiere das time-Modul, um Wartezeiten einzufügen
import subprocess  # Importiere subprocess, um den Java-Prozess zu starten

class DictionaryManagerGateway:
    """
    Diese Klasse stellt eine Verbindung zu einem Java-Wörterbuchmanager über Py4J her.
    Sie steuert den Start des Java-Prozesses, die Auswahl des Wörterbuchmanagers basierend auf der Sprache und das Beenden des Prozesses.
    """

    def __init__(self, settings):
        """
        Konstruktor für den DictionaryManagerGateway.

        :param settings: Die Anwendungseinstellungen, die die zu verwendende Sprache und andere Parameter enthalten.
        """
        jar_path = "demo-1.0.jar"  # Pfad zur JAR-Datei, die den Java-Wörterbuchmanager enthält

        # Starte den Java Gateway-Server als Subprozess
        self.process = subprocess.Popen(['java', '-jar', jar_path])  # Starte den Java-Prozess im Hintergrund
        time.sleep(5)  # Warte 3 Sekunden, um sicherzustellen, dass der Prozess vollständig gestartet ist

        self.settings = settings  # Speichere die Anwendungseinstellungen
        # Erstelle eine Verbindung zum Java Gateway
        gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25333))
        
        # Hole die Referenzen zu den deutschen und englischen Wörterbuchmanagern über den Java-Einstiegspunkt
        self.dictionary_manager_german = gateway.entry_point.getDictionaryManagerGerman()
        self.dictionary_manager_english = gateway.entry_point.getDictionaryManagerEnglish()
        
        # Setze den Wörterbuchmanager basierend auf der aktuellen Sprache in den Einstellungen
        self.dictionary_manager = self.get_dictionary_manager(self.settings.language)

    def get_dictionary_manager(self, language):
        """
        Gibt den passenden Wörterbuchmanager basierend auf der angegebenen Sprache zurück.

        :param language: Die Sprache, für die der Wörterbuchmanager benötigt wird (z. B. "Deutsch" oder "Englisch").
        :return: Der Wörterbuchmanager für die angegebene Sprache.
        """
        if language == "Deutsch":
            return self.dictionary_manager_german
        elif language == "Englisch":
            return self.dictionary_manager_english
        else:
            raise ValueError(f"Ungültige Sprache: {language}")  # Fehler, wenn eine nicht unterstützte Sprache angegeben wird

    def set_dictionary_manager(self, language: str):
        """
        Setzt den Wörterbuchmanager basierend auf der angegebenen Sprache.

        :param language: Die Sprache, für die der Wörterbuchmanager gesetzt werden soll.
        """
        self.dictionary_manager = self.get_dictionary_manager(language)  # Setze den Wörterbuchmanager basierend auf der Sprache

    def stop_java_process(self):
        """
        Beendet den Java-Prozess, wenn die Anwendung geschlossen wird.
        """
        self.process.kill()  # Beende den Java-Prozess, der mit `Popen` gestartet wurde
