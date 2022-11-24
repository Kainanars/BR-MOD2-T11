import random
#Importei o random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import  BIRD, AERO
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.components.dinosaur import Dinosaur


print("Bird", Dinosaur().mode_pokemon)

if Dinosaur().mode_pokemon:
    img = AERO
else:
    img = BIRD


#Importei o random, a Classe Obstacle, e a listas BIRD e o tamanho da Tela
class Bird(Obstacle):
    BIRD_Y_POS = [230, 250, 290] 
    #Essa variavel recebe uma lista com os valores do eixo Y para que os passáros 
    #apareçam em 3 alturas difentes

        
    def __init__(self):
        self.type = 0 #self.type igual a 0 pois é uma animação e não 2 objetos diferentes
        super().__init__(img, self.type)
        self.rect.x = SCREEN_WIDTH #Valor de X é o tamanho da tela(Final)
        self.rect.y = random.choice(self.BIRD_Y_POS) #Ele faz um random e defini a altura do bird
        self.step_index = 0


    def draw(self, screen):
        #Mesma lógica do run() do dino, ele utiliza do step_index para fazer a animação
        if self.step_index >= 10:
            self.step_index = 0
        self.image = img[0] if self.step_index < 5 else img[1]
        self.step_index += 1
        screen.blit(self.image, (self.rect.x, self.rect.y))
        #ele atualiza o screen blit, com a imagem e posição do bird(gerando a animação)
