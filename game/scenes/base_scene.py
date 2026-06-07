from typing import Optional

import pygame


class BaseScene:
    def __init__(self, screen):
        self.screen = screen

    def enter(self):
        pass

    def exit(self) -> None | str:
        pass

    def draw(self):
        pass

    def update(self) -> Optional[str]:
        self.screen.fill((0, 0, 0))

    def alpha_anime_exit(self, image: pygame.Surface):
        alpha = 255
        while alpha > 0:
            self.screen.fill((0, 0, 0))
            alpha -= 5
            image.set_alpha(alpha)
            self.screen.blit(image, (0, 0))
            pygame.display.flip()

    def alpha_anime_enter(self, image: pygame.Surface):
        alpha = 0
        while alpha < 255:
            self.screen.fill((0, 0, 0))
            alpha += 5
            image.set_alpha(alpha)
            self.screen.blit(image, (0, 0))
            pygame.display.flip()
