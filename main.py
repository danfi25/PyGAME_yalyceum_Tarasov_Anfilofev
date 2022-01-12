import pygame
import BirdClass
from pygame.locals import *

# --- TARASOV V ---

pygame.init()
run = True

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936
ground_scroll = 0

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Doom')

bg = pygame.image.load('resourses/background.png')
ground_img = pygame.image.load('resourses/ground.png')

bird_object = pygame.sprite.Group()
bird = BirdClass.Bird(100, int(screen_height / 2))
bird_object.add(bird)

while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    bird_object.draw(screen)
    bird_object.update()
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= 4
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()

# --- TARASOV ^ ---