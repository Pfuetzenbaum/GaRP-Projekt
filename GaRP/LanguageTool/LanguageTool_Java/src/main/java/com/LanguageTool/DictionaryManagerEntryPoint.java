package com.LanguageTool;

import java.io.IOException;

import org.languagetool.language.GermanyGerman;
import org.languagetool.language.BritishEnglish;

import py4j.GatewayServer;

public class DictionaryManagerEntryPoint {

    private DictionaryManager dictionaryManagerGerman;
    private DictionaryManager dictionaryManagerEnglish;

    public DictionaryManagerEntryPoint() throws IOException {
        dictionaryManagerGerman = new DictionaryManager("CustomDictionaryGerman", new GermanyGerman());
        dictionaryManagerEnglish = new DictionaryManager("CustomDictionaryEnglish", new BritishEnglish());
    }

    public DictionaryManager getDictionaryManagerGerman() {
        return dictionaryManagerGerman;
    }

    public DictionaryManager getDictionaryManagerEnglish() {
        return dictionaryManagerEnglish;
    }

    public static void main(String[] args) throws IOException {
        String currentWorkingDirectory = System.getProperty("user.dir");
        System.out.println("Current working directory: " + currentWorkingDirectory + "/" + "app/integrations/lib/Dictionary/CustomDictionaryGerman");
        GatewayServer gatewayServer = new GatewayServer(new DictionaryManagerEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}