import pygame
import os.path

from game.config import Display, Path
from game.saved import Saved
from .base_scene import BaseScene
from game.ui.button import Button
from game.ui.messagebox import MessageBox


class TitleScene(BaseScene):
    def __init__(self, screen):
        self.screen = screen
        self.avoid_mouse = False

        self.title_background = pygame.image.load(
            os.path.join(Path.PATH_IMAGE_TRANSITION, "sakura_slope.png")
        ).convert_alpha()

        self.continue_btn = Button(screen)
        self.continue_btn.msg = "继续游戏"
        self.continue_btn.pos = (150, 350)
        self.continue_btn.text_size = 60

        self.game_start_btn = Button(screen)
        self.game_start_btn.msg = "从头开始"
        self.game_start_btn.pos = (150, 550)
        self.game_start_btn.text_size = 60

    def enter(self):
        self.msg = MessageBox(self.screen)
        self.msg.msg = "GALGAME模板"
        self.msg.x = 500
        self.msg.y = 100
        self.msg.s = 70
        self.msg.center = True

        self.msg.show()

    def exit(self):
        temp_screen = pygame.Surface((Display.WIDTH, Display.HEIGHT))
        temp_screen.blit(self.screen, (0, 0))

    def update(self):
        if self.game_start_btn.pressed():
            Saved().save()
            return "game"
        if self.continue_btn.pressed():
            return "game"

    def draw(self):
        self.screen.blit(self.title_background, (0, 0))
        self.game_start_btn.blit()
        self.continue_btn.blit()
        self.msg.show()
