from pygame import Color
from fruits.fruit import Fruit

class Apple(Fruit):
    def __init__(self):
        super().__init__(Color(255, 0, 0), 90.0)
        self.name = "Apple"
        self.sprite = (221, 258, 129, 139)
