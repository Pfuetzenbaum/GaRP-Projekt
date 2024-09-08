// Copyright (C) 2024 Gantert, Schneider, Sewald

// Dieses Programm ist freie Software: Sie können es unter den Bedingungen
// der GNU General Public License, wie von der Free Software Foundation veröffentlicht,
// entweder Version 3 der Lizenz oder (nach Ihrer Wahl) jeder späteren Version
// weitergeben und/oder modifizieren.

// Dieses Programm wird in der Hoffnung verbreitet, dass es nützlich sein wird,
// aber OHNE JEDE GEWÄHRLEISTUNG; sogar ohne die implizite Gewährleistung der
// MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK. Siehe die
// GNU General Public License für weitere Details.

// Sie sollten eine Kopie der GNU General Public License zusammen mit diesem Programm
// erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.
package com.LanguageTool;

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
        private int fromPos;
        private int toPos;

        public FilteredRuleMatch(String sentence, String improvement, String affectedPart, String shortMessage, String longMessage, int fromPos, int toPos) {
            this.sentence = sentence;
            this.improvement = improvement;
            this.affectedPart = affectedPart;
            this.shortMessage = shortMessage;
            this.longMessage = longMessage;
            this.fromPos = fromPos;
            this.toPos = toPos;
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

        public int getFromPos() {
            return fromPos;
        }

        public int getToPos() {
            return toPos;
        }
    }

    // Bei der Initialisierung wird das Dictionary eingelesen und die Wörter als Ausnahmen für die Rechtschreibprüfung hinzugefügt
    // Language wird als allgemeines Objekt initialisiert, die spezifischen Sprachen erben von diesen und können so initialisiert werden
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
                ((SpellingCheckRule)rule).addIgnoreTokens(words);
            }
        }
    }

    // Methode zum Prüfen des Textes auf Rechtschreib-/Grammatikfehler
    public List<RuleMatch> checkText(String text) throws IOException{
        List<RuleMatch> matches = languageTool.check(text);
        return matches;
    }

    // Methode zum Prüfen des Textes auf Rechtschreib-/Grammatikfehler und Rückgabe der gefilterten Matches
    public List<FilteredRuleMatch> checkTextFiltered(String text) throws IOException {
        List<RuleMatch> matches = languageTool.check(text);
        List<FilteredRuleMatch> filteredMatches = new ArrayList<>();
    
        for (RuleMatch match : matches) {
            int fromPosSentence = match.getFromPosSentence();
            int toPosSentence = match.getToPosSentence();
            
            // Überprüfen, ob die Indizes gültig sind
            if (fromPosSentence >= 0 && toPosSentence >= 0 && fromPosSentence < toPosSentence && toPosSentence <= match.getSentence().toString().length()) {
                String sentence = match.getSentence().getText();
                String improvement = match.getSuggestedReplacements().isEmpty() ? "" : match.getSuggestedReplacements().toString();
                String affectedPart = sentence.substring(fromPosSentence, toPosSentence);
                String shortMessage = match.getShortMessage();
                String longMessage = match.getMessage();
                int fromPos = match.getFromPos();
                int toPos = match.getToPos();
                filteredMatches.add(new FilteredRuleMatch(sentence, improvement, affectedPart, shortMessage, longMessage,fromPos, toPos));
            }
        }
        return filteredMatches;
    }

    // Methode zum Hinzufügen eines Wortes zum Dictionary zum dauerhaften Ignorieren
    public void addWord(String word) throws IOException {
        List<String> words = dictionaryHandler.readDictionary();
        words.add(word);
        dictionaryHandler.writeDictionary(words);
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
            List<String> wordsToIgnore = Arrays.asList(word);
            ((SpellingCheckRule)rule).addIgnoreTokens(wordsToIgnore);
            }
        }
    }

    // Methode zum Ignorieren eines Wortes in der aktuellen Session
    public void ignoreWordInSession(String word) {
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
            List<String> wordsToIgnore = Arrays.asList(word);
            ((SpellingCheckRule)rule).addIgnoreTokens(wordsToIgnore);
            }
        }
    }

    // Methode zum Entfernen eines Wortes aus dem Dictionary
    // Nur Funktionell nach Neustart des LTs, da hier das Dictionary neu eingelesen werden muss
    public void removeWord(String word) throws IOException {
        dictionaryHandler.deleteWord(word);
    }

    // Methode zum Auslesen des Dictionaries
    public List<String> readDictionary() throws IOException {
        return dictionaryHandler.readDictionary();
    }
}