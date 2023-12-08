from pygame import Color
from fruits.fruit import Fruit

class Apricot(Fruit):
    def __init__(self):
        super().__init__(Color(234, 128, 55), 70.0)
        self.name = "Apricot"
        self.sprite = (108, 259, 110, 110)
