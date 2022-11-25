import pygame
import os

# Global Constants
TITLE = "Dino Nan Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_CHARMANDER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Charmander1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Charmander2.png")),
]

RUNNING_CHARIZARD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Charizard1 (2).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Charizard2 (2).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Charizard3 (2).png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/Charizard4 (2).png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
JUMPING_CHARMANDER = pygame.image.load(os.path.join(IMG_DIR, "Dino/CharmanderJump.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_CHARMANDER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CharmanderDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/CharmanderDuck1.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

POKEMON_T = [
    pygame.image.load(os.path.join(IMG_DIR, "Pokemons/Pokemon1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Pokemons/Pokemon2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Pokemons/Pokemon3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

AERO = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Aero1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Aero2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))
POKEBALL = pygame.image.load(os.path.join(IMG_DIR, 'Other/Pokeball.png'))
POKEBALL2 = pygame.image.load(os.path.join(IMG_DIR, 'Other/Pokeball2.png'))
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/Heart.png'))
SMALL_HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
EXPLOSION = pygame.image.load(os.path.join(IMG_DIR, 'Other/explosion.png'))
GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))
SCORE = pygame.image.load(os.path.join(IMG_DIR, 'Other/coin.png'))


SOUND = os.path.join(IMG_DIR, 'Sound/sound.mp3')
SOUND_JUMP = os.path.join(IMG_DIR, 'Sound/jump.wav')
SOUND_GAME_OVER = os.path.join(IMG_DIR, 'Sound/game_over.wav')
SOUND_POKEBALL = os.path.join(IMG_DIR, 'Sound/pokeball.wav')
SOUND_POWER_UP = os.path.join(IMG_DIR, 'Sound/coin.wav')
SOUND_POKEMON = os.path.join(IMG_DIR, 'Sound/pokemon.mp3')


BG_POKEMON = pygame.image.load(os.path.join(IMG_DIR, 'Other/Forest.jpg'))
BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))


DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"
CHARMANDER_TYPE = "charmander"
CHARIZARD_TYPE = "charizard"
HEART_TYPE = "heart"
SCORE_TYPE = "score"