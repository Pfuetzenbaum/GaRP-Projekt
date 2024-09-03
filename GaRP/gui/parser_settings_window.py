import customtkinter as ctk

class ParserSettingsWindow:
    def __init__(self, root, main_app):
        self.root = root
        self.main_app = main_app
        self.settings_window = ctk.CTkToplevel(self.root)
        self.settings_window.title("Parser Einstellungen")
        self.settings_window.geometry("400x600")

        self.create_widgets()

    def create_widgets(self):

        self.parsing_basic_setting_label = ctk.CTkLabel(self.settings_window, text="Parsing Grundeinstellung:")
        self.parsing_basic_setting_label.grid(row=0, column=0, padx=5, pady=5)

        self.parsing_basic_setting_var = ctk.StringVar(value=self.main_app.settings.parsing_basic_setting)
        if self.main_app.settings.parsing_basic_setting == "structured":
            self.parsing_basic_setting_var.set("Strukturiert")
        else:
            self.parsing_basic_setting_var.set("Seitenweise")
        self.parsing_basic_setting_optionmenu = ctk.CTkOptionMenu(self.settings_window, values=["Strukturiert", "Seitenweise"], variable=self.parsing_basic_setting_var)
        self.parsing_basic_setting_optionmenu.grid(row=0, column=1, padx=5, pady=5)

        self.starting_page_label = ctk.CTkLabel(self.settings_window, text="Startseite:")
        self.starting_page_label.grid(row=1, column=0, padx=5, pady=5)

        self.starting_page_entry = ctk.CTkEntry(self.settings_window)
        self.starting_page_entry.insert(0, self.main_app.settings.starting_page)
        self.starting_page_entry.grid(row=1, column=1, padx=5, pady=5)

        self.ending_page_label = ctk.CTkLabel(self.settings_window, text="Endseite:")
        self.ending_page_label.grid(row=2, column=0, padx=5, pady=5)

        self.ending_page_entry = ctk.CTkEntry(self.settings_window)
        self.ending_page_entry.insert(0, self.main_app.settings.ending_page)
        self.ending_page_entry.grid(row=2, column=1, padx=5, pady=5)
    	
        self.check_fontname_label = ctk.CTkLabel(self.settings_window, text="Schriftart prüfen:")
        self.check_fontname_label.grid(row=3, column=0, padx=5, pady=5)

        self.check_fontname_var = ctk.BooleanVar(value=self.main_app.settings.check_fontname)
        self.check_fontname_checkbox = ctk.CTkCheckBox(self.settings_window, text="", variable=self.check_fontname_var)
        self.check_fontname_checkbox.grid(row=3, column=1, padx=5, pady=5)

        self.first_lines_to_skip_label = ctk.CTkLabel(self.settings_window, text="Erste zu überspringende Zeilen:")
        self.first_lines_to_skip_label.grid(row=4, column=0, padx=5, pady=5)

        self.first_lines_to_skip_entry = ctk.CTkEntry(self.settings_window)
        self.first_lines_to_skip_entry.insert(0, self.main_app.settings.first_lines_to_skip)
        self.first_lines_to_skip_entry.grid(row=4, column=1, padx=5, pady=5)

        self.last_lines_to_skip_label = ctk.CTkLabel(self.settings_window, text="Letzte zu überspringende Zeilen:")
        self.last_lines_to_skip_label.grid(row=5, column=0, padx=5, pady=5)

        self.last_lines_to_skip_entry = ctk.CTkEntry(self.settings_window)
        self.last_lines_to_skip_entry.insert(0, self.main_app.settings.last_lines_to_skip)
        self.last_lines_to_skip_entry.grid(row=5, column=1, padx=5, pady=5)

        self.save_button = ctk.CTkButton(self.settings_window, text="Speichern", command=self.save_settings)
        self.save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=20)

        self.settings_window.attributes("-topmost", True) # Setze das Fenster auf die oberste Ebene

    def save_settings(self):
        try:
            parsing_basic_setting = self.parsing_basic_setting_var.get()
            if parsing_basic_setting == "Strukturiert":
                self.main_app.settings.parsing_basic_setting = "structured"
            elif parsing_basic_setting == "Seitenweise":
                self.main_app.settings.parsing_basic_setting = "pagewise"

            self.main_app.settings.starting_page = int(self.starting_page_entry.get())
            self.main_app.settings.ending_page = int(self.ending_page_entry.get())
            self.main_app.settings.first_lines_to_skip = int(self.first_lines_to_skip_entry.get())
            self.main_app.settings.last_lines_to_skip = int(self.last_lines_to_skip_entry.get())

            if self.main_app.settings.parsing_basic_setting == "structured":
                self.main_app.settings.check_fontname = self.check_fontname_var.get()

            print(self.main_app.settings.parsing_basic_setting)

            self.settings_window.destroy()
        except ValueError as e:
            # Handle invalid integer inputs
            error_message = "Invalid input: {}".format(e)
            ctk.CTkMessagebox.show_error("Error", error_message)
        except Exception as e:
            # Handle any other unexpected errors
            error_message = "An unexpected error occurred: {}".format(e)
            ctk.CTkMessagebox.show_error("Error", error_message)