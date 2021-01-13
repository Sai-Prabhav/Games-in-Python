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


def midrect(x, y, wid1, heig1, text):
    return (x+wid1//2-text[0]//2, y+heig1//2-text[1]//2)


def button(surf, tex, posit, width, height, activeColor, inactiveColor, action, font, click=False):

    x, y = posit
    pos = pygame.mouse.get_pos()
    if inthebox((x, y), pos, width, height):
        pygame.draw.rect(surf, activeColor, pygame.Rect(x, y, width, height))
        text = font.render(tex, 1, inactiveColor)
        if click:
            action()
    else:
        pygame.draw.rect(surf, inactiveColor, pygame.Rect(x, y, width, height))
        text = font.render(tex, 1, activeColor)

    win.blit(text, midrect(x, y, width, height,
                           (text.get_width(), text.get_height())))


def message():
    print('hi')

def drawall(list):
    for things in list:
        things.draw()
    pygame.display.update()

run = True

while run:
    click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True

    button(win, 'hooooi', midrect(0, 0, 520, 520, (150, 100)), 150, 100,
           (0, 200, 2), (4, 6, 200), message, pygame.font.SysFont('Arial.ttf', 30, True), click)
    pygame.display.update()
    clock.tick(80)
