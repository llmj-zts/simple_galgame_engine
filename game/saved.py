import pickle
import os

from game.config import Path


class Saved:
    def __init__(self):
        self.PATH = os.path.join(Path.PATH_SAVE, "save.sav")

    def save(self, c=1):
        game_process = [c, -1]
        s = {}
        s["process"] = game_process.copy()
        with open(self.PATH, "wb") as pickle_file:
            pickle.dump(s, pickle_file)
        return game_process

    def load(self):
        with open(self.PATH, "rb") as pickle_file:
            s = pickle.load(pickle_file)
        game_process = s["process"].copy()
        game_process[1] -= 1

        return game_process
