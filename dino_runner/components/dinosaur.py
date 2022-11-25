import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import SOUND_JUMP
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DUCKING_SHIELD, DEFAULT_TYPE, SHIELD_TYPE, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER
from dino_runner.utils.constants import CHARMANDER_TYPE, RUNNING_CHARMANDER, DUCKING_CHARMANDER, JUMPING_CHARMANDER, CHARIZARD_TYPE, RUNNING_CHARIZARD, HEART_TYPE, SCORE_TYPE

X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, CHARMANDER_TYPE: DUCKING_CHARMANDER, CHARIZARD_TYPE: RUNNING_CHARIZARD, HEART_TYPE: DUCKING, SCORE_TYPE: DUCKING}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, CHARMANDER_TYPE: JUMPING_CHARMANDER, CHARIZARD_TYPE: RUNNING_CHARIZARD, HEART_TYPE: JUMPING, SCORE_TYPE: JUMPING}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, CHARMANDER_TYPE: RUNNING_CHARMANDER, CHARIZARD_TYPE: RUNNING_CHARIZARD, HEART_TYPE: RUNNING, SCORE_TYPE: RUNNING}


class Dinosaur(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.jump_vel = JUMP_VEL
        self.heart = 0
        self.dino_duck = False #Passei a variavel dino_duck como Falsa
        self.setup_state()
        pygame.mixer.music.set_volume(0.01)
        self.sound_jump = pygame.mixer.Sound(SOUND_JUMP)

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
    
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()
                
        if self.step_index >= 9:
            self.step_index = 0
        
        if (DUCK_IMG[self.type] or RUN_IMG[self.type] or JUMP_IMG[self.type]) == JUMP_IMG[CHARIZARD_TYPE]:
            self.dino_rect.y = 10

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE] or user_input[pygame.K_w]) and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
            self.sound_jump.play()
        elif (user_input[pygame.K_DOWN] or user_input[pygame.K_s]) and not self.dino_jump: 
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        if JUMP_IMG[self.type] == JUMP_IMG[CHARIZARD_TYPE]:
            self.image = JUMP_IMG[self.type][self.step_index // 5]
        else:
            self.image = JUMP_IMG[self.type]

        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS + 30 #Defini a posição vertical quando o Dino estiver agachado
        self.step_index += 1
        self.dino_duck = False

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
