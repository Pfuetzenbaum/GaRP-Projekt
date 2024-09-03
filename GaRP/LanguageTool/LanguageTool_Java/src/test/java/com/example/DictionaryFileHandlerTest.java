package com.example;

import org.junit.jupiter.api.*;
import java.io.IOException;
import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

// Test class for DictionaryFileHandler -> Added words have to be manually removed to ensure the test works
public class DictionaryFileHandlerTest {
    private DictionaryFileHandler handler;
    private static final String TEST_DICTIONARY_PATH = "src/Dictionary/CustomDictionaryTest";

    @BeforeEach
    public void setUp() {
        handler = new DictionaryFileHandler(TEST_DICTIONARY_PATH);
    }

    @Test
    public void testReadDictionary() throws IOException {
        List<String> words = handler.readDictionary();
        assertNotNull(words);
        // Add more assertions based on what you expect the contents of the dictionary to be
    }

    @Test
    public void testWriteDictionary() throws IOException {
        List<String> words = Arrays.asList("test1", "test2", "test3");
        handler.writeDictionary(words);

        List<String> writtenWords = handler.readDictionary();
        //assertEquals(words, writtenWords);
    }

    @Test
    public void testDeleteWords() throws IOException {
        // Arrange
        String testWord = "test1";
        List<String> words = Arrays.asList(testWord, "test2", "test3");
        handler.writeDictionary(words); // Ensure the word is in the dictionary

        // Act
        handler.deleteWord(testWord);

        // Assert
        List<String> wordsAfterDeletion = handler.readDictionary();
        assertFalse(wordsAfterDeletion.contains(testWord));
    }
}