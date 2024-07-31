package com.example;

import java.nio.file.*;
import java.io.IOException;
import java.util.*;

// Class to handle reading and writing to a dictionary file
// WIP: Functionality to not add double words?
public class DictionaryFileHandler {
    private Path dictionaryPath;

    public DictionaryFileHandler(String dictionaryFilePath) {
        dictionaryPath = Paths.get(dictionaryFilePath);
    }

    public List<String> readDictionary() throws IOException {
        return Files.readAllLines(dictionaryPath);
    }

    public void writeDictionary(List<String> words) throws IOException {
        Files.write(dictionaryPath, words);
    }

    public void deleteWord(String word) throws IOException {
        List<String> words = readDictionary();
        words.remove(word);
        writeDictionary(words);
    }
}