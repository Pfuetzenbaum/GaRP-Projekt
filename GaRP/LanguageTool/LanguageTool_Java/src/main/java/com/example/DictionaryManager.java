package com.example;

import java.io.IOException;
import java.util.*;

import org.languagetool.JLanguageTool;
import org.languagetool.Language;
import org.languagetool.rules.RuleMatch;
import org.languagetool.rules.Rule;
import org.languagetool.rules.spelling.SpellingCheckRule;

public class DictionaryManager {
    private DictionaryFileHandler dictionaryHandler;
    private JLanguageTool languageTool;

    // Klasse für die Rückgabe der gefilterten Matches
    class FilteredRuleMatch {
        private String sentence;
        private String improvement;
        private String affectedPart;
        private String shortMessage;
        private String longMessage;
    
        public FilteredRuleMatch(String sentence, String improvement, String affectedPart, String shortMessage, String longMessage) {
            this.sentence = sentence;
            this.improvement = improvement;
            this.affectedPart = affectedPart;
            this.shortMessage = shortMessage;
            this.longMessage = longMessage;
        }
    
        public String getSentence() {
            return sentence;
        }
    
        public String getImprovement() {
            return improvement;
        }
    
        public String getAffectedPart() {
            return affectedPart;
        }
    
        public String getShortMessage() {
            return shortMessage;
        }
    
        public String getLongMessage() {
            return longMessage;
        }
    }

    // Bei der Initialisierung wird das Dictionary eingelesen und die Wörter als Ausnahmen für die Rechtschreibprüfung hinzugefügt
    // Lanuage wird als allgemeines Objekt initialisiert, die spezifischen Sprachen erben von diesen und können so initialisiert werden
    // Für Deutsch: new GermanyGerman()
    // Für Englisch: new BritishEnglish()
    public DictionaryManager(String dictionaryFilePath, Language language) throws IOException {
        dictionaryHandler = new DictionaryFileHandler(dictionaryFilePath);
        languageTool = new JLanguageTool(language);
        addIgnoredWordsFromDictionary();
    }

    // Methode zum Ignorieren der bereits vorhandenen Wörter aus dem Dictionary
    // Lediglich intern genutzt
    private void addIgnoredWordsFromDictionary() throws IOException {
        List<String> words = dictionaryHandler.readDictionary();
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
                ((SpellingCheckRule)rule).acceptPhrases(words);
            }
        }
    }

    // Methode zum Prüfen des Textes auf Rechtschreib-/Grammatikfehler
    // WIP: Mit Robin abkkären, welche Rückgabewerte benötigt werden
    // Wenn das eigentliche fehlerhafte Wort zurückgegeben werden soll, muss eine Anpassung vorgenommen werden
    public List<RuleMatch> checkText(String text) throws IOException{
        List<RuleMatch> matches = languageTool.check(text);
        return matches;
    }

    // Methode zum Prüfen des Textes auf Rechtschreib-/Grammatikfehler und Rückgabe der gefilterten Matches
    public List<FilteredRuleMatch> checkTextFiltered(String text) throws IOException {
        List<RuleMatch> matches = languageTool.check(text);
        List<FilteredRuleMatch> filteredMatches = new ArrayList<>();
    
        for (RuleMatch match : matches) {
            String sentence = match.getSentence().toString();
            String improvement = match.getSuggestedReplacements().isEmpty() ? "" : match.getSuggestedReplacements().get(0);
            String affectedPart = sentence.substring(match.getFromPosSentence(), match.getToPosSentence());
            String shortMessage = match.getShortMessage();
            String longMessage = match.getMessage();
            filteredMatches.add(new FilteredRuleMatch(sentence, improvement, affectedPart, shortMessage, longMessage));
        }
        return filteredMatches;
    }

    // Methode zum Hinzufügen eines Wortes zum Dictionary zum dauerhaften Ignorieren
    // WIP: Funktion einbauen: Nur Fehler die Rechtschreibfehler sind, dürfen hinzugefügt werden -> 
    // Sonst werden Kommafehler etc. auch hinzugefügt -> Mit Robin abklären -> Fügt er vlt. den Button dynamisch ein?
    public void addWord(String word) throws IOException {
        List<String> words = dictionaryHandler.readDictionary();
        words.add(word);
        dictionaryHandler.writeDictionary(words);
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
            List<String> wordsToIgnore = Arrays.asList(word);
            ((SpellingCheckRule)rule).acceptPhrases(wordsToIgnore);
            }
        }
    }

    // Methode zum Ignorieren eines Wortes in der aktuellen Session
    // WIP: Funktion einbauen: Nur Fehler die Rechtschreibfehler sind, dürfen hinzugefügt werden
    public void ignoreWordInSession(String word) {
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
            List<String> wordsToIgnore = Arrays.asList(word);
            ((SpellingCheckRule)rule).acceptPhrases(wordsToIgnore);
            }
        }
    }

    // Methode zum Entfernen eines Wortes aus dem Dictionary
    // Nur Funktionell nach Neustart des LTs 
    // Da hier das Dictionary neu eingelesen werden muss
    public void removeWord(String word) throws IOException {
        dictionaryHandler.deleteWord(word);
    }


}