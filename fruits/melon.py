from pygame import Color
from fruits.fruit import Fruit

class Melon(Fruit):
    def __init__(self):
        super().__init__(Color(181, 210, 128), 130.0)
        self.name = "Melon"
        self.sprite = (482, 0, 218, 240)
