import pygame
import random 
#Importei o random
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import LargeCactus 
from dino_runner.components.obstacles.bird import Bird
#Importei a Class LargeCactus e Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_random = random.randint(0, 2)
        #Esse obstacle_random é para colocar um obstaculo aleatório
        if len(self.obstacles) == 0:         
            if obstacle_random == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif obstacle_random == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif obstacle_random == 2:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)      
        

    