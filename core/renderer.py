from pygame import Surface, display
from core.scene import Scene

class Renderer:
    def __init__(self):
        pass

    def render(self, screen: Surface, scene: Scene):
        # draw background
        screen.fill(scene.config.BACKGROUND_COLOR)

        for fruit in scene.fruits:
            fruit.draw(screen)

        display.update()