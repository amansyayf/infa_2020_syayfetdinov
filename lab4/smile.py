import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 700;
y1 = 700
x2 = 300;
y2 = 200
N = 10
color_1 = (255, 255, 255)
rect(screen, color_1, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x_1 = x1 + h
for i in range(N):
    line(screen, color_1, (x_1, y1), (x_1, y2))
    x_1 += h

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
"Added something to README"

