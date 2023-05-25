import pygame
import os
import sys
import pygame

SIZE = WIDTH, HEIGHT = 1000, 890
N = 18
EMPTY = 0
BRICK = 1
IRON = 2
PLAYER = 3
ENEMY = 4
FPS = 60
CELL_SIZE = 55
EGG_SIZE = (30, 50)
PLAYER_SIZE = (100, 200)
CHICKEN_SIZE = (80, 100)
STICK_SIZE = (300, 50)

ALL_SPRITES = pygame.sprite.Group()
TEXTURE_GROUP = pygame.sprite.Group()
EGG_GROUP = pygame.sprite.Group()
STICK_GROUP = pygame.sprite.Group()
# SHIELD_BONUS_GROUP = pygame.sprite.Group()
# TANK_GROUP = pygame.sprite.Group()
# ENEMY_TANK_GROUP = pygame.sprite.Group()
# COOLDOWN_BONUS_GROUP = pygame.sprite.Group()


SCREEN = pygame.display.set_mode(SIZE)
SURFACE = pygame.Surface(SIZE)


def load_image(name, colorkey=None):
    """Функция загрузки изображения"""
    fullname = os.path.join("origin", "media", 'img', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    image = pygame.image.load(fullname)
    return image


def load_sound(name):
    fullname = os.path.join("origin", "media", 'music', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    pygame.mixer.music.load(fullname)


def make_sound(name):
    """Функция загрузки музыки"""
    fullname = os.path.join("origin", "media", 'music', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    sound = pygame.mixer.Sound(fullname)
    return sound


def load_file(filename):
    fullname = os.path.join("origin", "media", filename)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        raise FileNotFoundError
    return fullname