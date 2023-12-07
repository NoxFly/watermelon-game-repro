from pygame import Color
from fruit import Fruit


class Peach(Fruit):
    def __init__(self):
        super().__init__(Color(243, 154, 152), 8.0)