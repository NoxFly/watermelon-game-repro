from pygame import Surface, display
from core.scene import Scene
from pygame.draw import line

class Renderer:
    def __init__(self):
        pass

    def render(self, screen: Surface, scene: Scene) -> None:
        # draw background
        screen.fill(scene.config.BACKGROUND_COLOR)

        # mouse position = next fruit deposit
        line(screen, (255, 255, 255, 128), (scene.mousePosition[0], 0), (scene.mousePosition[0], scene.config.WINDOW_SIZE[1]))
        scene.currentFruit.draw(screen)

        for fruit in scene.fruits:
            fruit.draw(screen)

        display.update()