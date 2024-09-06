package com.LanguageTool;

import java.io.IOException;

import org.languagetool.language.GermanyGerman;
import org.languagetool.language.BritishEnglish;

import py4j.GatewayServer;

public class DictionaryManagerEntryPoint {

    private DictionaryManager dictionaryManagerGerman;
    private DictionaryManager dictionaryManagerEnglish;

    public DictionaryManagerEntryPoint() throws IOException {
        dictionaryManagerGerman = new DictionaryManager("GaRP/LanguageTool/LanguageTool_Java/src/Dictionary/CustomDictionaryGerman", new GermanyGerman());
        dictionaryManagerEnglish = new DictionaryManager("GaRP/LanguageTool/LanguageTool_Java/src/Dictionary/CustomDictionaryEnglish", new BritishEnglish());
    }

    public DictionaryManager getDictionaryManagerGerman() {
        return dictionaryManagerGerman;
    }

    public DictionaryManager getDictionaryManagerEnglish() {
        return dictionaryManagerEnglish;
    }

    public static void main(String[] args) throws IOException {
        GatewayServer gatewayServer = new GatewayServer(new DictionaryManagerEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}