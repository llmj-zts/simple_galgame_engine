from typing import Optional


class BaseScene:
    def __init__(self, screen):
        self.screen = screen

    def enter(self):
        pass

    def exit(self):
        pass

    def draw(self):
        pass

    def update(self) -> Optional[str]:
        self.screen.fill((0, 0, 0))
