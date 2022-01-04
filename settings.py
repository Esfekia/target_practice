class Settings:
	"""A Class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#Bullet settings
		self.bullet_width = 15
		self.bullet_height = 15
		self.bullet_color = (252,15,192)
		self.bullets_allowed =3

		#Target settings
		self.target_width = 50
		self.target_height = 200
		self.target_color = (0,255,0)
		
		#How quickly the game speeds up
		self.speedup_scale = 2

		self.initiliaze_dynamic_settings()

	def initiliaze_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""

		self.ship_speed = 1.5
		self.bullet_speed = 3
		self.target_speed = 0.5
		
		#target_direction of 1 represents down, -1 represents up.
		self.target_direction = -1

		#Game Mechanics
		self.number_miss =3
		self.target_hit = 0
		self.ship_limit = 3
		
	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed *= self.speedup_scale
		self.target_speed*= self.speedup_scale
