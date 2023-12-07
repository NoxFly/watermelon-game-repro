from pygame import Color
from fruit import Fruit


class Cherry(Fruit):
    def __init__(self):
        super().__init__(Color(172, 57, 52), 3.0)