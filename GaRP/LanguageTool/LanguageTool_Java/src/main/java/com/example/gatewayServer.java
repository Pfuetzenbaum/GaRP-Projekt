package com.example;

import java.io.IOException;

import org.languagetool.language.GermanyGerman;

import py4j.GatewayServer;

public class gatewayServer {
    private static final String DICTIONARY_FILE_PATH = "src/Dictionary/CustomDictionaryTest";
        public static void main(String[] args) throws IOException {
        GatewayServer gatewayServer = new GatewayServer(new DictionaryManager(DICTIONARY_FILE_PATH,new GermanyGerman()));
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }
}
