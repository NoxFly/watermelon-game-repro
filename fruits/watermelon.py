from pygame import Color
from fruit import Fruit

class Watermelon(Fruit):
    def __init__(self):
        super().__init__(Color(62, 99, 11), 12.0)