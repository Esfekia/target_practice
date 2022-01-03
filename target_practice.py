# A simple game where player tries to shoot a moving target practice on other side of the screen.
import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
#from bullet import Bullet
#from rectangle import Rectangle
#from game_stats import GameStats
#from button import Button
#from target import Target

class TargetPractice:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game and create game resources."""

		pygame.init()

		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Target Practice")

		#Create an instance to store the game statistics.
		#self.stats = GameStats(self)
		self.ship = Ship(self)
		#self.bullets = pygame.sprite.Group()
		
		#Create the rectangular, moving target.
		#self._create_target()

		#Create the Play button.
		#self.play_button = Button(self, "Play") 


	def run_game(self):
		"""Start the main loop for the game."""
		while True:

			#Update the ship's position.
			self.ship.update()

			#Redraw the screen during each pass through the loop.
			self._update_screen()

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		#Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance and run the game.
	tp = TargetPractice()
	tp.run_game()