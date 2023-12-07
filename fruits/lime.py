from pygame import Color
from fruit import Fruit

class Lime(Fruit):
    def __init__(self):
        super().__init__(Color(173, 187, 105), 4.0)