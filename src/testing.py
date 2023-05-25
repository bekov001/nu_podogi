import sys
import time
from random import choices

import pygame


from src.origin.classes.chicken import Chicken
from src.origin.classes.egg import Egg
from src.origin.classes.player import Player
from src.origin.classes.stick import Stick
from src.origin.helpers import SCREEN, ALL_SPRITES, HEIGHT, WIDTH, PLAYER_SIZE, \
	SIZE, load_file, load_image, load_sound
import pygame_gui as gui

from src.origin.levels.level1 import level, level2, level3


class Game:
	def __init__(self):
		self.manager = gui.UIManager(SIZE)
		self.score = 0
		self.time = 0
		self.maximum = int(open("origin/media/data/record.txt", "r").read())

	def main(self):
		color = (255, 255, 255)
		position = (0, 0)

		# CREATING CANVAS
		# canvas = pygame.display.set_mode((500, 500))
		level_run()
		# TITLE OF CANVAS
		pygame.display.set_caption("Show Image")

		# image = pygame.image.load("Screenshot.png")

		self.player = Player(WIDTH // 2, HEIGHT - PLAYER_SIZE[1])

		exit = False
		font = pygame.font.Font(pygame.font.match_font('comicsansms'), 20)
		started_time = time.time()
		bg = load_image("bg.png")
		while not exit:
			# time_delta = clock.tick(60)
			# canvas.fill(color)
			# canvas.blit(egg, dest=position)


			SCREEN.fill("black")

			# SCREEN.blit()
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
					f = open("origin/media/data/leaders.txt", "a")
					f.write(
						str(name) + ":" + f"score - {self.player.score}, time - {round(time.time() - started_time, 1)}")

					if self.player.score > self.maximum:
						print("YOU HAVE A RECORD")
						f = open("origin/media/data/record.txt", "w")
						f.write(str(self.player.score))


				self.player.update(event)
				# self.manager.process_events(event)
			SCREEN.fill("black")
			# bg = load_image("bg.png")
			#
			# # INSIDE OF THE GAME LOOP
			SCREEN.blit(bg, (0, 0))
			ALL_SPRITES.draw(SCREEN)
			SCREEN.blit(font.render(
				'Time: ' + str(round(time.time() - started_time, 1)
							   ) + ' sec', True, 'black'), (10, 20))
			SCREEN.blit(font.render(
				'Score: ' + str(round(self.player.score)), True, 'black'), (150, 20))
			ALL_SPRITES.update()
			# self.manager.update(time_delta)
			# self.manager.draw_ui(SCREEN)
			# timing = time.time()
			pygame.display.update()


def choose_level():
	try:
		answer = int(input("выберите уровень (1, 2, 3): "))
		if int(answer) > 3 or int(answer) < 1:
			print("ошибка")
		elif answer == 1:
			return level
		elif answer == 2:
			return level2
		else:
			return level3

	except Exception:
		print("Ошибка попробуйте еще раз")


if "__main__" == __name__:
	name = input("Ваше имя:" )
	level_run = choose_level()
	pygame.init()
	load_sound("song.mp3")
	pygame.mixer.music.set_volume(0.5)
	pygame.mixer.music.play(-1)

	# clock = pygame.time.Clock()
	game = Game()
	game.main()