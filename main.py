import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/tir.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

target_speed = 1
dx = random.choice([-1, 1]) * target_speed
dy = random.choice([-1, 1]) * target_speed

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    target_x += dx
    target_y += dy

    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        dx *= -1
    if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        dy *= -1


    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()