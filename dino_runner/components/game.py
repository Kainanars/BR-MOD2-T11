import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20
        self.score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.game_speed = 20 #Quando inicia o run denovo ele reseta os valores
        
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5
    
    def write_text(self, past_text, color, text_center, font_style = "freesansbold.ttf", font_size = 22):
        font = pygame.font.Font(font_style, font_size)
        text = font.render(past_text, True, color)
        text_rect = text.get_rect()             #Criei a função de escrever texto
        text_rect.center = text_center
        self.screen.blit(text, text_rect)

    def draw(self):
        self.clock.tick(FPS)
        self.draw_background()
        self.player.draw(self.screen)
        self.draw_score()
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

        if self.score > 500:
            self.screen.fill(("#000000"))
        else:
            self.screen.fill(("#F0FFFF"))

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        if self.score > 500:
            color = ("#F0FFFF")
        else:
            color = ("#000000")
            
        self.write_text(f"Score: {self.score}", color, (1000, 50))

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255,255,255))
        half_screen_heigth = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.write_text("Press any key to start", (0,0,0), (half_screen_width, half_screen_heigth))

        else:
            self.write_text(f"Press any key to restart", (0,0,0), (half_screen_width, half_screen_heigth))
            self.write_text(f"Score: {self.score}", (0,0,0), (half_screen_width, half_screen_heigth + 50), font_size=18 )
            self.write_text(f"Deaths: {self.death_count}", (0,0,0), (half_screen_width, half_screen_heigth + 80), font_size=18)


        pygame.display.update()
        self.handle_events_on_menu()