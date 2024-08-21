package com.example;

import java.io.IOException;

import org.languagetool.language.GermanyGerman;

import py4j.GatewayServer;

public class DictionaryManagerEntryPoint {

    private DictionaryManager dictionaryManager;

    public DictionaryManagerEntryPoint() throws IOException {
        // Pfad auf eigenem Rechner ändern -> Relativer Pfad funktioniert nicht
        dictionaryManager = new DictionaryManager("/Users/luis/Library/CloudStorage/OneDrive-Personal/Dokumente/1_DHBW/5.Semester/Semesterprojekt/LanguageCheck/GaRP/LanguageTool/LanguageTool_Java/src/Dictionary/CustomDictionary", new GermanyGerman());
    }

    public DictionaryManager getDictionaryManager() {
        return dictionaryManager;
    }

    public static void main(String[] args) throws IOException {
        GatewayServer gatewayServer = new GatewayServer(new DictionaryManagerEntryPoint());
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}