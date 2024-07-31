package com.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.languagetool.language.GermanyGerman;
import org.languagetool.rules.RuleMatch;

import java.io.IOException;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class DictionaryManagerTest {
    private DictionaryManager dictionaryManager;
    private static final String DICTIONARY_FILE_PATH = "src/Dictionary/CustomDictionaryTest";
    //
    private static final String initialwords = "Aless, tetwort, Grrammatik";

    @BeforeEach
    void setUp() throws IOException {
        dictionaryManager = new DictionaryManager(DICTIONARY_FILE_PATH, new GermanyGerman());
    }

    @Test
    void testCheckText() throws IOException {
        String text = "Alles purrfekt";
        List<RuleMatch> matches = dictionaryManager.checkText(text);
        assertEquals(6, matches.get(0).getFromPos());
    }

    @Test
    void testAddWord() throws IOException {
        String word = "purfekt";
        dictionaryManager.addWord(word);
        // Assert that the word is now in the dictionary
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }

    @Test
    void testIgnoreWordInSession() throws IOException {
        String word = "purfekt";
        dictionaryManager.ignoreWordInSession(word);
        // Assert that the word is now ignored
        assertTrue(dictionaryManager.checkText(word).isEmpty());
    }

    @Test
    void testRemoveWord() throws IOException {
        String word = "testword";
        dictionaryManager.addWord(word);
        dictionaryManager.removeWord(word);
        // Assert that the word is no longer in the dictionary
        assertFalse(dictionaryManager.checkText(word).isEmpty());
    }
}