import pygame
from pygame.locals import *


# --- ANFILOFEV V ---
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resourses/pipe.png')
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(150 / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(150 / 2)]

    def update(self):
        self.rect.x -= 4
        if self.rect.right < 0:
            self.kill()

# --- ANFILOFEV ^ ---
