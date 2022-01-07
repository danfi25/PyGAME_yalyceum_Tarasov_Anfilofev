import pygame
from pygame.locals import *

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

while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= 4
    if abs(ground_scroll) > 35:
        ground_scroll = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
