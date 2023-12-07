from pygame import Color
from fruit import Fruit

class Eggplant(Fruit):
    def __init__(self):
        super().__init__(Color(112, 104, 143), 2.0)