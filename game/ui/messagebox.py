import pygame
from typing import Optional


class MessageBox:
    def __init__(self, screen):
        self.msg: str = "请输入文本"
        self.x: int = 0
        self.y: int = 0
        self.s: int = 50
        self.color: tuple = (255, 255, 255)
        self.alpha: int = 255
        self.center: bool = False
        self.surface: Optional[pygame.Surface] = None
        self.screen: Optional[pygame.Surface] = screen
        self.atas: bool = True
        self.font: str = "wenquanyizenhei"

    def show(self):
        message = pygame.font.SysFont(self.font, self.s).render(
            self.msg, self.atas, self.color
        )

        if self.center:
            rect = message.get_rect(center=(self.x, self.y))
        else:
            rect = message.get_rect(center=(self.x, self.y))
            rect.x = self.x
            rect.y = self.y
        message.set_alpha(self.alpha)
        # 若不加对于screen的判断，虽然程序可以运行但检查器会报错
        if (self.surface is None) and (self.screen is not None):
            self.screen.blit(message, rect)
        elif self.surface:
            self.surface.blit(message, rect)
