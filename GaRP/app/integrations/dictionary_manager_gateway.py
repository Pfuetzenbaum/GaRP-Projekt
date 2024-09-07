from py4j.java_gateway import JavaGateway, GatewayParameters
import subprocess

class DictionaryManagerGateway:
    # Sprachkonstanten
    DEUTSCH = "Deutsch"
    ENGLISCH = "Englisch"
    
    def __init__(self, settings):
        jar_path ="integrations/lib/demo-1.0.jar"

        # Starte den Java Gateway-Server als Subprozess
        self.process = subprocess.Popen(['java', '-jar', jar_path])

        self.settings = settings
        self.gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25333))
        self.dictionary_manager_german = None
        self.dictionary_manager_english = None
        self.dictionary_manager = self._get_dictionary_manager(self.settings.language)
    
    def _initialize_managers(self):
        """Initialisiere die Dictionary-Manager nur bei Bedarf."""
        if self.dictionary_manager_german is None:
            self.dictionary_manager_german = self.gateway.entry_point.getDictionaryManagerGerman()
        if self.dictionary_manager_english is None:
            self.dictionary_manager_english = self.gateway.entry_point.getDictionaryManagerEnglish()

    def _get_dictionary_manager(self, language: str):
        """Gibt den Wörterbuchmanager basierend auf der Sprache zurück."""
        self._initialize_managers()
        if language == self.DEUTSCH:
            return self.dictionary_manager_german
        elif language == self.ENGLISCH:
            return self.dictionary_manager_english
        else:
            raise ValueError(f"Ungültige Sprache: {language}")

    def set_dictionary_manager(self, language: str):
        """Setzt den Wörterbuchmanager basierend auf der angegebenen Sprache."""
        self.dictionary_manager = self._get_dictionary_manager(language)
    