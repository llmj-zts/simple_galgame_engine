import glob
import pygame
import os.path
from game.extra import Extra
from game.config import Path
from game.saved import Saved
from .base_scene import BaseScene


class GameScenes(BaseScene):
    def __init__(self, screen):
        self.text = Extra().read_script()
        self.screen = screen
        self.game_process = [0, 0]
        self.show_length = 0
        self.show_text = None

        self.image = {}
        for i in glob.glob(os.path.join(Path.PATH_IMAGE, "figure", "*.png")):
            self.image[os.path.basename(i).split(".")[0]] = pygame.image.load(
                i
            ).convert_alpha()

    def enter(self):
        self.game_process = Saved().load()

    def next(self):
        self.show_length = 0
        self.game_process[1] += 1
        if self.text[self.game_process[0]][self.game_process[1]][0] == "@P":
            self.game_process = [
                self.text[self.game_process[0]][self.game_process[1]][1],
                0,
            ]
        self.show_text = self.text[self.game_process[0]][self.game_process[1]]
        if not self.show_text[0] in ("@E", "@L", "@S", "@B", "@T", "@P"):
            self.show_text[2] = Extra().adapt_text_width(self.show_text[2], 56)
