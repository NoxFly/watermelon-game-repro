import pygame, threading, time
from typing import List
from random import randint
from pygame import mouse, image
from core.quadtree import Quadtree, QuadtreePoint
from fruits.fruit import Fruit
from fruits.fruit_order import fruit_order

class Scene:
    def __init__(self, config, setState: callable, setRunningState: callable):
        self.config = config
        self.setState = setState
        self.setRunningState = setRunningState

        self.fruits: List[Fruit] = []
        self.currentFruit: Fruit = None
        self.mousePosition = (0, 0)

        self.isInDeposit = False

        Fruit.image = image.load('assets/fruits_sprite.png').convert_alpha()

        self.createNewCurrentFruit()


    def update(self, deltaTime: float) -> None:
        self.mousePosition = mouse.get_pos()

        qt = Quadtree(0, 0, self.config.WINDOW_SIZE[0], self.config.WINDOW_SIZE[1], 4)

        maxFruitSize = 0

        for fruit in self.fruits:
            c = QuadtreePoint(fruit.position.x, fruit.position.y, fruit.size, fruit)
            qt.insert(c)

            if fruit.size > maxFruitSize:
                maxFruitSize = fruit.size

        for fruit in self.fruits:
            fruit.update(qt, deltaTime, self.config.WINDOW_SIZE, maxFruitSize/2)

        if self.currentFruit:
            self.currentFruit.position.set(self.mousePosition[0] - self.currentFruit.size / 2, self.config.FRUIT_DEPOSIT_Y)


    def processEvents(self) -> None:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                self.setRunningState(False)

            # if the event is a left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if not self.isInDeposit:
                    self.isInDeposit = True
                    self.currentFruit.static = False
                    self.fruits.append(self.currentFruit)
                    self.currentFruit = None

                    threading.Thread(target=lambda: (time.sleep(1), self.createNewCurrentFruit())).start()


    def createNewCurrentFruit(self) -> None:
        fruit = self.randomFruit()
        fruit.position.set(self.mousePosition[0], self.config.FRUIT_DEPOSIT_Y)
        self.currentFruit = fruit
        self.isInDeposit = False


    def randomFruit(self) -> Fruit:
        m = self.config.MAX_RANDOM_FRUIT_RANK
        r = randint(0, m)
        f = fruit_order[r]() # fruit_order[r] returns Apple (for instance) so we do Apple() do create a new random fruit instance
        return f