import pygame
import BirdClass
import ClassPipe
import random
from pygame.locals import *

# --- TARASOV V ---

pygame.init()
run = True

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936
ground_scroll = 0
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Doom')

bg = pygame.image.load('resourses/background.png')
ground_img = pygame.image.load('resourses/ground.png')

bird_object = pygame.sprite.Group()
pipe_object = pygame.sprite.Group()
bird = BirdClass.Bird(100, int(screen_height / 2))
bird_object.add(bird)

while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    bird_object.draw(screen)
    bird_object.update()
    pipe_object.draw(screen)
    screen.blit(ground_img, (ground_scroll, 768))

    if pygame.sprite.groupcollide(bird_object, pipe_object, False, False) or bird.rect.top < 0:
        bird.game_over = True

    if bird.rect.bottom > 768:
        bird.game_over = True
        bird.flying = False

    if bird.game_over is False and bird.flying is True:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = ClassPipe.Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
            top_pipe = ClassPipe.Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
            pipe_object.add(btm_pipe)
            pipe_object.add(top_pipe)
            last_pipe = time_now

        if bird.game_over is False:
            ground_scroll -= 4
            if abs(ground_scroll) > 35:
                ground_scroll = 0

        pipe_object.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and bird.flying is False and bird.game_over is False:
            bird.flying = True
    pygame.display.update()

pygame.quit()

# --- TARASOV ^ ---
