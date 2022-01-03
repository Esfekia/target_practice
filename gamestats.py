class GameStats:
	"""Tracks statistics for Target Practice."""

	def __init__ (self, tp_game):
		"""Initialize statistics."""
		self.settings = tp_game.settings
		self.reset_stats()
		#Start Target Practice in an inactive state.
		self.game_active = False

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit