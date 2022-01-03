import pygame

class Target():
	"""A class to represent a single target."""

	def __init__(self, tp_game):
		"""Initialize the target and set its starting position."""
		super().__init__()
		self.screen = tp_game.screen
		self.settings = tp_game.settings
		self.screen_rect = self.screen.get_rect()

		#Build the target's rect object and put it center right.
		self.rect =pygame.Rect(0,0, self.settings.target_width,
			self.settings.target_height)
		self.rect.midright =self.screen_rect.midright

	def draw_target(self):
		# Draw the target
		pygame.draw.rect(self.screen, self.settings.target_color, self.rect)


	