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
        String text = "Die Relativitätstheorie, entwickelt von Albert Einstein zu Beginn des 20. Jahrhunderts, revolutionierte unser Verständnis von Raum, Zeit und Gravitation. Sie besteht aus zwei Haupttheorien: der speziellen Relativitätstheorie und der allgemeinen Relativitätstheorie.\n" + //
                        "\n" + //
                        "### Spezielle Relativitätstheorie\n" + //
                        "\n" + //
                        "Die spezielle Relativitätstheorie, veröffentlicht 1905, basiert auf zwei Grundpostulaten. Erstens: Die Gesetze der Physik sind in allen Inertialsystemen gleich. Ein Inertialsystem ist ein Bezugssystem, das sich mit konstanter Geschwindigkeit bewegt, ohne beschleunigt zu werden. Zweitens: Die Lichtgeschwindigkeit im Vakuum ist für alle Beobachter konstant, unabhängig von der Bewegung der Lichtquelle oder des Beobachters.\n" + //
                        "\n" + //
                        "Eine der bemerkenswertesten Konsequenzen dieser Theorie ist die Relativität der Gleichzeitigkeit. Zwei Ereignisse, die in einem Inertialsystem gleichzeitig erscheinen, müssen dies nicht in einem anderen Inertialsystem sein. Dies führte zu einem neuen Verständnis der Natur von Raum und Zeit, die nicht mehr als getrennte Entitäten betrachtet werden, sondern als ein zusammenhängendes Raum-Zeit-Kontinuum.\n" + //
                        "\n" + //
                        "Ein weiteres berühmtes Ergebnis der speziellen Relativitätstheorie ist die berühmte Formel \\(E=mc^2\\), die besagt, dass Energie und Masse äquivalent sind. Diese Gleichung impliziert, dass Masse eine Form von Energie ist, was zur Erkenntnis führte, dass selbst Ruhemasse eine riesige Menge an Energie darstellt. Diese Erkenntnis hat weitreichende Implikationen, von der Energiegewinnung bis hin zur Kernphysik.\n" + //
                        "\n" + //
                        "Die Theorie beschreibt auch die Zeitdilatation und Längenkontraktion. Zeitdilatation bedeutet, dass eine Uhr, die sich relativ zu einem Beobachter bewegt, langsamer geht als eine Uhr im Ruhestand des Beobachters. Längenkontraktion besagt, dass ein sich bewegendes Objekt in Bewegungsrichtung kürzer erscheint als im Ruhestand.\n" + //
                        "\n" + //
                        "### Allgemeine Relativitätstheorie\n" + //
                        "\n" + //
                        "Die allgemeine Relativitätstheorie, veröffentlicht 1915, erweitert die spezielle Relativitätstheorie auf beschleunigte Bezugssysteme und beschreibt die Gravitation als Krümmung der Raum-Zeit durch Masse und Energie. Anstatt Gravitation als eine Kraft zu betrachten, wie es Isaac Newton getan hatte, stellte Einstein fest, dass massive Objekte die Raum-Zeit krümmen, und diese Krümmung beeinflusst die Bewegung von Objekten.\n" + //
                        "\n" + //
                        "Ein anschauliches Beispiel ist das Bild von Raum-Zeit als einem Gummituch. Wenn ein schwerer Ball (stellvertretend für ein massives Objekt wie die Sonne) auf das Tuch gelegt wird, verformt sich das Tuch (die Raum-Zeit) und erzeugt eine Mulde. Ein kleinerer Ball (stellvertretend für ein kleineres Objekt wie die Erde), der auf dieses Tuch gerollt wird, bewegt sich aufgrund der Krümmung der Raum-Zeit in einer gekrümmten Bahn. Diese gekrümmte Bahn ist das, was wir als Umlaufbahn wahrnehmen.\n" + //
                        "\n" + //
                        "Die allgemeine Relativitätstheorie wurde durch mehrere Beobachtungen bestätigt. Eine der frühesten und bekanntesten Bestätigungen war die Beobachtung der Sonnenfinsternis von 1919. Dabei wurde das Licht von Sternen, das nahe an der Sonne vorbeilief, durch die Schwerkraft der Sonne abgelenkt, genau wie es die allgemeine Relativitätstheorie vorhersagt. Diese Lichtablenkung, bekannt als Gravitationslinseneffekt, ist inzwischen ein wichtiges Werkzeug in der Astronomie geworden, um Masseverteilungen im Universum zu untersuchen.\n" + //
                        "\n" + //
                        "Ein weiteres Phänomen, das durch die allgemeine Relativitätstheorie erklärt wird, ist die Zeitdilatation in starken Gravitationsfeldern, auch als gravitative Zeitdilatation bekannt. Uhren in der Nähe eines massiven Objekts, wie eines Planeten oder eines Sterns, ticken langsamer als Uhren, die weiter entfernt sind. Dies hat praktische Anwendungen, z. B. in der Satellitennavigation: GPS-Satelliten müssen Korrekturen für die Zeitdilatation sowohl aufgrund ihrer Geschwindigkeit (spezielle Relativitätstheorie) als auch ihrer Position im Gravitationsfeld der Erde (allgemeine Relativitätstheorie) vornehmen.\n" + //
                        "\n" + //
                        "### Kosmologische Konsequenzen\n" + //
                        "\n" + //
                        "Die allgemeine Relativitätstheorie hat auch tiefgreifende Konsequenzen für unser Verständnis des Universums als Ganzes. Sie bildet die Grundlage für die moderne Kosmologie, einschließlich des Urknallmodells, das besagt, dass das Universum vor etwa 13,8 Milliarden Jahren in einem extrem heißen und dichten Zustand begann und sich seitdem ausdehnt. Die Theorie liefert auch die Grundlage für das Verständnis der schwarzen Löcher, Regionen im Raum, in denen die Gravitationskraft so stark ist, dass nichts, nicht einmal Licht, entweichen kann.\n" + //
                        "\n" + //
                        "Einstein selbst war anfangs skeptisch gegenüber einigen kosmologischen Implikationen seiner Theorie, insbesondere der Vorstellung eines dynamischen, sich ausdehnenden Universums. Um ein statisches Universum zu ermöglichen, führte er eine kosmologische Konstante in seine Gleichungen ein. Später, als beobachtende Astronomen wie Edwin Hubble die Expansion des Universums bestätigten, bezeichnete Einstein die Einführung dieser Konstante als seinen \"größten Fehler\". Ironischerweise hat die moderne Astronomie Hinweise darauf gefunden, dass eine Form der kosmologischen Konstante, heute als dunkle Energie bekannt, tatsächlich existiert und für die beschleunigte Expansion des Universums verantwortlich sein könnte.\n" + //
                        "\n" + //
                        "### Philosophische Implikationen und Fazit\n" + //
                        "\n" + //
                        "Die Relativitätstheorie hat nicht nur die Physik, sondern auch die Philosophie beeinflusst. Sie stellt das traditionelle Konzept eines absoluten, unveränderlichen Raums und einer absoluten Zeit in Frage und zeigt, dass diese Größen relativ sind und vom Beobachter abhängen. Dies hat zu einer tieferen Diskussion über die Natur der Realität und unser Verständnis des Universums geführt.\n" + //
                        "\n" + //
                        "Insgesamt bleibt die Relativitätstheorie eine der größten intellektuellen Errungenschaften der Menschheitsgeschichte. Sie hat nicht nur unser physikalisches Weltbild revolutioniert, sondern auch technologische Innovationen inspiriert und unser Verständnis des Universums vertieft. Trotz ihrer Komplexität und den tiefgehenden theoretischen Einsichten ist sie durch Experimente und Beobachtungen gut bestätigt und bleibt ein fundamentales Werkzeug in der modernen Physik und Astronomie.";
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
        
        long endTime = System.currentTimeMillis();
        long executionTime = endTime - startTime;
        System.out.println("Execution time: " + executionTime + " milliseconds");
    }
}