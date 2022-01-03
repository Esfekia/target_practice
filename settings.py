class Settings:
	"""A Class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""

		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#Ship settings
		self.ship_speed = 1.5

		#Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 15
		self.bullet_height = 15
		self.bullet_color = (252,15,192)
		self.bullets_allowed =3

		#Target settings

		self.target_width = 50
		self.target_height = 200
		self.target_color = (0,255,0)
		self.target_speed = 1.0

		#target_direction of 1 represents down, -1 represents up.
		self.target_direction = -1

		#Game Mechanics
		self.number_miss =3
		self.game_active = True
