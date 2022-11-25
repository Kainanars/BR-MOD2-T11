import random

from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import  BIRD, AERO
from dino_runner.utils.constants import SCREEN_WIDTH


class Bird(Obstacle):
    BIRD_Y_POS = [230, 250, 290] 
 
    def __init__(self):
        self.type = 0 #self.type igual a 0 pois é uma animação e não 2 objetos diferentes
        super().__init__(BIRD, self.type)
        self.rect.x = SCREEN_WIDTH #Valor de X é o tamanho da tela(Final)
        self.rect.y = random.choice(self.BIRD_Y_POS) #Ele faz um random e defini a altura do bird
        self.step_index = 0

    def draw(self, screen):
        if self.step_index >= 10:
            self.step_index = 0
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.step_index += 1
        screen.blit(self.image, (self.rect.x, self.rect.y))