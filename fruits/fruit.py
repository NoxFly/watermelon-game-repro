from pygame import Color, Surface, Rect
from pygame.draw import circle
from pygame.transform import scale
from core.vector import Vector2
from core.quadtree import Quadtree

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

    def update(self, fruits: Quadtree, deltaTime: float, bounds: tuple[int, int], maxRadius: float) -> None:
        # if the fruit is a static object, don't update it
        if self.static:
            return
        
        # apply gravity
        if self.position.y < bounds[1] - self.size:
            self.speed += self.acceleration * deltaTime
            self.position.y += 0.5 * self.speed * deltaTime

        nearby_fruits = fruits.queryRadius(self.position.x, self.position.y, self.size/2 + maxRadius)

        for point in nearby_fruits:
            fruit = point.ref

            if fruit is self:
                continue

            distance = self.position.dist(fruit.position)

            if distance < self.size + fruit.size:  # collision detected
                direction = self.position.sub(fruit.position)
                direction.normalize_ip()
                force = direction.mult(100)  # force factor
                self.speed -= force.y
                fruit.speed += force.y


    def draw(self, surface: Surface) -> None:
        fruit_image = Fruit.image.subsurface(Rect(self.sprite))
        fruit_image = scale(fruit_image, (int(self.size), int(self.size)))
        
        surface.blit(fruit_image, self.position.tuple())
        
        # debug indicator
        # circle(surface, Color(255, 0, 0), self.position.tuple(), self.size / 2)