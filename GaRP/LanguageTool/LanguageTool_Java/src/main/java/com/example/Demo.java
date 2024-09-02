package com.example;
 import org.languagetool.JLanguageTool;
 import org.languagetool.language.GermanyGerman;
 import org.languagetool.rules.RuleMatch;
 import org.languagetool.rules.Rule;
 import org.languagetool.rules.spelling.SpellingCheckRule;

 import java.util.Arrays;
 import java.util.List;
 import java.io.IOException;

// Klasse zum kurzen Demonstrieren der Funktionalität der LanguageTool Java API  
// Speziell das Ignorieren von Wörtern und Phrasen mit der AcceptPhrases Methode
// Warnung: LanguageTool auf Java und Python sind unterschiedlich zu der offiziell angebotenen Version von LanguageTool (https://forum.languagetool.org/t/language-tool-java-or-python-wrapper-does-not-validate-all-grammar-check-which-is-getting-validated-via-https-languagetool-org/9378)
public class Demo 
{
    public static void main( String[] args ) throws IOException
    {
        // Default LanguageTool
        long startTime = System.currentTimeMillis();
        GermanyGerman germany = new GermanyGerman();
        String text = "Hir is ein Text voler Fehler. Der Hund isst sein lecker Steak und der Katze sitzt auf dem Sofa. Ich habe gehen in die Geschäft um Milch zu kaufen, aber es regnet draussen. \"Warum ist das Wetter so schlecht?\", frag er sich. Dann sah ich ein Freund und wir gingen zusammen. Er sagte, dass er hat eine neue Auto. Der Auto ist sehr schnell und rot. Wir haben spielen Fußball im Park und trinken Cola. Es war ein gut Tag, aber die Sonne scheint nicht. Also, das war mein Tag. Viellecht machen wir das wieder bald!";
        // Test 1 -> Temporäres Hinzufügen von Wörtern
        System.out.println("1. Check -> Rappenpappenvoll -> Fehler");
        JLanguageTool langTool = new JLanguageTool(germany);
        // Ausgeben aktuell deaktivierter Regeln -> Müssen gegebenenfalls noch aktiviert werden
        // WIP: Beim Default werden einige Kommafehler nicht erkannt..., evtl. noch Regeln aktivieren?
        System.out.println(langTool.getDisabledRules());
        System.out.println(langTool.getCategories());

        List<RuleMatch> matches = langTool.check(text);
        for (RuleMatch match : matches) {
            System.out.println("Potential error at characters " +
            match.getFromPos() + "-" + match.getToPos() + ": " +
            match.getMessage() + "-"+ match.getShortMessage());
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
        
        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Execution time: " + executionTime + " milliseconds");
    }
}