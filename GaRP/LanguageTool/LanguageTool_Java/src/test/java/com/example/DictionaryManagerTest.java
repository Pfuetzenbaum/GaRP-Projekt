package com.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.languagetool.language.GermanyGerman;
import org.languagetool.rules.RuleMatch;

import com.example.DictionaryManager.FilteredRuleMatch;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class DictionaryManagerTest {
    private DictionaryManager dictionaryManager;
    private static final String DICTIONARY_FILE_PATH = "src/Dictionary/CustomDictionaryTest";

    @BeforeEach
    void setUp() throws IOException {
        dictionaryManager = new DictionaryManager(DICTIONARY_FILE_PATH, new GermanyGerman());
    }

    // Testen, ob das Wort korrekt als falsch erkannt wurde -> Abgleich mit der Position des Fehlers
    @Test
    void testCheckText() throws IOException {
        String text = "Alles purrfekt";
        List<RuleMatch> matches = dictionaryManager.checkText(text);
        assertEquals(6, matches.get(0).getFromPos());
    }

    // Testen ob bei Rechtschreibfehler alle Felder des FilteredRuleMatch Objekts befüllt sind
    @Test
    void testCheckTextFiltered() throws IOException {
        String text = "Ich besitse ein Auto";
        List<FilteredRuleMatch> filteredMatches = dictionaryManager.checkTextFiltered(text);
        assertNotNull(filteredMatches);
        for (FilteredRuleMatch match : filteredMatches) {
            assertNotNull(match.getSentence());
            assertNotNull(match.getImprovement());
            assertNotNull(match.getAffectedPart());
            assertNotNull(match.getShortMessage());
            assertNotNull(match.getLongMessage());
            assertNotNull(match.getFromPos());
            assertNotNull(match.getToPos());
        }
    }

    // Überprüfen ob Wort zum Wörterbuch hinzugefügt wird & ob es ignoriert wird
    @Test
    void testAddWord() throws IOException {
        String word = "purfekt";
        dictionaryManager.addWord(word);
        List<String> words = dictionaryManager.readDictionary();
        assertTrue(words.contains(word));
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }

    // Überprüfen ob Wort ignoriert wird
    @Test
    void testIgnoreWordInSession() throws IOException {
        String word = "purfekt";
        dictionaryManager.ignoreWordInSession(word);
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }
}