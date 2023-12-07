from pygame import Color
from fruit import Fruit

class Banana(Fruit):
    def __init__(self):
        super().__init__(Color(234, 186, 113), 5.0)