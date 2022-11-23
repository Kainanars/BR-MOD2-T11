import random

from dino_runner.components.obstacles.obstacle import Obstacle
#Importei o randon e a Class Obstacle

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0,2)#Ele faz um random para definir qual cacto vai usar
        super().__init__(image, self.type)
        self.rect.y = 300 #Valor encontrado no youtube, para que ele fique rente ao chão