from pygame import Color
from fruit import Fruit

class Pineapple(Fruit):
    def __init__(self):
        super().__init__(Color(255, 217, 149), 11.0)