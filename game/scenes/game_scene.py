import time
from game.interpreter import ImageLoad
from game.interpreter.solver import Solver
from game.saves import saved
from game.config import GameStatus
from game.scenes.base_scene import BaseScene
from game.scenes.manage_scene import SceneManager
from game.scenes.sequences.transition_scene import TransitionScene


class GameScenes(BaseScene):
    def __init__(self, screen):
        self.screen = screen
        self.solve = Solver()

        self.manage_scene = SceneManager(self.screen)

        self.manage_scene.register("transition", TransitionScene(screen))
        self.manage_scene.register("dialog", TransitionScene(screen))
        self.manage_scene.register("choice", TransitionScene(screen))

    def enter(self):
        game_process = saved.load()
        GameStatus.GAMESTATES = game_process
        GameStatus.FIGURE_IMAGE = ImageLoad.load_all_figure()

        self.next()

    def next(self):
        next_scene = self.solve.next()
        if next_scene != "none":
            saved.save(GameStatus.GAMESTATES)
            self.manage_scene.switch(next_scene)
        print(GameStatus.GAMESTATES)
        self.next()

    def update(self):
        GameStatus.GAMESTATES.time = time.time()
        self.manage_scene.update()

    def draw(self):
        self.manage_scene.draw()

    def exit(self):
        self.next()
