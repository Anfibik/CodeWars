"""https://www.codewars.com/kata/57520361f2dac757360018ce"""


class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    def info(self):
        d = {"water": "wet", "fire": "fiery", "grass": "grassy"}
        if self.level <= 20:
            l = "weak"
        elif self.level > 50:
            l = "strong"
        else:
            l = "fair"

        return f"{self.name}, a {d[self.pkmntype]} and {l} Pokemon."
