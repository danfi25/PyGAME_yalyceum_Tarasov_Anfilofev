import pygame
import BirdClass
import ClassPipe
import random
import ClassRes
import Screen
from pygame.locals import *

# --- TARASOV V ---

pygame.init()
run = True

clock = pygame.time.Clock()
fps = 60

ground_scroll = 0
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
f = open('score.txt')
max_score = f.readline()
score = 0
pass_pipe = False

screen = Screen.screen
pygame.display.set_caption('Flappy Doom')
font = pygame.font.SysFont('roboto', 90)
font1 = pygame.font.SysFont('roboto', 50)

bg = pygame.image.load('resourses/background.png')
ground_img = pygame.image.load('resourses/ground.png')
button_res = pygame.image.load('resourses/restart_button.png')


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_game():
    pipe_object.empty()
    bird.rect.x = 100
    bird.rect.y = int(Screen.screen_height / 2)
    return 0


bird_object = pygame.sprite.Group()
pipe_object = pygame.sprite.Group()
bird = BirdClass.Bird(100, int(Screen.screen_height / 2))
bird_object.add(bird)
button_res = ClassRes.Res(Screen.screen_width // 2 - 50, Screen.screen_height // 2 - 100, button_res)

while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    bird_object.draw(screen)
    bird_object.update()
    pipe_object.draw(screen)
    screen.blit(ground_img, (ground_scroll, 768))

    if len(pipe_object) > 0:
        if bird_object.sprites()[0].rect.left > pipe_object.sprites()[0].rect.left \
                and bird_object.sprites()[0].rect.right < pipe_object.sprites()[0].rect.right \
                and pass_pipe is False:
            pass_pipe = True
        if pass_pipe is True:
            if bird_object.sprites()[0].rect.left > pipe_object.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
    draw_text(str(score), font, 'white', int(Screen.screen_width / 2), 20)
    draw_text(f'Hi score: {max_score}', font1, 'white', 20, 5)
    if score > int(max_score):
        max_score = score
    file = open('score.txt', 'w')
    file.write(f'{max_score}')
    file.close()

    if pygame.sprite.groupcollide(bird_object, pipe_object, False, False) or bird.rect.top < 0:
        bird.game_over = True

    if bird.rect.bottom > 768:
        bird.game_over = True
        bird.flying = False

    if bird.game_over is False and bird.flying is True:
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            btm_pipe = ClassPipe.Pipe(Screen.screen_width, int(Screen.screen_height / 2) + pipe_height, -1)
            top_pipe = ClassPipe.Pipe(Screen.screen_width, int(Screen.screen_height / 2) + pipe_height, 1)
            pipe_object.add(btm_pipe)
            pipe_object.add(top_pipe)
            last_pipe = time_now

        if bird.game_over is False:
            ground_scroll -= 4
            if abs(ground_scroll) > 35:
                ground_scroll = 0

        pipe_object.update()

    if bird.game_over is True:
        if button_res.draw() is True:
            bird.game_over = False
            score = reset_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and bird.flying is False and bird.game_over is False:
            bird.flying = True
    pygame.display.update()

pygame.quit()

# --- TARASOV ^ ---
