from py4j.java_gateway import JavaGateway, GatewayParameters

class DictionaryManagerGateway:
    def __init__(self, settings):
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
            raise ValueError("Ungültige Sprache")