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
from py4j.java_gateway import JavaGateway, GatewayParameters
import time
import subprocess


class DictionaryManagerGateway:
    def __init__(self, settings):

        jar_path ="demo-1.0_new.jar"

        # Starte den Java Gateway-Server als Subprozess
        self.process = subprocess.Popen(['java', '-jar', jar_path])
        time.sleep(3)

        self.settings = settings
        gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25333))
        self.dictionary_manager_german = gateway.entry_point.getDictionaryManagerGerman()
        self.dictionary_manager_english = gateway.entry_point.getDictionaryManagerEnglish()
        self.dictionary_manager = self.get_dictionary_manager(self.settings.language)
       
    def get_dictionary_manager(self, language):
        if language == "Deutsch":
            return self.dictionary_manager_german
        elif language == "Englisch":
            return self.dictionary_manager_english
        else:
            raise ValueError(f"Ungültige Sprache: {language}")

    def set_dictionary_manager(self, language: str):
        """Setzt den Wörterbuchmanager basierend auf der angegebenen Sprache."""
        self.dictionary_manager = self._get_dictionary_manager(language)
    
    def stop_java_process(self):
        """Beende den Java-Prozess, wenn die Anwendung geschlossen wird."""
        self.process.kill()