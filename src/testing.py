import time

import pygame

from src.origin.classes.egg import Egg
from src.origin.helpers import SCREEN, ALL_SPRITES

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
