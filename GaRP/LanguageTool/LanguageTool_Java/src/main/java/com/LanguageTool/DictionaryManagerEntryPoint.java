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

import java.io.IOException;

import org.languagetool.language.GermanyGerman;
import org.languagetool.language.BritishEnglish;

import py4j.GatewayServer;

public class DictionaryManagerEntryPoint {

    private DictionaryManager dictionaryManagerGerman;
    private DictionaryManager dictionaryManagerEnglish;

    public DictionaryManagerEntryPoint() throws IOException {
        dictionaryManagerGerman = new DictionaryManager("GaRP-Projekt/GaRP/LanguageTool/LanguageTool_Java/src/Dictionary/CustomDictionaryGerman", new GermanyGerman());
        dictionaryManagerEnglish = new DictionaryManager("GaRP-Projekt/GaRP/LanguageTool/LanguageTool_Java/src/Dictionary/CustomDictionaryEnglish", new BritishEnglish());
    }

    public DictionaryManager getDictionaryManagerGerman() {
        return dictionaryManagerGerman;
    }

    public DictionaryManager getDictionaryManagerEnglish() {
        return dictionaryManagerEnglish;
    }

    public static void main(String[] args) throws IOException {
        String currentWorkingDirectory = System.getProperty("user.dir");
        System.out.println("Current working directory: " + currentWorkingDirectory);
        GatewayServer gatewayServer = new GatewayServer(new DictionaryManagerEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}