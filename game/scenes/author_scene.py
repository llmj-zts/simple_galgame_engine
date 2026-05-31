from .base_scene import BaseScene
from ..ui.messagebox import MessageBox


class AuthorScene(BaseScene):
    def enter(self):
        pass

    def draw(self):
        msg = MessageBox(self.screen)
        msg.msg = "开发者:4564564"
        msg.x = 200
        msg.y = 300
        msg.show()
