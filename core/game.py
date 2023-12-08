import pygame
from enum import Enum
from core.renderer import Renderer
from core.scene import Scene

class GameState(Enum):
    NONE = None
    START = 0
    PLAY = 1
    PAUSE = 2
    GAME_OVER = 3


class Game:
    def __init__(self, config):
        self.config = config
        
        self.screen: pygame.Surface = pygame.display.set_mode(self.config.WINDOW_SIZE)
        pygame.display.set_caption(self.config.TITLE)

        if hasattr(self.config, "ICON"):
            icon = pygame.image.load(self.config.ICON).convert_alpha()
            pygame.display.set_icon(icon)

        self.clock: pygame.time.Clock = pygame.time.Clock()
        
        self.running: bool = False
        self.state: GameState = GameState.NONE

        self.renderer = Renderer()
        self.scene = Scene(self.config, self.setState, self.setRunningState)

    def setState(self, state: GameState) -> None:
        self.state = state

    def setRunningState(self, state: bool) -> None:
        self.running = state

    def run(self) -> None:
        self.running = True
        self.state = GameState.START

        while self.running:
            deltaTime = self.clock.tick(self.config.FPS) / 1000.0

            # game update & rendering
            self.scene.update(deltaTime)
            self.renderer.render(self.screen, self.scene)

            
            # process events
            self.scene.processEvents()

        pygame.display.quit()
        pygame.quit()