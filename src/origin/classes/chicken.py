import random
import time
import pygame

from pygame import font

from src.origin.classes.egg import Egg
from src.origin.helpers import ALL_SPRITES, load_image, SCREEN, EGG_GROUP, \
    EGG_SIZE, CHICKEN_SIZE


# CELL_SIZE = 50


class Chicken(pygame.sprite.Sprite):
    """Вражеский танк"""
    def __init__(self, x, y, diff):
        super().__init__(ALL_SPRITES)
        # self.add(EGG_GROUP)
        self.image = pygame.transform.scale(load_image("chicken.webp"),
                                            CHICKEN_SIZE)
        self.rect = pygame.Rect(x, y, *CHICKEN_SIZE)
        self.start = time.time()
        self.diff = diff

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

    def spawn(self):
        egg = Egg(self.rect.x + EGG_SIZE[0], self.rect.y, self.diff/ 100000)

    def update(self, *args):
        pass
        # if self.cd_time:
        #     if time.time() - self.cd_time >= 3:
        #         self.delay = 3
        #         self.cd_time = 0
        if time.time() - self.start >= random.randint(3, 60):
            self.spawn()
            self.start = time.time()
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


if '__main__' == __name__:
    pygame.init()

    color = (255, 255, 255)
    position = (0, 0)

    # CREATING CANVAS
    canvas = pygame.display.set_mode((500, 500))

    # TITLE OF CANVAS
    pygame.display.set_caption("Show Image")

    # image = pygame.image.load("Screenshot.png")
    egg = Egg(50, 50)
    exit = False

    while not exit:
        # canvas.fill(color)
        # canvas.blit(egg, dest=position)
        started_time = time.time()
        SCREEN.fill("black")
        ALL_SPRITES.draw(SCREEN)
        # SCREEN.blit(font.render(
        #     'Time: ' + str(round(time.time() - started_time, 1)
        #                    ), True, 'black'), (10, 20))
        # SCREEN.blit(font.render(
        #     'Cooldown: ' + str(round(self.player.delay * 0.3, 1)
        #                        ) + ' sec', True, 'black'), (120, 20))
        ALL_SPRITES.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        pygame.display.update()
