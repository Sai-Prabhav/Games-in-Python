import sys
import random
import pygame
import time
import threading
pygame.init()

fps = 6
fpsClock = pygame.time.Clock()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Times New Roman.ttf', 30, True)


class body():
    def __init__(self, size):
        self.size = size
        self.l, self.b = size
        self.cellma = []
        self.nebma = []
        for row in range(self.l):
            self.cellma.append([])
            self.nebma.append([])
            for celll in range(self.b):
                self.nebma[row].append([])
                self.cellma[row].append(
                    self.cell(random.choice([True, False]), (row, celll), self.cellma))
        print("done")

    def draw(self):
        
        for x, row in enumerate(self.cellma):
            for y, cell in enumerate(row):
                self.nebma[x][y] = cell.neb()

        for x,rowneb in enumerate(self.nebma):
            for y,cellneb in enumerate(rowneb):
                if cellneb==3:
                    self.cellma[x][y].IsAlive=True
                    
                elif cellneb != 2:
                    self.cellma[x][y].IsAlive = False
        for x, row in enumerate(self.cellma):
            for y, cell in enumerate(row):
                cell.draw()
        print("draw")
    class cell():
        def __init__(self, IsAlive, cords, cellma):
            self.cellma = cellma
            self.IsAlive = IsAlive
            self.cords = cords
            self.x, self.y = cords
            self.width = 10
            self.height = 10
            if self.IsAlive:
                self.color = (255, 255, 255)
            else:
                self.color = (0, 0, 0)

        def neb(self):
            neb = 0
            neblist = [[self.x-1, self.y-1], [self.x, self.y-1], [self.x-1, self.y], [self.x+1, self.y + 1], [self.x, self.y+1], [self.x+1, self.y], [self.x-1, self.y+1], [self.x+1, self.y-1]]

            for nbe in neblist:
                try:
                    neb += self.cellma[nbe[0]][nbe[1]].IsAlive
                except:
                    
                    continue
            print(neb)
            return neb

        def draw(self):
            if self.IsAlive:
                self.color = (255, 255, 255)
            else:
                self.color = (0, 0, 0)
            pygame.draw.rect(screen, self.color, (self.x*10,
                             self.y*10, self.width, self.height))
            # print("draw")


bodyy = body((50, 50))


def st(function):
    print(time.time())
    start = time.time()
    function()
    end = time.time()
    print(f"it took {end-start} sec")



def demon():
        screen.fill((255, 250, 200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        bodyy.draw()
        pygame.display.update()
        fpsClock.tick(30)

while True:
    start = time.time()
    demon()
    end = time.time()
    print(f"it took {end-start} sec")
