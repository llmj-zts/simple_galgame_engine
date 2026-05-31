class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {}
        self.current_scene = None

    def register(self, name, scene):
        self.scenes[name] = scene

    def switch(self, name):
        if self.current_scene:
            self.current_scene.exit()

        self.current_scene = self.scenes.get(name)

        if self.current_scene:
            self.current_scene.enter()

    def draw(self):
        if self.current_scene:
            self.current_scene.draw()

    def update(self):
        if self.current_scene:
            result = self.current_scene.update()
            if result:
                self.switch(result)
