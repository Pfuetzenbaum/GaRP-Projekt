package com.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.languagetool.language.GermanyGerman;
import org.languagetool.rules.RuleMatch;

import com.example.DictionaryManager.FilteredRuleMatch;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

// Noch überarbeiten mit Tests zu Filehandlern
class DictionaryManagerTest {
    private DictionaryManager dictionaryManager;
    private static final String DICTIONARY_FILE_PATH = "src/Dictionary/CustomDictionaryTest";

    @BeforeEach
    void setUp() throws IOException {
        dictionaryManager = new DictionaryManager(DICTIONARY_FILE_PATH, new GermanyGerman());
    }

    @Test
    void testInitialDictionaryWordsAreIgnored() throws IOException {
        String word = "Wetttt";
        // Schauen ob das bereits im Wörterbuch vorhandene Wort bei Initialisierung zur Ignorierung hinzugefügt wurde
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }


    // Testen, ob das Wort korrekt als falsch erkannt wurde
    @Test
    void testCheckText() throws IOException {
        String text = "Alles purrfekt";
        List<RuleMatch> matches = dictionaryManager.checkText(text);
        assertEquals(6, matches.get(0).getFromPos());
    }

    @Test
    void testCheckTextFiltered() throws IOException {
        String text = "Hallo ich bin eine Testdatei und ich besitse einen Rechtschreibfehler und ein  Grammtikfehler";
        List<FilteredRuleMatch> filteredMatches = dictionaryManager.checkTextFiltered(text);

        assertNotNull(filteredMatches);
        assertFalse(filteredMatches.isEmpty());

        for (FilteredRuleMatch match : filteredMatches) {
            assertNotNull(match.getSentence());
            assertNotNull(match.getImprovement());
            assertNotNull(match.getAffectedPart());
            assertNotNull(match.getShortMessage());
            assertNotNull(match.getLongMessage());
        }
    }

    // Wort zum Wörterbuch hinzufügen und anschließen prüfen ob es den Fehler noch anzeigt
    // WIP: Überprüfung ob Wort auch im Wörterbuch vorhanden ist
    @Test
    void testAddWord() throws IOException {
        String word = "purfekt";
        dictionaryManager.addWord(word);
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }

    @Test
    void testIgnoreWordInSession() throws IOException {
        String word = "purfekt";
        dictionaryManager.ignoreWordInSession(word);
        // Assert that the word is now ignored
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }

    // Wort zum Wörterbuch hinzufügen und anschließend entfernen und prüfen ob es den Fehler noch anzeigt
    // WIP: Überprüfung ob Wort auch im Wörterbuch nicht mehr vorhanden ist
    @Test
    void testRemoveWord() throws IOException {
        String word = "testword";
        dictionaryManager.addWord(word);
        dictionaryManager.removeWord(word);
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }
}