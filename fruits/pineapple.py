from pygame import Color
from fruits.fruit import Fruit

class Pineapple(Fruit):
    def __init__(self):
        super().__init__(Color(255, 217, 149), 150.0)
        self.name = "Pineapple"
        self.sprite = (260, 0, 218, 255)