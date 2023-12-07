from pygame import Color
from fruit import Fruit


class Apple(Fruit):
    def __init__(self):
        super().__init__(Color(255, 0, 0), 7.0)