import pygame
import os

# Global Constants
TITLE = "Chrome Luffy Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
OBSTACLE_Y_POS = 330
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

FONT_STYLE = "freesansbold.ttf"

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Luffy/parado/luffy parado 1.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 3.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 4.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 5.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 6.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 7.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 8.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/escudo/luffy correndo escudo.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 2.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/martelo/luffy correndo martelo.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/correndo/luffy correndo 2.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Luffy/combos/combo 4/luffy combo 51.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Luffy/escudo/luffy pulando escudo.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Luffy/martelo/luffy pulando martelo.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/combos/combo 5/luffy combo 57.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/combos/combo 5/luffy combo 58.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/escudo/luffy duck escudo2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/escudo/luffy duck escudo1.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/martelo/luffy duck martelo.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Luffy/combos/combo 5/luffy combo 57.png")),
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

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

RESET = pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))

DIE_SOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/die.ogg')
POWER_UP_SOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/powerUp.ogg')
JUMP_SOUND = pygame.mixer.Sound('dino_runner/assets/Sounds/jump.ogg')