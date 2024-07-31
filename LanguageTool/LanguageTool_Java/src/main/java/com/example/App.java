package com.example;
/**
 * Hello world!
 *
 */

 import org.languagetool.JLanguageTool;
 import org.languagetool.language.GermanyGerman;
 import org.languagetool.rules.RuleMatch;
 import org.languagetool.rules.Rule;
 import org.languagetool.rules.spelling.SpellingCheckRule;

 import java.util.Arrays;
 import java.util.List;
 import java.io.IOException;


public class App 
{
    public static void main( String[] args ) throws IOException
    {
        long startTime = System.currentTimeMillis();
        GermanyGerman germany = new GermanyGerman();
        String text = "Lenny ist rappenpappenvoll";
        // Test 1 -> Temporäres Hinzufügen von Wörtern
        System.out.println("1. Check -> Rappenpappenvoll -> Fehler");
        JLanguageTool langTool = new JLanguageTool(germany);
        List<RuleMatch> matches = langTool.check(text);
        for (RuleMatch match : matches) {
            System.out.println("Potential error at characters " +
            match.getFromPos() + "-" + match.getToPos() + ": " +
            match.getMessage());
            System.out.println("Suggested correction(s): " +
            match.getSuggestedReplacements());
            }
        // comment in to use statistical ngram data:
        //langTool.activateLanguageModelRules(new File("/data/google-ngram-data"));
        for (Rule rule : langTool.getAllActiveRules()) {
            if (rule instanceof SpellingCheckRule) {
            List<String> wordsToIgnore = Arrays.asList("rappenpappenvoll");
            ((SpellingCheckRule)rule).acceptPhrases(wordsToIgnore);
            }
        }
        
        // 2. Check -> Rappenpappenvoll -> Kein Fehler
        System.out.println("2. Check -> Rappenpappenvoll -> Kein Fehler");
        matches = langTool.check(text);
        for (RuleMatch match : matches) {
            System.out.println("Potential error at characters " +
            match.getFromPos() + "-" + match.getToPos() + ": " +
            match.getMessage());
            System.out.println("Suggested correction(s): " +
            match.getSuggestedReplacements());
            }
        
        // Test 2 -> Dauerhaftes Hinzufügen von Wörtern
        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Execution time: " + executionTime + " milliseconds");
    }
}