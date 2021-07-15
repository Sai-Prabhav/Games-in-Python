import sys
import random
import pygame

pygame.init()

fps = 6
fpsClock = pygame.time.Clock()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont('Times New Roman.ttf', 30, True)


def IsTurnl(pos, bt):
    for po in pos:
        if po[0] <= 175:
            return False
    for pp in pos:
        if pp in bt:
            return False
            break
    return True


def IsStop(cor):
    for cors in cor:
        if cors[1] <= 0:
            return True
    return False


def IsTurnr(pos, bt):
    for po in pos:
        if po[0] >= width:
            return False

    for pp in pos:
        if pp in bt:
            return False
            break
    return True


def IsRun(bt, prester):
    for pp in prester:
        if pp[1] >= height:
            return False
            # print("false")
            break

    for pp in prester:
        if pp in bt:
            return False
            break
    return True


class block():
    def __init__(self, color, cord=[100, 100]):
        # #print("hi")
        self.cord = cord
        self.size = 25
        self.rect = [cord[0], cord[1], 25, 25]
        self.color = color

    def update(self, cord):
        self.cord = cord
        self.rect = [cord[0], cord[1], 25, 25]

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


class tet():
    def __init__(self):
        self.run = True
        self.start = [random.randint(0, 9)*25+225, 0]
        self.x, self.y = self.start
        self.color = random.choice(
            [(20, 200, 50), (50, 10, 190), (20, 250, 10), (150, 100, 30)])
        # print(self.color)
        self.blockcor = random.choice(
            [[
                self.start],
             [
                self.start,
                [self.x, self.y+25]],
             [
                self.start,
                [self.x, self.y+25],
                [self.x, self.y+50]],
             [
                self.start,
                [self.x+25, self.y],
                [self.x, self.y+25],
                [self.x-25, self.y+25]],
             [
                self.start,
                [self.x-25, self.y],
                [self.x, self.y+25],
                [self.x+25, self.y+25]],
             [
                self.start,
                [self.x+25, self.y]],

             [
                self.start,
                [self.x-25, self.y],
                [self.x+25, self.y]],
             [
                self.start,
                [self.x+25, self.y],
                [self.x, self.y+25],
                [self.x+25, self.y+25]],
             [
                self.start,
                [self.x, self.y+25],
                [self.x, self.y+50],
                [self.x+25, self.y+50]],
             [
                self.start,
                [self.x, self.y+25],
                [self.x, self.y+50],
                [self.x-25, self.y+50]],
             ])
        self.blocks = [block(self.color, cord=cord) for cord in self.blockcor]
        self.dt = []
        self.dtl = []
        self.score = 0

    def right(self):
        blockcor1 = [[s[0]+25, s[1]] for s in self.blockcor]
        if IsTurnr(blockcor1, self.dtl):
            self.blockcor = blockcor1
            for i in range(len(self.blockcor)):
                self.blocks[i].update(self.blockcor[i])

    def left(self):
        blockcor1 = [[s[0]-25, s[1]] for s in self.blockcor]
        if IsTurnl(blockcor1, self.dtl):
            self.blockcor = blockcor1
            for i in range(len(self.blockcor)):
                self.blocks[i].update(self.blockcor[i])

    def update(self):
        blockcor1 = [[s[0], s[1]+25] for s in self.blockcor]
        if IsRun(self.dtl, blockcor1):
            self.blockcor = blockcor1
            for i in range(len(self.blockcor)):
                self.blocks[i].update(self.blockcor[i])

        else:
            # print(IsStop(self.blockcor))
            if IsStop(self.blockcor):
                self.run = False
            for dnn in self.blockcor:
                self.dtl.append(dnn)
                self.dt.append(block(self.color, dnn))
            self.start = [random.randint(0, 4)*25+250, 0]
            self.x, self.y = self.start
            self.color = random.choice(
                [(20, 200, 50), (50, 10, 190), (20, 250, 10), (150, 100, 30)])
            # print(self.color)
            self.blockcor = random.choice(
                [[
                    self.start],
                 [
                    self.start,
                    [self.x, self.y+25]],
                 [
                    self.start,
                    [self.x, self.y+25],
                    [self.x, self.y+50]],
                 [
                    self.start,
                    [self.x+25, self.y],
                    [self.x, self.y+25],
                    [self.x-25, self.y+25]],
                 [
                    self.start,
                    [self.x-25, self.y],
                    [self.x, self.y+25],
                    [self.x+25, self.y+25]],
                 [
                    self.start,
                    [self.x+25, self.y]],

                 [
                    self.start,
                    [self.x-25, self.y],
                    [self.x+25, self.y]],
                 [
                    self.start,
                    [self.x+25, self.y],
                    [self.x, self.y+25],
                    [self.x+25, self.y+25]],
                 [
                    self.start,
                    [self.x, self.y+25],
                    [self.x, self.y+50],
                    [self.x+25, self.y+50]],
                 [
                    self.start,
                    [self.x, self.y+25],
                    [self.x, self.y+50],
                    [self.x-25, self.y+50]],
                 ])
            self.blocks = [block(self.color, cord) for cord in self.blockcor]
            self.score += 1

    def draw(self):
        for dnn in self.dt:
            dnn.draw()
        for blo in self.blocks:
            blo.draw()


# Game loop.

tetr = tet()
t = 0
while True:
    t += 1
    # print("hi")
    screen.fill((255, 250, 200))
    pygame.draw.rect(screen, (30, 70, 20), [200, 0, 300, 500])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if tetr.run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            tetr.right()
            # print("right")
        if keys[pygame.K_LEFT]:
            tetr.left()
            # print("left")
        if keys[pygame.K_DOWN]:
            tetr.update()        # Draw.
            tetr.draw()
            pygame.draw.rect(screen, (30, 70, 20), [200, 0, 300, 500])

        # Update.
        if t % 3 == 0:
            t = 0
            tetr.update()
    txt = font.render('score:' + str(tetr.score), 1, (0, 0, 0))
    tetr.draw()
    screen.blit(txt, (20, 20))
    pygame.display.flip()
    fpsClock.tick(9)
