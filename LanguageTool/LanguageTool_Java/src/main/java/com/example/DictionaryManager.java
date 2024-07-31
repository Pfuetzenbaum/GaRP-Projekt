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
    JLanguageTool languageTool;
    GermanyGerman german;

    public DictionaryManager(String dictionaryFilePath, GermanyGerman german) {
        dictionaryHandler = new DictionaryFileHandler(dictionaryFilePath);
        languageTool = new JLanguageTool(german);
    }

    public void initLanguageTool(GermanyGerman german) throws IOException {
        german = new GermanyGerman();
        languageTool = new JLanguageTool(german);
    }

    public List<RuleMatch> checkText(String text) throws IOException{
        List<RuleMatch> matches = languageTool.check(text);
        return matches;
    }

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

    public void ignoreWordInSession(String word) {
        for (Rule rule : languageTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
            List<String> wordsToIgnore = Arrays.asList(word);
            ((SpellingCheckRule)rule).acceptPhrases(wordsToIgnore);
            }
        }
    }

    // WIP: Weg finden ohne das Tool neu zu starten?
    // Sonst muss das Ganze neu initialisiert werden
    public void removeWord(String word) throws IOException {
        dictionaryHandler.deleteWord(word);
    }
}