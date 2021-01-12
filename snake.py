import pygame
from time import sleep
from random import randrange
import os
pygame.init()
width = 500
win = pygame.display.set_mode((width+20, 520))
pygame.display.set_caption("snakeee")
run = True
clock = pygame.time.Clock()
#bg = pygame.image.load(r'C:\Users\CSC\Desktop\my code\sankeeeee\bg.jpg')
snakelen = 1
snake_body = []
font = pygame.font.SysFont('Arial.ttf', 30, True)
print(os.path.dirname(__file__))
foods = pygame.image.load(os.path.dirname(__file__) + '/Food.png')
head = heads = pygame.image.load(os.path.dirname(__file__)+'/snake head.png')


def istuching(ob1, ob2):
    if ob1[0]+ob1[2] > ob2[0] and ob1[0] < ob2[0]+ob2[3] and ob1[1]+ob1[3] > ob2[1] and ob1[1] < ob2[1]+ob2[3]:
        return True
    else:
        return False


class snake(object):

    def __init__(self, x, y, width, height):
        self.snake_body = [[x, y, 25, 25]]
        self.snakelen = 1
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 25
        self.direction = 0
        self.run = True
        self.hitbox = [self.x, self.y, 25, 25]
        self.score = 0
        self.xman = 0

    def restart(self):
        width = 25
        height = 25
        x = 250
        y = 250
        self.snake_body = [[x, y, 25, 25]]
        self.snakelen = 1
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 25
        self.direction = 0
        self.run = True
        self.hitbox = [self.x, self.y, 25, 25]
        self.score = 0

    def draw(self, win):
        if self.direction == 0:
            heads = pygame.transform.rotate(head, 90)
            heads = pygame.transform.flip(head, False, True)

        if self.direction == 2:
            self.x += self.vel
            heads = pygame.transform.flip(head, False, False)

        if self.direction == 4:
            self.x -= self.vel
            heads = pygame.transform.flip(head, True, False)

        if self.direction == 1:
            self.y -= self.vel
            heads = pygame.transform.rotate(head, 90)

        if self.direction == 3:
            self.y += self.vel
            heads = pygame.transform.rotate(head, 90)
            heads = pygame.transform.flip(heads, False, True)

        self.hitbox = [self.x, self.y, 25, 25]

        for i in range(len(self.snake_body)):
            if i > 0:
                if istuching(self.hitbox, self.snake_body[i]):
                    self.run = False

        for i in range(len(self.snake_body[1:])):
            pygame.draw.rect(win, (0, 200, 0), pygame.Rect(
                self.snake_body[i+1][0], self.snake_body[i+1][1], self.height, self.width))

        win.blit(heads, (self.snake_body[0][0], self.snake_body[0][1]))

        if self.x >= 509 or self.y >= 509:
            self.run = False
            self.direction = 0

        elif self.x+20 <= 0 or self.y+20 <= 0:
            self.xman += 1
            self.direction = 0

            if self.xman == 3:
                self.run = False
                self.xman = 0

    def grow(self):
        self.snake_body.insert(0, [self.x, self.y, 25, 25])

        self.score += 1


class food(object):
    def __init__(self):
        self.x = randrange(0, 500, 25)
        self.y = randrange(0, 500, 25)
        self.hitbox = [self.x, self.y, 25, 25]
        self.r = 0

    def draw(self, win):
        if self.r >= 360:
            self.r = 0
        self.r += 15
        foodss = pygame.transform.rotate(foods, self.r)
        win.blit(foodss, (self.x, self.y))

        self.hitbox = [self.x, self.y, 25, 25]

    def remove(self):
        self.x = randrange(0, 500, 25)
        self.y = randrange(0, 500, 25)
        self.hitbox = [self.x, self.y, 25, 25]


def redraw(win):

    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), pygame.Rect(0, 500, 500, 20))
    txt = font.render('score:' + str(snakee.score), 1, (0, 0, 0))
    win.blit(txt, (20, 500))
    snacks.draw(win)
    snakee.draw(win)
    pygame.display.update()


def out():
    sleep(0.5)
    tex = font.render('RIP you died', 1, (225, 225, 0))
    text = font.render('score: ' + str(snakee.score) +
                       ' press space to play again', 1, (225, 225, 0))
    win.blit(text, (10, 35))
    win.blit(tex, (10, 10))
    pygame.display.update()
    if keys[pygame.K_SPACE]:
        snakee.run == True
        snakee.restart()


snakee = snake(width/2, width/2, 25, 25)
snacks = food()
i = 0
while run:
    keys = pygame.key.get_pressed()

    if snakee.run == False:
        out()

    clock.tick(5)

    snakee.snake_body.insert(0, [snakee.x, snakee.y, 25, 25])
    snakee.snake_body.pop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and not(snakee.direction == 3):
        snakee.direction = 1
    if keys[pygame.K_RIGHT] and not(snakee.direction == 4):
        snakee.direction = 2
    if keys[pygame.K_DOWN] and not(snakee.direction == 1):
        snakee.direction = 3
    if keys[pygame.K_LEFT] and not(snakee.direction == 2):
        snakee.direction = 4
    if istuching(snakee.hitbox, snacks.hitbox):
        snacks.remove()
        snakee.grow()

    i += 1
    if snakee.run == True:
        redraw(win)
