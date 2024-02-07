
import pygame
# from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# initiate pygame, settings and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# make a ship
	ship = Ship(ai_settings, screen)
	# make a group to store bullets
	#bullets = Group()
	
	# set bg color
	bg_color = (230, 230, 230)

	# start the main loop for the game
	while True:
		gf.check_events(ship)
		ship.update()
		#bullets.update()
		gf.update_screen(ai_settings, screen, ship)

		# redraw the screen during each pass through the loop
		# screen.fill(ai_settings.bg_color)
		# ship.blitme()
		# make the most recent drawn screen visible
		# pygame.display.flip()

run_game()