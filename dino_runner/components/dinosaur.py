import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_SHIELD, RUNNING_CHARMANDER, JUMPING_CHARMANDER, DUCKING_CHARMANDER

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = JUMP_VEL
        self.dino_duck = False #Passei a variavel dino_duck como Falsa
        self.mode_pokemon = False
    
    def update(self, user_input):
        if self.mode_pokemon:
            self.pokemon_game()
        else:
            if self.dino_run:
                self.run()
            elif self.dino_duck:
                self.duck()
            elif self.dino_jump:
                self.jump()
                
        if self.step_index > 10:
            self.step_index = 0

        if user_input[pygame.K_CAPSLOCK]:
                self.mode_pokemon = True

        if user_input[pygame.K_LSHIFT]:
                self.mode_pokemon = False

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE] or user_input[pygame.K_w]) and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.dino_jump: 
            #Verifica se o usuario pressionou seta para baixo ou a tecla S e se dino_jump é Falso
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not self.dino_jump and not self.dino_duck:
            #Pq não consigo por self.dino_duck no lugar de passar as Keys?
            #Verifica se o Dino esta pulando ou agachando
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

    def run(self, img = RUNNING):
        self.image = img[0] if self.step_index < 5 else img[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self, img = JUMPING):
        self.image = img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self, img = DUCKING):
        self.image = img[0] if self.step_index < 5 else img[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 30 #Defini a posição vertical quando o Dino estiver agachado
        self.step_index += 1
        self.dino_duck = False
    
    def pokemon_game(self):
        if self.dino_run:
            self.run(img = RUNNING_CHARMANDER)
        elif self.dino_duck:
            self.duck(img = DUCKING_CHARMANDER)
        elif self.dino_jump:
            self.jump(img = JUMPING_CHARMANDER)


    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
