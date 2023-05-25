import sys
import time

import pygame

from src.origin.classes.chicken import Chicken
from src.origin.classes.egg import Egg
from src.origin.classes.player import Player
from src.origin.classes.stick import Stick
from src.origin.helpers import SCREEN, ALL_SPRITES, HEIGHT, WIDTH, PLAYER_SIZE, \
	SIZE, load_file
import pygame_gui as gui


class Game:
	def __init__(self):
		self.manager = gui.UIManager(SIZE)

	def main(self):
		color = (255, 255, 255)
		position = (0, 0)

		# CREATING CANVAS
		# canvas = pygame.display.set_mode((500, 500))

		# TITLE OF CANVAS
		pygame.display.set_caption("Show Image")

		# image = pygame.image.load("Screenshot.png")
		egg = Egg(50, 50)
		self.player = Player(WIDTH // 2, HEIGHT - PLAYER_SIZE[1])
		stick = Stick(50, 200)

		chicken = Chicken(0, 50)
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
				self.player.update(event)
			pygame.display.update()



if "__main__" == __name__:
	pygame.init()

	game = Game()
	game.main()