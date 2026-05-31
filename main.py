import pygame
import sys

from game.game_loop import Game
from game.config import Display


def main():
    pygame.init()
    pygame.display.set_caption(Display.TITLE)
    screen = pygame.display.set_mode((Display.WIDTH, Display.HEIGHT), pygame.DOUBLEBUF)
    Game(screen).run()

    try:
        Game(screen).run()
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
