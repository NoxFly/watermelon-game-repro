from pygame import Color
from fruits.fruit import Fruit

class Lime(Fruit):
    def __init__(self):
        super().__init__(Color(173, 187, 105), 50.0)
        self.name = "Lime"
        self.sprite = (9, 353, 78, 76)
