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
from views.main_window import MainWindow
from views.error_window import ErrorWindow


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.error_window = ErrorWindow(self.root)  # Initialisiere ErrorWindow hier
        
        try:
            self.main_window = MainWindow(self.root, self.error_window)
        except Exception as e:
            self.error_window.show_error_message("Fehler beim Initialisieren des Programms", str(e))  

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainApplication(root)
    root.mainloop()
