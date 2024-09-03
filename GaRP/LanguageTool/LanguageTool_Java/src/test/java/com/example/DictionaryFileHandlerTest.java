package com.example;

import org.junit.jupiter.api.*;
import java.io.IOException;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;


public class DictionaryFileHandlerTest {
    private DictionaryFileHandler handler;
    private static final String TEST_DICTIONARY_PATH = "src/Dictionary/CustomDictionaryTest";

    @BeforeEach
    public void setUp() {
        handler = new DictionaryFileHandler(TEST_DICTIONARY_PATH);
    }

    // Testet ob Wörter in das Dictionary geschrieben werden können
    @Test
    public void testWriteDictionary() throws IOException {
        List<String> words = Arrays.asList("test1", "test2", "test3");
        handler.writeDictionary(words);

        List<String> writtenWords = handler.readDictionary();
        assertTrue(writtenWords.containsAll(words));
    }

    // Testet ob Wörter aus dem Dictionary gelöscht werden können
    @Test
    public void testDeleteWords() throws IOException {
        String testWord = "test1";
        List<String> words = Arrays.asList(testWord, "test2", "test3");
        handler.writeDictionary(words); 

        handler.deleteWord(testWord);

        List<String> wordsAfterDeletion = handler.readDictionary();
        assertFalse(wordsAfterDeletion.contains(testWord));
    }
}