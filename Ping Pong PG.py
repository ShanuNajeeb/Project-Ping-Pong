import random
import pygame, sys
pygame.init()
clock = pygame.time.Clock()

def ball_movement():
    global ballspeed_x, ballspeed_y
    ball.x += ballspeed_x
    ball.y += ballspeed_y

    #screen borders
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ballspeed_y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_restart()

    #paddle colliding
    if ball.colliderect(player_a) or ball.colliderect(player_b):
        ballspeed_x *= -1

def player_movement():
    player_a.y += player_speed
    if player_a.top <= 0:
        player_a.top = 0
    if player_a.bottom >= HEIGHT:
        player_a.bottom = HEIGHT

def playerb_ai():
    if player_b.top < ball.y:
        player_b.top += player_b_speed
    if player_b.bottom > ball.y:
        player_b.bottom -= player_b_speed
    if player_b.top <= 0:
        player_b.top += 0
    if player_b.bottom >= HEIGHT:
        player_b.bottom = HEIGHT

def ball_restart():
    global ballspeed_x, ballspeed_y
    ball.center = (WIDTH/2, HEIGHT/2)
    ballspeed_y *= random.choice((1, -1))
    ballspeed_x *= random.choice((1, -1))

#Window
WIDTH, HEIGHT = 1450, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong! ")
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)

#colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_GREY = (200, 200, 200)
GREY12 = pygame.Color('grey12')

FPS = 60

#draw
ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30,30)
player_a = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70, 10,140)
player_b = pygame.Rect(10, HEIGHT/2 - 70, 10,140)

ballspeed_x = 5 * random.choice((1, -1))
ballspeed_y = 5 * random.choice((1, -1))
player_speed = 0
player_b_speed = 8

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5

    ball_movement()
    player_movement()
    playerb_ai()

    # apply on screen
    WIN.fill(GREY12)
    pygame.draw.rect(WIN, LIGHT_GREY, player_a)
    pygame.draw.rect(WIN, LIGHT_GREY, player_b)
    pygame.draw.ellipse(WIN, LIGHT_GREY, ball)
    pygame.draw.aaline(WIN, LIGHT_GREY, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    pygame.display.flip()
