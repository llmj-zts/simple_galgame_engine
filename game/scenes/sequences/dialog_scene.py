from game.interpreter.solver import Solver
from game.scenes import BaseScene
from game.saves import saved
from game.config import GameStatus


class DialogScene(BaseScene):
    def __init__(self, screen):
        # 你可能要用到的参数:
        # GameStatus.FIGURE_IMAGE:这个变量加载了全部人像,类型为Dict{str:pygame.Surface}
        # GameStatus.GAMESTATES.current_show_name:这个变量包含了现在需要显示的人物姓名,类型str
        # GameStatus.GAMESTATES.current_show_text:这个变量包含了现在需要显示的对话内容,类型str
        # GameStatus.GAMESTATES.current_background:这个变量包含了现在需要显示的背景,类型str
        # GameStatus.GAMESTATES.current_figure:这个变量包含了现在需要显示的人像名字,类型str
        self.screen = screen
        self.solve = Solver()

    def enter(self):
        # 这里负责管理进入到事件
        pass

    def exit(self):
        # 这里负责实现退出的事件
        # dialog退出是没有动画的,所以可以不用管这个函数
        # 不建议更改这个函数
        next_scene = self.solve.next()
        if next_scene != "none":
            saved.save(GameStatus.GAMESTATES)
            return next_scene

    def update(self):
        # 这里负责管理刷新
        # 你需要在这里实现检查是否按键点击，点击后就进入下一个场景
        # 如果返回None就什么都不会发生
        return (
            self.exit()
        )  # 注意，这里返回self.exit()就会进入下一个场景，你需要加入判断条件

    def draw(self):
        # 这里负责与绘画有关的事件
        # 你需要在这里添加show,blit等需要显示的
        pass
