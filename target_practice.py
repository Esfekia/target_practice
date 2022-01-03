# A simple game where player tries to shoot a moving target practice on other side of the screen.
import sys
from time import sleep
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from gamestats import GameStats
from button import Button
from target import Target

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
		self.stats = GameStats(self)
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		
		#Create the Target Rectangle.
		self.target = Target(self)
		
		#Create the Play button.
		self.play_button = Button(self, "Play") 


	def run_game(self):
		"""Start the main loop for the game."""
		while True:

			#Watch for keyboard and mouse events.
			self._check_events()

			#Check if game still active first!
			if self.stats.game_active:
				#Update the ship's position.
				self.ship.update()

				#Update the bullet's position.
				self._update_bullets()

				#Update the target's movement:
				#self._update_target()
				self.target.update()

			#Redraw the screen during each pass through the loop.
			self._update_screen()

	def _check_events(self):
		"""Respond to key presses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)

	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks play"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			#Reset the game statistics and set active flag
			self.stats.reset_stats()
			self.stats.game_active = True
			self.bullets.empty()
			self.ship.center_ship()

			#Hide the mouse cursor
			pygame.mouse.set_visible(False)

	def _check_keydown_events(self,event):
		"""Respond to key presses."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_p and not self.stats.game_active:
			#Reset the game statistics and set active flag.
			self.stats.reset_stats()
			self.stats.game_active = True
			self.bullets.empty()
			self.ship.center_ship()

			#Hide the mouse cursor
			pygame.mouse.set_visible(False)

	def _check_keyup_events(self,event):
		"""Respond to key releases."""
		if event.key == pygame.K_UP:
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.ship.moving_down = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		#First check max bullets allowed in settings.
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _create_target(self):
		"""Create the target"""
		target = Target(self)

	def _update_bullets(self):
		"""Update position of bullets and get rid of old bullets."""
		#Update bullet positions.
		self.bullets.update()

		#Get rid of bullets that disappeared off screen.
		for bullet in self.bullets.copy():
			if bullet.rect.right >= self.settings.screen_width:
				self.settings.number_miss-=1
				print (f"Lives left" +str(self.settings.number_miss))
				if self.settings.number_miss == 0:
					self.stats.game_active=False
					pygame.mouse.set_visible(True)
					self.settings.number_miss = 3
				self.bullets.remove(bullet)

		self.check_bullet_target_collisions()

	def check_bullet_target_collisions(self):
		"""Respond to bullet-target collissions."""

		#Remove any bullets that have collided.
		collissions = pygame.sprite.spritecollide(
			self.target,self.bullets,True)

	def _update_target(self):
		"""Update the position of the target"""
		self.target.update()

	def _update_screen(self):
		"""Update images on the screen and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		#Draw the bullets
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		#Draw the target
		self.target.draw_target()

		#Draw the play button if the game is inactive.
		if not self.stats.game_active:
			self.play_button.draw_button()

		#Make the most recently drawn screen visible.
		pygame.display.flip()

if __name__ == '__main__':
	#Make a game instance and run the game.
	tp = TargetPractice()
	tp.run_game()