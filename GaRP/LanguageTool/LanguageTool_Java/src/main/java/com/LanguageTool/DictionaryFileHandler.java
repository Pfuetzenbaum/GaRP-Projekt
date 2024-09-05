package com.LanguageTool;

import java.nio.file.*;
import java.io.IOException;
import java.util.*;

// Klasse zum Lesen und Schreiben von Wörtern in ein Dictionary-File
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