import pygame
import random 

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [ Cactus(), Bird() ]

        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])
        Y_POS_OBST = +500, 5
        X_POS_OBST = 1000, 500
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):

                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count +=1
                    game.sound_game_over.play()
                    break
                elif game.player.type == "hammer":
                    self.obstacles.remove(obstacle)
                    game.sound_power_up.play()
                elif game.player.type == "shield":
                    game.sound_power_up.play()
                    pass
                elif game.player.type == "charmander":
                    game.sound_power_up.play()
                    obstacle.rect.y = random.choice(Y_POS_OBST)
                    obstacle.rect.x = random.choice(X_POS_OBST)
                elif game.player.type == "charizard":
                    game.sound_power_up.play()
                    pass
                elif game.player.type == "heart":
                    if game.player.heart >= 1:
                        self.obstacles.remove(obstacle)
                        game.player.heart -= 1
                    else:
                        pygame.time.delay(500)
                        game.playing = False
                        game.death_count +=1
                        game.sound_game_over.play()
                        break

                elif game.player.type == "score":
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count +=1
                    game.sound_game_over.play()
                    break

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)