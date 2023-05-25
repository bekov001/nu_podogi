import random
import time
import pygame

from pygame import font

from src.origin.helpers import ALL_SPRITES, load_image, SCREEN, EGG_GROUP, \
    EGG_SIZE, STICK_GROUP, PLAYER_GROUP


# CELL_SIZE = 50


class LeftEgg(pygame.sprite.Sprite):
    """Вражеский танк"""
    def __init__(self, x, y, speed=0):
        super().__init__(ALL_SPRITES)
        self.add(EGG_GROUP)
        self.health = 100
        self.image = pygame.transform.scale(load_image("egg.png"),
                                            EGG_SIZE)
        self.def_image = pygame.transform.scale(load_image("egg.png"),
                                            EGG_SIZE)
        self.rect = pygame.Rect(x, y, *EGG_SIZE)
        self.angular = 0
        self.start = time.time()
        self.speed = speed
        # self.image = pygame.transform.scale(load_image("base/enemy_base.png"),
        #                                     (CELL_SIZE, CELL_SIZE))
        # self.music = music

    # def strike(self):
    #     """Функция стрельбы"""
    #     Strike(self.rect.center, self.enemy.rect.center, TANK_GROUP)
    #     self.music['shot'].play()

    def show_xp(self):
        """Функция показать здоровье танка"""
        pass
        # xp = self.health / 100
        # pygame.draw.rect(SCREEN, "green",
        #                  (self.rect.x, self.rect.y - 10, CELL_SIZE * xp, 5))
        # pygame.draw.rect(SCREEN, "red",
        #                  (self.rect.x + CELL_SIZE * xp,
        #                   self.rect.y - 10, CELL_SIZE - CELL_SIZE * xp, 5))


    def generate_direction(self, enemy_pos):
        pass
        # """Функция генерирует ход танка ИИ"""
        # if enemy_pos[0] > self.rect.center[0]:
        #     if enemy_pos[1] > self.rect.center[1]:
        #         dir = random.choice(
        #             [pygame.K_DOWN, pygame.K_RIGHT] * 3 +
        #             [pygame.K_RIGHT, pygame.K_LEFT,
        #              pygame.K_UP, pygame.K_DOWN])
        #     elif enemy_pos[1] < self.rect.center[1]:
        #         dir = random.choice([pygame.K_RIGHT, pygame.K_UP] * 3 +
        #                             [pygame.K_RIGHT, pygame.K_LEFT,
        #                              pygame.K_UP, pygame.K_DOWN])
        #     else:
        #         dir = random.choice([pygame.K_RIGHT, pygame.K_DOWN,
        #                              pygame.K_UP] * 3 +
        #                             [pygame.K_RIGHT, pygame.K_LEFT,
        #                              pygame.K_UP, pygame.K_DOWN])
        # elif enemy_pos[0] < self.rect.center[0]:
        #     if enemy_pos[1] > self.rect.center[1]:
        #         dir = random.choice([pygame.K_LEFT, pygame.K_DOWN] * 3 +
        #                             [pygame.K_RIGHT, pygame.K_LEFT,
        #                              pygame.K_UP, pygame.K_DOWN])
        #     elif enemy_pos[1] < self.rect.center[1]:
        #         dir = random.choice([pygame.K_LEFT, pygame.K_UP] * 3 +
        #                             [pygame.K_RIGHT, pygame.K_LEFT,
        #                              pygame.K_UP, pygame.K_DOWN])
        #     else:
        #         dir = random.choice([pygame.K_DOWN,
        #                              pygame.K_UP, pygame.K_LEFT] * 3 +
        #                             [pygame.K_RIGHT, pygame.K_LEFT,
        #                              pygame.K_UP, pygame.K_DOWN])
        # else:
        #     if enemy_pos[1] > self.rect.center[1]:
        #         dir = random.choice([pygame.K_DOWN, pygame.K_LEFT,
        #                              pygame.K_RIGHT] * 3 +
        #                             [pygame.K_RIGHT, pygame.K_LEFT,
        #                              pygame.K_UP, pygame.K_DOWN])
        #     elif enemy_pos[1] < self.rect.center[1]:
        #         dir = random.choice([pygame.K_UP, pygame.K_LEFT,
        #                              pygame.K_RIGHT] * 3 +
        #                             [pygame.K_RIGHT, pygame.K_LEFT,
        #                              pygame.K_UP, pygame.K_DOWN])
        #     else:
        #         dir = random.choice([pygame.K_RIGHT,
        #                              pygame.K_LEFT, pygame.K_UP,
        #                              pygame.K_DOWN])
        # return dir

    def check_collision(self):
        if pygame.sprite.spritecollideany(self, STICK_GROUP):
            self.rect = pygame.Rect(self.rect.x + 1, self.rect.y, *EGG_SIZE)
            # if not self.healed:
            #     self.health = 100
            #     self.healed = True
            #     self.music['boost'].play()
        # if pygame.sprite.spritecollideany(self, COOLDOWN_BONUS_GROUP):
        #     self.cd_time = time.time()
        #     self.delay = CoolDown.cooldown_time
        #     self.music['boost'].play()

    def logic(self):
        if self.rect.x <= 0:
            self.kill()
            # Rotate the image by any degree
        self.angular += 1
        self.image = pygame.transform.rotate(self.def_image,
                                             (self.angular) % 360)
        if pygame.sprite.spritecollideany(self, STICK_GROUP):
            self.rect = pygame.Rect(self.rect.x - 1, self.rect.y, *EGG_SIZE)
        elif pygame.sprite.spritecollideany(self, PLAYER_GROUP):
            self.kill()
        else:
            self.rect = pygame.Rect(self.rect.x, self.rect.y + 1, *EGG_SIZE)

    def update(self, *args):

        if time.time() - self.start >= self.speed:
            self.logic()
            self.start = time.time()
        # self.image = pygame.transform.scale(self.image, EGG_SIZE)

        # self.rect = self.rect
        # if self.cd_time:
        #     if time.time() - self.cd_time >= 3:
        #         self.delay = 3
        #         self.cd_time = 0
        # if self.health > 0:
        #     self.muzzle.get_muzzle(self.rect.center,
        #                            self.enemy.rect.center)
        #     data = zip(
        #         (-90, 90, 180, 0),
        #         ((CELL_SIZE, 0), (-CELL_SIZE, 0), (0, -CELL_SIZE), (0,
        #                                                             CELL_SIZE)
        #          ),
        #         [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN])
        #
        #     if args:
        #         board = args[0]
        #         enemy_pos = self.enemy.get_position()
        #         chosen = self.generate_direction(enemy_pos)
        #         for angle, move, direction in data:
        #             if chosen == direction and board.is_empty(
        #                     board.get_cell((self.rect.x + move[0],
        #                                     self.rect.y + move[1]))) and \
        #                     all((self.rect.x + move[0],
        #                          self.rect.y + move[1]) !=
        #                         (tank.rect.x, tank.rect.y)
        #                         for tank in ENEMY_TANK_GROUP) and \
        #                     (self.rect.x + move[0],
        #                      self.rect.y + move[1]) != (
        #                     self.enemy.rect.x, self.enemy.rect.y):
        #                 self.rect = self.rect.move(*move)
        #                 self.image = pygame.transform.rotate(
        #                     self.image, self.current_angle - angle)
        #                 self.muzzle.get_muzzle(self.rect.center,
        #                                        self.enemy.rect.center)
        #                 self.current_angle = angle
        #                 self.healed = False
        #                 self.do_strike += 1
        #                 # соблюдение кулдауна
        #         if self.do_strike == self.delay:
        #             self.strike()
        #             self.do_strike = 0
        #     self.show_xp()
        # else:
        #     self.music['death'].play()
        #     self.muzzle.kill()
        #     self.kill()

