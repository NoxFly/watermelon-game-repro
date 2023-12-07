from typing import List
from fruits.fruit import Fruit

class Scene:
    def __init__(self, config, setState: callable):
        self.config = config
        self.setState = setState
        self.fruits: List[Fruit] = []

    def update(self):
        for fruit in self.fruits:
            fruit.update(self.fruits)