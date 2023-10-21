"""
Author: Core447
Year: 2023

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This programm comes with ABSOLUTELY NO WARRANTY!

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
import os
import json

class Page(dict):
    def __init__(self, json_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json_path = json_path
        self.load()

    def load(self):
        with open(self.json_path) as f:
            self.update(json.load(f))

    def save(self):
        # Make keys last element
        self.move_key_to_end(self, "keys")
        with open(self.json_path, "w") as f:
            json.dump(self, f, indent=4)

    def move_key_to_end(self, dictionary, key):
        if key in self:
            value = self.pop(key)
            self[key] = value

    def set_background(self, file_path, loop=True, fps=30, show=True):
        background = {
            "show": show,
            "path": file_path,
            "loop": loop,
            "fps": fps
        }
        self["background"] = background
        self.save()