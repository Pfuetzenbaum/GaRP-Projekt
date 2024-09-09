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
        Files.write(dictionaryPath, words, StandardOpenOption.APPEND);
    }

    public void deleteWord(String word) throws IOException {
        List<String> words = readDictionary();
        words.remove(word);
        Files.write(dictionaryPath, words);
    }

   public void clearDictionary() throws IOException {
        Files.write(dictionaryPath, Collections.emptyList(), StandardOpenOption.TRUNCATE_EXISTING);
    }
}