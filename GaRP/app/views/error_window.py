"""Copyright (C) 2024 Gantert, Schneider, Sewald

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/> """

import customtkinter as ctk

class ErrorWindow:
    def __init__(self, root):
        self.root = root

    def show_error_message(self, title, message):
        error_window = ctk.CTkToplevel(self.root)
        error_window.title(title)
        error_window.geometry("400x200")
        error_window.attributes("-topmost", True)  # Setze das Fenster auf die oberste Ebene

        error_label = ctk.CTkLabel(error_window, text=message, wraplength=380)
        error_label.pack(padx=10, pady=10)