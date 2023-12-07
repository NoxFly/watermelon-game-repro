from pygame import Color
from fruit import Fruit

class Melon(Fruit):
    def __init__(self):
        super().__init__(Color(181, 210, 128), 10.0)