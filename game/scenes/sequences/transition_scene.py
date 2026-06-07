import pygame
import time
from game.interpreter.ImageLoad import load_transition
from game.interpreter.solver import Solver
from game.scenes.base_scene import BaseScene
from game.ui.message import Message
from game.saves import saved
from game.config import GameStatus


class TransitionScene(BaseScene):
    def __init__(self, screen):
        self.screen = screen
        self.timer = 0
        self.title_surface = screen  # pygame.Surface((Display.WIDTH, Display.HEIGHT))
        self.solve = Solver()

    def enter(self):
        self.chapter = GameStatus.GAMESTATES.current_show_name
        self.title = GameStatus.GAMESTATES.current_show_text
        self.background_name = GameStatus.GAMESTATES.current_background
        self.background = load_transition(self.background_name)

        self.msg_chapter = Message(self.screen)
        self.msg_chapter.msg = self.chapter
        self.msg_chapter.x = 250
        self.msg_chapter.y = 200
        self.msg_chapter.size = 100
        self.msg_chapter.center = True
        self.msg_chapter.surface = self.title_surface

        self.msg_title = Message(self.screen)
        self.msg_title.msg = self.title
        self.msg_title.x = 250
        self.msg_title.y = 350
        self.msg_title.size = 70
        self.msg_title.center = True
        self.msg_title.surface = self.title_surface

        self.transition_anime_enter(self.background)
        self.msg_title.show()
        self.msg_chapter.show()

    def update(self):
        if self.timer > 50:
            next_scene = self.solve.next()
            saved.save(GameStatus.GAMESTATES)
            print(next_scene)
            if next_scene != "none":
                return next_scene

    def exit(self):
        self.transition_anime_exit(self.background)

    def draw(self):
        self.title_surface.blit(self.background, (750, 200))
        self.timer += 1

    def transition_anime_enter(self, image: pygame.Surface):
        alpha = 0
        while alpha < 255:
            self.screen.fill((0, 0, 0))
            alpha += 5
            image.set_alpha(alpha)
            self.screen.blit(image, (750, 200))
            pygame.display.flip()

    def transition_anime_exit(self, image: pygame.Surface):
        alpha = 255
        while alpha > 0:
            self.screen.fill((0, 0, 0))
            alpha -= 5
            image.set_alpha(alpha)
            self.screen.blit(image, (750, 200))
            pygame.display.flip()
