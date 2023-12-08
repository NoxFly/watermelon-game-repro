from pygame import Color
from fruits.fruit import Fruit


class Peach(Fruit):
    def __init__(self):
        super().__init__(Color(243, 154, 152), 100.0)
        self.name = "Peach"
        self.sprite = (352, 260, 156, 156)