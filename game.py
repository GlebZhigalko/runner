import random

import pygame




#инициализация модуля 

pygame.init()

#создание среды
white = (255, 255, 255)
black = (0, 0, 0)
orange = (255, 165, 0)
WIDTH = 440
HEIGHT = 300

#создание значений основ игры
score = 0
player_x = 50
player_y = 200
y_change = 0
gravity = 1
x_change = 0
obstacles = [300, 400, 600]
obstacle_speed = 2
active = False
#добавление музыки
pygame.mixer.init()
pygame.mixer.music.load("music2.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
#настройка отображающих моментов 
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Runner')
background = black
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
#код игры
running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    score_text = font.render(f'Счёт очков: {score}', True, white, black)
    screen.blit(score_text, (160, 250))
    floor = pygame.draw.rect(screen, white, [0, 220, WIDTH, 5])
    player = pygame.draw.rect(screen, white, [player_x, player_y, 20, 20])
    obstacle0 = pygame.draw.rect(screen, orange, [obstacles[0], 200, 20, 20])
    obstacle1 = pygame.draw.rect(screen, orange, [obstacles[1], 200, 20, 20])
    obstacle2 = pygame.draw.rect(screen, orange, [obstacles[2], 200, 20, 20])

    if not active:
        instruction_text = font.render(f'Нажмите Пробел', True, white, black)
        screen.blit(instruction_text, (140, 50))
        instruction_text2 = font.render(f'Пробел - прыжок.  <- / -> - Движение', True, white, black)
        screen.blit(instruction_text2, (80, 90))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not active:
            if event.key == pygame.K_SPACE:
                y_change = 18
                obstacles = [300, 400, 600]
                player_x = 50
                score = 0
                active = True

        if event.type == pygame.KEYDOWN and active:
            if event.key == pygame.K_SPACE and y_change == 0:
                y_change = 18
            if event.key == pygame.K_RIGHT:
                x_change = 2
            if event.key == pygame.K_LEFT:
                x_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = 0

    for i in range(len(obstacles)):
        if active:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < -20:
                obstacles[i] = random.randint(470, 570)
                score += 1
            if player.colliderect(obstacle0) or player.colliderect(obstacle1) or player.colliderect(obstacle2):
                active = False

    if 0 <= player_x <= 370:
        player_x += x_change
    if player_x < 0:
        player_x = 0
    if player_x > 370:
        player_x = 370

    if y_change > 0 or player_y < 200:
        player_y -= y_change
        y_change -= gravity
    if player_y > 200:
        player_y = 200
    if player_y == 200 and y_change < 0:
        y_change = 0

    pygame.display.flip()
pygame.quit()