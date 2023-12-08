from pygame import Color
from fruits.fruit import Fruit

class Watermelon(Fruit):
    def __init__(self):
        super().__init__(Color(62, 99, 11), 160.0)
        self.name = "Watermelon"
        self.sprite = (0, 0, 258, 258)