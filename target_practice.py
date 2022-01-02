# A simple game where player tries to shoot a moving target practice on other side of the screen.
import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from rectangle import Rectangle
from game_stats import GameStats
from button import Button

class TargetPractice:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game and create game resources."""

		pygame.init()

		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.
