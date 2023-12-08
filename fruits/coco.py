from pygame import Color
from fruits.fruit import Fruit

class Coco(Fruit):
    def __init__(self):
        super().__init__(Color(161, 97, 69), 110.0)
        self.name = "Coco"
        self.sprite = (510, 242, 160, 164)
