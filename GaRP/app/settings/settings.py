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

class Settings:
    def __init__(self):
        self.parsing_basic_setting = "structured"
        self.starting_page = 1
        self.ending_page = 100
        self.check_fontname = False
        self.first_lines_to_skip = 0
        self.last_lines_to_skip = 0
        self.language = "Deutsch"
