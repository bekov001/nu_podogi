from itertools import product
import time
import pygame

from src.origin.helpers import CELL_SIZE, ALL_SPRITES, load_image, PLAYER_SIZE, \
    PLAYER_GROUP, EGG_GROUP


class Player(pygame.sprite.Sprite):
    """Вражеский танк"""
    def __init__(self, x, y):
        super().__init__(ALL_SPRITES)
        self.score = 0
        self.add(PLAYER_GROUP)
        self.health = 100
        self.image = pygame.transform.scale(load_image("player.png"),
                                           PLAYER_SIZE)
        self.rect = pygame.Rect(x, y, *PLAYER_SIZE)

    # def strike(self, event):
    #     """Функция выстрела"""
    #     if event.type == pygame.MOUSEBUTTONDOWN \
    #             and time.time() - self.created > self.delay * 0.3:
    #         self.music['player_shot'].play()
    #         Strike(self.rect.center, event.pos, ENEMY_TANK_GROUP)
    #         self.created = time.time()
    #         self.muzzle.get_muzzle(self.rect.center, event.pos)

    def get_position(self):
        return self.rect.center

    # def show_xp(self):
    #     """Показывает здоровье танка"""
    #     xp = self.health / 100
    #     font = pygame.font.Font(pygame.font.match_font('comicsansms'), 15)
    #     pygame.draw.rect(SCREEN, "green", (10, 10, 200 * xp, 10))
    #     pygame.draw.rect(SCREEN, "red", (
    #         200 * xp + 10, 10, 200 - 200 * xp, 10))
    #     SCREEN.blit(font.render(str(self.health) + 'hp', True, 'green'),
    #                 (210, 7))

    def update(self, *args):
        CELL_SIZE = 30
        data = zip(((CELL_SIZE, 0), (-CELL_SIZE, 0),
                                      ),
                   [(pygame.K_RIGHT, pygame.K_d),
                    (pygame.K_LEFT, pygame.K_a),
                  ])
        # self.muzzle.get_muzzle(self.rect.center, pygame.mouse.get_pos())
        if args and args[0].type == pygame.KEYDOWN:
            for move, direction in data:
                if args[0].key in direction:
                #         board.is_empty(
                #             board.get_cell(
                #                 (self.rect.x + move[0],
                #                  self.rect.y + move[1])
                #             )
                #         ) and all((self.rect.x + move[0],
                #                    self.rect.y + move[1]) !=
                #                   (tank.rect.x, tank.rect.y)
                #                   for tank in ENEMY_TANK_GROUP):
                    self.rect = self.rect.move(*move)
                #     self.image = pygame.transform.rotate(
                #         self.image,
                #         self.current_angle - angle)
                #     self.muzzle.get_muzzle(self.rect.center,
                #                            pygame.mouse.get_pos())
                #     self.current_angle = angle
                #     self.healed = False
        if pygame.sprite.spritecollideany(self, EGG_GROUP):
            self.score += 1
        # if args:
        #     self.strike(args[0])
        # self.show_xp()
        # else:
        #     self.muzzle.kill()
        #     self.kill()