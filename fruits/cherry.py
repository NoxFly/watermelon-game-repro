from pygame import Color
from fruits.fruit import Fruit


class Cherry(Fruit):
    def __init__(self):
        super().__init__(Color(172, 57, 52), 40.0)
        self.name = "Cherry"
        self.sprite = (171, 378, 45, 45)