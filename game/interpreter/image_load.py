import pygame
import os.path
from game.ui.messagebox import MessageBox
from game.config import Display, Path


class ImageLoad:
    def __init__(self, screen):
        self.screen = screen
        self.image = {}

    def FigureLoad(self):
        pass

    def UiLoad(self, text):
        return pygame.image.load(
            os.path.join(Path.PATH_IMAGE_UI, f"{text}.png")
        ).convert_alpha()

    def BackgroundLoad(self, text):
        return pygame.image.load(
            os.path.join(Path.PATH_IMAGE_BACKGROUND), f"{text}.png"
        ).convert_alpha()

    def ImageLoad(self, n):
        if n[0] == "@B":
            if n[1] == "black":
                self.image["black"] = pygame.Surface((Display.WIDTH, Display.HEIGHT))
            else:
                self.image[n[1]] = self.BackgroundLoad(n[1])
        elif n[0] == "@T":
            title_surface = pygame.Surface((Display.WIDTH, Display.HEIGHT))

            title = MessageBox(self.screen)
            title.msg = n[1]
            title.x = 250
            title.y = 200
            title.s = 100
            title.surface = title_surface
            title.center = True

            name = MessageBox(self.screen)
            name.msg = n[2]
            name.x = 250
            name.y = 350
            name.s = 70
            name.surface = title_surface
            name.center = True

            title.show()
            name.show()

            title_surface.blit(
                pygame.image.load(
                    os.path.join(Path.PATH_IMAGE_TRANSITION, n[3])
                ).convert_alpha(),
                (750, 200),
            )  # 章节图片
            self.image["".join(n)] = title_surface
            return self.image
