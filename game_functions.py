import sys

import pygame

def check_keydown_events(event, ship):
	# respond to keypress
	if event.key == pygame.K_RIGHT:
		# move ship to right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# move ship to left
		ship.moving_left = True

def check_keyup_events(event, ship):
	# respond to keypress
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	if event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ship):
	# respond to keypress and mouse
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ship)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship):
	# update images, flip screen
	# redrawe the screen during each pass
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	# make the most recently drawn visible
	pygame.display.flip()