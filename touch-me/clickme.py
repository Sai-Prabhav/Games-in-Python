from pygamelib import button
import pygame
from time import sleep
from random import randint

pygame.init()
clock = pygame.time.Clock()
normalfont=pygame.font.SysFont('Times New Roman.ttf', 20, False)
WIDTH = 400
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((255, 255, 0), rect=None, special_flags=0)
pygame.display.update()

class cbox():

    def __init__(self,WIDTH,HEIGHT):
        self.width =60
        self.height=60
        self.WIDTH,self.HEIGHT=WIDTH,HEIGHT
        self.vel=5
        self.x=randint(0,self.WIDTH-self.width)
        self.y=randint(0,self.HEIGHT-self.height)

        self.score=0

    def draw(self,surface,click):
        
        button(surface,'Click Me',(self.x,self.y),self.width,self.height,(0,255,255),(0,150,200),self.replace,normalfont,click)
        txt = normalfont.render('score:' + str(self.score), 1, (0, 0, 0))
        win.blit(txt, (20, 20))
        pygame.display.update()
    def replace(self):
        self.score+=1
        self.x=randint(0,self.WIDTH-self.width)
        self.y=randint(0,self.HEIGHT-self.height)



run = True
cboxa=cbox(WIDTH,HEIGHT)
while run:
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    win.fill((255, 255, 0), rect=None, special_flags=0)
    cboxa.draw(win,click)