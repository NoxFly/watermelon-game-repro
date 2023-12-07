from pygame import Color
from pygame.draw import circle

class Fruit:
    def __init__(self, color: Color, size: float = 2.0, position: tuple[int, int] = (0, 0)):
        self.position = position
        self.color = color
        self.size = size

    def update(self):
        pass

    def draw(self, surface):
        circle(surface, self.color, self.position, self.size / 2)