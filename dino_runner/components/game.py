import pygame

from dino_runner.utils.constants import SOUND_POKEMON, SOUND, SOUND_GAME_OVER, SOUND_POKEBALL, SOUND_POWER_UP, BG_POKEMON, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, SCORE_TYPE, HEART_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager


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
        self.score_boost = 0
        self.max_score = 0
        self.death_count = 0
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.music = pygame.mixer.music.load(SOUND)
        #self.music_pokemon = pygame.mixer.music.load(SOUND_POKEMON)
        self.sound_game_over = pygame.mixer.Sound(SOUND_GAME_OVER)
        self.sound_power_up = pygame.mixer.Sound(SOUND_POWER_UP)
        self.sound_pokeball = pygame.mixer.Sound(SOUND_POKEBALL)
        pygame.mixer.music.set_volume(0.05)
        pygame.mixer.music.play(-1)

    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()
    
    def run(self):
        self.playing = True
        self.power_up_manager.reset_power_ups()
        self.obstacle_manager.reset_obstacles()
        self.score = 0
        self.score_boost = 0
        self.game_speed = 20 #Quando inicia o run denovo ele reseta os valores
        
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.update_max_score()

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
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2

    def update_max_score(self):
        if (self.score + self.score_boost) > self.max_score:
            self.max_score = (self.score + self.score_boost)
    
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
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
        self.screen.fill(("#87CEEB"))

    def draw_background(self):
        image_width = BG_POKEMON.get_width()
        self.screen.blit(BG_POKEMON, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG_POKEMON, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG_POKEMON, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def draw_score(self):
        color = ("#000000")
        self.write_text(f"Max Score: {self.max_score} | Score: {self.score + self.score_boost}", color, (930, 50), font_style="Score.ttf", font_size=18)

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 10000, 2)
            if time_to_show >= 0:                  
                self.write_text(
                    f"{self.player.type.capitalize()} enabled for {time_to_show} seconds", (0,0,0), (500,40),font_size=18)
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

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
            self.write_text("Press any key to start", "#00008B", (half_screen_width, half_screen_heigth), font_style="Pixel.ttf")    
        else:
            self.screen.blit(GAME_OVER, (half_screen_width -195, half_screen_heigth -  140))
            self.write_text(f"Press any key to restart", "#008000", (half_screen_width, half_screen_heigth), font_style="Pixel.ttf")
            self.write_text(f"Score : {self.score + self.score_boost}", (0,0,0), (half_screen_width, half_screen_heigth + 50), font_style="Pixel.ttf", font_size=18 )
            self.write_text(f"Max Score: {self.max_score}", (0,0,0), (half_screen_width, half_screen_heigth + 80), font_style="Pixel.ttf", font_size=18)
            self.write_text(f"Deaths: {self.death_count}", (0,0,0), (half_screen_width, half_screen_heigth + 110), font_style="Pixel.ttf", font_size=18)
        pygame.display.update()
        self.handle_events_on_menu()