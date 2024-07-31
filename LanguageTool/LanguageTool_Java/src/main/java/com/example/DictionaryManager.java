package com.example;

import java.io.IOException;
import java.util.*;

import org.languagetool.JLanguageTool;
import org.languagetool.language.GermanyGerman;
import org.languagetool.rules.RuleMatch;
import org.languagetool.rules.Rule;
import org.languagetool.rules.spelling.SpellingCheckRule;

public class DictionaryManager {
    private DictionaryFileHandler dictionaryHandler;
    private JLanguageTool languageTool;

    // Bei der Initialisierung wird das Dictionary eingelesen und die Wörter als Ausnahmen für die Rechtschreibprüfung hinzugefügt
    public DictionaryManager(String dictionaryFilePath, GermanyGerman german) throws IOException {
        dictionaryHandler = new DictionaryFileHandler(dictionaryFilePath);
        languageTool = new JLanguageTool(german);
        addIgnoredWordsFromDictionary();
    }

    public void addIgnoredWordsFromDictionary() throws IOException {
        List<String> words = dictionaryHandler.readDictionary();
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
                ((SpellingCheckRule)rule).acceptPhrases(words);
            }
        }
    }

    // WIP: Mit Robin abkkären, welche Rückgabewerte benötigt werden
    public List<RuleMatch> checkText(String text) throws IOException{
        List<RuleMatch> matches = languageTool.check(text);
        return matches;
    }

    // WIP: Funktion einbauen: Nur Fehler die Rechtschreibfehler sind, dürfen hinzugefügt werden
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

    // WIP: Funktion einbauen: Nur Fehler die Rechtschreibfehler sind, dürfen hinzugefügt werden
    public void ignoreWordInSession(String word) {
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
            List<String> wordsToIgnore = Arrays.asList(word);
            ((SpellingCheckRule)rule).acceptPhrases(wordsToIgnore);
            }
        }
    }

    // WIP: Weg finden ohne das Tool neu zu starten?
    // Sonst muss das Ganze neu initialisiert werden -> Bedeutet, dass auch Session-Wörter verloren gehen
    public void removeWord(String word) throws IOException {
        dictionaryHandler.deleteWord(word);
    }
}