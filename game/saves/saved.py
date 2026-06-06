import pickle
import os.path
from game.config import Path
from game.saves.game_data import GameStats


PATH = os.path.join(Path.PATH_SAVE, "save.sav")


def save(game_data: GameStats) -> None:
    with open(PATH, "wb") as file:
        pickle.dump(game_data, file)


def load() -> GameStats:
    with open(PATH, "rb") as file:
        game_data = pickle.load(file)
    return game_data
