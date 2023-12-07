from pygame import Color
from fruit import Fruit

class Coco(Fruit):
    def __init__(self):
        super().__init__(Color(161, 97, 69), 9.0)