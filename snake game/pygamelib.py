def inthebox(posofbox, poscus, wid, heig):
    if posofbox[1] <= poscus[1] and posofbox[0] <= poscus[0] and poscus[0] < posofbox[0]+wid and poscus[1] < posofbox[1]+heig:
        return True
    else:
        return False


def midrect(x, y, wid1, heig1, widthofob):
    return (x+wid1//2-widthofob[0]//2, y+heig1//2-widthofob[1]//2)


def button(surf, tex, whereToPlaceIt, widthOfButton, heightOfButton, activeColor, inactiveColor, action, font, click=False):
    x, y = whereToPlaceIt
    pos = pygame.mouse.get_pos()
    if inthebox((x, y), pos, widthOfButton, heightOfButton):
        pygame.draw.rect(surf, activeColor, pygame.Rect(
            x, y, widthOfButton, heightOfButton))
        text = font.render(tex, 1, inactiveColor)
        if click:
            action()
    else:
        pygame.draw.rect(surf, inactiveColor, pygame.Rect(
            x, y, widthOfButton, heightOfButton))
        text = font.render(tex, 1, activeColor)

    surf.blit(text, midrect(x, y, widthOfButton, heightOfButton,
                            (text.get_width(), text.get_height())))


def drawall(list):
    for things in list:
        things.draw()
    pygame.display.update()
