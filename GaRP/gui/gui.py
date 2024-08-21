import customtkinter as ctk
from tkinter import filedialog, Menu, Text
import sys
import os
from tkinterdnd2 import DND_FILES, TkinterDnD

# Append the path to the top-level project directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Now the import should work
from GaRP.parser.pdfminer_text_extraction import extract_text_from_pdf_structured

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("CTk example")

        # add widgets to app
        self.button = ctk.CTkButton(self, command=self.button_click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

    # add methods to app
    def button_click(self):
        print("button click")


app = App()
app.mainloop()
