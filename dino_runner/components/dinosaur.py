import pygame
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_SHIELD

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

class Dinosaur:
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

    
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()
            
        if self.step_index > 10:
            self.step_index = 0
        
        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE] or user_input[pygame.K_w]) and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.dino_jump: 
            #Verifica se o usuario pressionou seta para baixo ou a tecla S e se dino_jump é Falso
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or (user_input[pygame.K_DOWN] or user_input[pygame.K_s])):
            #Pq não consigo por self.dino_duck no lugar de passar as Keys?
            #Verifica se o Dino esta pulando ou agachando
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 30 #Defini a posição vertical quando o Dino estiver agachado
        self.step_index += 1

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
