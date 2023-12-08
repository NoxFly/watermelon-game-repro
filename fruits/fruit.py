from pygame import Color, Surface, Rect
from pygame.draw import circle
from pygame.transform import scale
from typing import List
from core.vector import Vector2

class Fruit:
    image: Surface = None

    def __init__(self, color: Color, size: float = 2.0):
        self.static: bool = True
        self.name: str = "Fruit"
        
        self.sprite: tuple[int, int, int, int]  = (0, 0, 1, 1) # x, y, width, height in the image

        self.color: Color = color
        self.size: float = size

        self.position: Vector2 = Vector2(0, 0)
        self.speed: float = 0.0
        self.acceleration: float = 1000.0

    def update(self, fruits: 'List[Fruit]', deltaTime: float, bounds: tuple[int, int]) -> None:
        # if the fruit is a static object, don't update it
        if self.static:
            return
        
        # apply physics
        if self.position.y < bounds[1] - self.size:
            self.speed += self.acceleration * deltaTime
            self.position.y += 0.5 * self.speed * deltaTime


    def draw(self, surface: Surface) -> None:
        fruit_image = Fruit.image.subsurface(Rect(self.sprite))
        fruit_image = scale(fruit_image, (int(self.size), int(self.size)))
        
        surface.blit(fruit_image, self.position.tuple())
        
        # debug indicator
        # circle(surface, Color(255, 0, 0), self.position.tuple(), self.size / 2)