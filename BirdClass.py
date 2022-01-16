import pygame
from pygame.locals import *


# --- ANFILOFEV V ---

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.flying = False
        self.game_over = False
        self.imagelest = []
        self.inx = 0
        self.cout = 0
        for num in range(1, 4):
            img = pygame.image.load(f'resourses/bird{num}.png')
            self.imagelest.append(img)
        self.image = self.imagelest[self.inx]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):
        if self.flying is True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if self.game_over is False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.cout += 1
            flap_cooldown = 5

            if self.cout > flap_cooldown:
                self.cout = 0
                self.inx += 1
                if self.inx >= len(self.imagelest):
                    self.inx = 0
            self.image = self.imagelest[self.inx]

            self.image = pygame.transform.rotate(self.imagelest[self.inx], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.imagelest[self.inx], -90)

# --- ANFILOFEV ^ ---
