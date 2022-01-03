import pygame

class Ship:
	"""A Class to manage the ship."""

	def __init__(self, tp_game):
		"""Initialize the ship and set its starting position."""
		self.screen = tp_game.screen
		self.settings = tp_game.settings
		self.screen_rect = tp_game.screen.get_rect()

		#Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#Start each new ship at the middle left of the screen.
		self.rect.midleft = self.screen_rect.midleft

		#Store a decimal value for the ships x,y position.
		self.x = float (self.rect.x)
		self.y = float (self.rect.y)

		#Movement flag
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Update the ship's position based on the movement flags."""

		#Update the ship's y value, not the rect.
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed 

		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed

		#Update the rect object from self.y
		self.rect.y = self.y

	def center_ship (self):
		"""Center the ship on midleft of the screen."""
		self.rect.midleft = self.screen_rect.midleft
		self.x = float(self.rect.x)
		self.y =float(self.rect.y)

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)