from pygame import Color
from fruit import Fruit

class Apricot(Fruit):
    def __init__(self):
        super().__init__(Color(234, 128, 55), 6.0)