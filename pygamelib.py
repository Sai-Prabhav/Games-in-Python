import pygame
clock = pygame.time.Clock()
win = pygame.display.set_mode((500+20, 520))
pygame.init()

black = (255, 255, 255)


def inthebox(posofbox, poscus, wid, heig):
    if posofbox[1] <= poscus[1] and posofbox[0] <= poscus[0] and poscus[0] < posofbox[0]+wid and poscus[1] < posofbox[1]+heig:
        return True

    else:
        return False


def button(surf, tex, x, y, width, height, activeColor, inactiveColor, action=None, font=pygame.font.SysFont('Arial.ttf', 30, True)):
    pos = pygame.mouse.get_pos()

    if inthebox((x, y), pos, width, height):
        pygame.draw.rect(surf, activeColor, pygame.Rect(x, y, width, height))
    else:
        pygame.draw.rect(surf, inactiveColor, pygame.Rect(x, y, width, height))


run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
    button(win, 'hi', 269, 100, 50, 100,
           (0, 200, 2), (4, 6, 200), action=None)
    pygame.display.update()
    clock.tick(80)
