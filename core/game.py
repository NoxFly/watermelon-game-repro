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
        self.screen = pygame.display.set_mode(self.config.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.running = False
        self.state = GameState.NONE

        self.renderer = Renderer()
        self.scene = Scene(self.config, self.setState)

    def setState(self, state: GameState):
        self.state = state

    def run(self):
        self.running = True
        self.state = GameState.START

        while self.running:
            # game update & rendering
            self.scene.update()
            self.renderer.render(self.screen, self.scene)

            self.clock.tick(self.config.FPS)
            
            # process events
            self.processEvents()

        pygame.display.quit()
        pygame.quit()

    def processEvents(self):
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.running = False