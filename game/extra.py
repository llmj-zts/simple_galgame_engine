import os
import unicodedata
from game.config import Display, Path


class Extra:
    def read_script(self):
        f = open(os.path.join(Path.PATH_SCRIPT, "text.py"), "r")
        text = ["请输入文本"]
        exec(f.read())
        return text

    def insert_str(self, original_string, position, substring):
        return original_string[:position] + substring + original_string[position:]

    def char_width(self, char):
        if char in Display.FONT_WIDTH_FIX:
            return Display.FONT_WIDTH_FIX[char]
        if unicodedata.east_asian_width(char) in ["W", "F"]:
            return 2
        elif unicodedata.east_asian_width(char) in ["N", "Na"]:
            return 1
        elif unicodedata.east_asian_width(char) == "H":
            return 0.5
        else:
            return 0

    def adapt_text_width(self, text, max_length):
        text_list = text.split("\n")
        for item_num in range(len(text_list)):
            length = 0
            n = 0
            string = text_list[item_num]
            for i in string:
                if i == "\n":
                    length = 0
                else:
                    length += self.char_width(i)
                if length > max_length:
                    string = self.insert_str(string, n, "\n")
                    length = self.char_width(i)
                    n += 1
                n += 1
            text_list[item_num] = string
        return "\n".join(text_list)
