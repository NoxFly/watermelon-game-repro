from pygame import Color
from fruits.fruit import Fruit

class Eggplant(Fruit):
    def __init__(self):
        super().__init__(Color(112, 104, 143), 40.0)
        self.name = "Eggplant"
        self.sprite = (104, 378, 40, 40)