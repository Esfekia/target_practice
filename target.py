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
		self.rect.midright = self.screen_rect.midright

		#Store the target's exact position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update (self):
		"""Move the target up or down."""
		self.y += (self.settings.target_speed * 
			self.settings.target_direction)
		

		if self.rect.top < 0:
			#It has moved past the top of the screen.
			#Place at top of screen and change direction.
			self.rect.top = 0
			self.settings.target_direction = 1

		elif self.rect.bottom > self.screen_rect.bottom:
			#Place at bottom and change direction.
			self.rect.bottom = self.screen_rect.bottom
			self.settings.target_direction = -1

		#update the rect position.
		self.rect.y = self.y
	
	def draw_target(self):
		# Draw the target
		pygame.draw.rect(self.screen, self.settings.target_color, 
			self.rect)