import pygame
from pygame.locals import *


class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.imagelest = []
		self.inx = 0
		self.cout = 0
		for num in range(1, 4):
			img = pygame.image.load(f'resourses/bird{num}.png')
			self.imagelest.append(img)
		self.image = self.imagelest[self.inx]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.cout += 1
		flap_cooldown = 3
		if self.cout > flap_cooldown:
			self.cout = 0
			self.inx += 1
			if self.inx >= len(self.imagelest):
				self.inx = 0
		self.image = self.imagelest[self.inx]
