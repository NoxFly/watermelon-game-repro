from pygame import Color
from fruits.fruit import Fruit

class Banana(Fruit):
    def __init__(self):
        super().__init__(Color(234, 186, 113), 50.0)
        self.name = "Banana"
        self.sprite = (24, 259, 85, 85)
