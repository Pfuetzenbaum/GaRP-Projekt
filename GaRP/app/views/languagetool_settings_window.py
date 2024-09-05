import customtkinter as ctk

class LanguageToolSettingsWindow:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        self.settings_window = ctk.CTkToplevel(self.root)
        self.settings_window.title("Language Tool Einstellungen")
        self.settings_window.geometry("300x200")
        self.settings_window.attributes("-topmost", True) # Setze das Fenster auf die oberste Ebene

        self.create_widgets()

    def create_widgets(self):
        self.language_label = ctk.CTkLabel(self.settings_window, text="Sprache:")
        self.language_label.grid(row=0, column=0, padx=5, pady=5)

        self.language_var = ctk.StringVar()
        self.language_var.set(self.main_window.settings.language)  # Setze den aktuell eingestellten Wert

        self.language_option_menu = ctk.CTkOptionMenu(self.settings_window, values=["Deutsch", "Englisch"], variable=self.language_var)
        self.language_option_menu.grid(row=0, column=1, padx=5, pady=5)

        save_button = ctk.CTkButton(self.settings_window, text="Speichern", command=self.save_settings)
        save_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def save_settings(self):
        selected_language = self.language_var.get()
        # Save the selected language to your settings or database
        self.main_window.settings.language = selected_language
        self.main_window.dictionary_manager_gateway.dictionary_manager = self.main_window.dictionary_manager_gateway.get_dictionary_manager(selected_language)
        self.settings_window.destroy()  # Close the settings window