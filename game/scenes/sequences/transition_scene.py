import pygame
from game.interpreter.ImageLoad import load_transition
from game.scenes.base_scene import BaseScene
from game.ui.message import Message
from game.config import Display, GameStatus

"""
message(n[1],250,200,100,surface=title_surface,center=True)#章节标题
message(n[2],250,350,70,surface=title_surface,center=True)#章节名称
title_surface.blit(pygame.image.load(f"title\\{n[3]}.png").convert_alpha(),(750,200))#章节图片
"""


class TransitionScene(BaseScene):
    def __init__(self, screen):
        self.screen = screen
        self.title_surface = screen  # pygame.Surface((Display.WIDTH, Display.HEIGHT))

    def enter(self):
        print("到我出场啦")
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

    def update(self):
        return None

    def draw(self):
        self.msg_title.show()
        self.msg_chapter.show()
        self.title_surface.blit(self.background, (750, 200))

    def transition_anime_enter(self, image: pygame.Surface):
        alpha = 0
        while alpha < 255:
            self.screen.fill((0, 0, 0))
            alpha += 5
            image.set_alpha(alpha)
            self.screen.blit(image, (750, 200))
            pygame.display.flip()
