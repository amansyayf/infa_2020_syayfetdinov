from pygame.draw import *
from random import randint
import pygame
from os import path

pygame.init()

FPS = 50
s_x = 1200
s_y = 600
screen = pygame.display.set_mode((s_x, s_y))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
PINK = (230, 50, 230)
LIME = (230, 255, 101)
FOREST_GREEN = (5, 100, 5)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, PINK, LIME, FOREST_GREEN]

pygame.font.SysFont('arial', 36)
f1 = pygame.font.Font(None, 30)

score = 0
c = 0
d = 0
e = 0


class Ball:
    def __init__(self, x, y, r, v_y, v_x, color):
        self.x = x
        self.y = y
        self.r = r
        self.v_y = v_y
        self.v_x = v_x
        self.color = color

    def move(self, x, y, r, v_y, v_x, color):
        if self.x + self.r > s_x:
            self.v_x = -randint(0, 10)
            self.v_y = randint(0, 10)
        elif self.x - self.r < 0:
            self.v_x = randint(0, 10)
            self.v_y = randint(0, 10)
        elif self.y - self.r < 0:
            self.v_x = randint(0, 10)
            self.v_y = randint(0, 10)
        elif self.y + self.r > s_y:
            self.v_x = randint(0, 10)
            self.v_y = -randint(0, 10)
        self.v_x += self.v_y / (abs(self.v_y) + 1) * int(e ** 0.2) - 0.3 * self.v_y
        self.v_y -= self.v_x / (abs(self.v_x) + 1) * int(e ** 0.2) - 0.3 * self.v_x
        self.x += int(self.v_x)
        self.y += int(self.v_y)

        return circle(screen, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

score = 0

while not finished:
    clock.tick(FPS)
    screen.blit(f1.render('score = ' + str(score), 1, (255, 255, 255)), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = event.pos
            if ((x1 - a.x) ** 2 + (y1 - a.y) ** 2) <= a.r ** 2:
                score += 1
                print(score)
                c = 0
            if ((x1 - b.x) ** 2 + (y1 - b.y) ** 2) <= b.r ** 2:
                score += 1
                print(score)
                d = 0
            if ((x1 - f.x) ** 2 + (y1 - f.y) ** 2) <= f.r ** 2:
                score += 1
                print(score)
                e = 0
    c += 1
    if c < 202:
        if c < 2:

            a = Ball(randint(100, 1100), randint(100, 500), randint(10, 100),
                     randint(-10, 10), randint(-10, 10), COLORS[randint(0, 8)])
        else:
            a.move(a.x, a.y, a.r, a.v_y, a.v_x, a.color)
    else:
        c = 0

    d += 1
    if d < 215:
        if d < 2:
            b = Ball(randint(100, 1100), randint(100, 500), randint(10, 100),
                     randint(-10, 10), randint(-10, 10), COLORS[randint(0, 8)])
        else:
            b.move(b.x, b.y, b.r, b.v_y, b.v_x, b.color)
    else:
        d = 0
    e += 1
    if e < 190:
        if e < 2:
            f = Ball(randint(100, 1100), randint(100, 500), randint(10, 100),
                     randint(-10, 10), randint(-10, 10), COLORS[randint(0, 8)])
        else:
            f.move(f.x, f.y, f.r, f.v_y, f.v_x, f.color)

    else:
        e = 0
    pygame.display.update()
    screen.fill(BLACK)

running = True

pygame.quit()
