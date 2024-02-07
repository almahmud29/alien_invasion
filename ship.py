import pygame
class Ship:

	def __init__(self, ai_settings, screen):
		# initialize ship and it's starting position
		
		self.screen = screen
		self.ai_settings = ai_settings

		# load ship image and get it's rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
				

		# start each new ship at bottom center of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# store a decimal value for the ship's center
		self.center = float(self.rect.centerx)
		
		# Movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# update ship position based on  movement flag
		# update ship's center value not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
			# self.rect.centerx += 1
		if self.moving_left and self.rect.left > 0 :
			self.center -= self.ai_settings.ship_speed_factor
			# self.rect.centerx -= 1

		# Update rect object from self.center
		self.rect.centerx = self.center

	def blitme(self):
		# Draw ship at its current location
		
		self.screen.blit(self.image, self.rect)
		