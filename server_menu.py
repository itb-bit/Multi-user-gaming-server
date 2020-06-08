# -*- coding: utf-8 -*-
import pygame
import math
import server_parmeters
import server_screen
import color


def button(screen, x, y, ww, wh, color1, text="", chanse=False):
    """Making a button"""
    if chanse:
        if server_parmeters.mouse[0] >= x and server_parmeters.mouse[0] <= x + ww and \
                        server_parmeters.mouse[1] >= y and server_parmeters.mouse[1] <= y + wh:
            pygame.draw.rect(screen, color.gray, (x, y, ww, wh))
        else:
            pygame.draw.rect(screen, color1, (x, y, ww, wh))

    else:
        pygame.draw.rect(screen, color1, (x, y, ww, wh))
    drowtext(screen, x+ww/2, y+wh/2, 20, text)
    return server_parmeters.mouse[0] >= x and server_parmeters.mouse[0] <= x + ww and \
           server_parmeters.mouse[1] >= y and server_parmeters.mouse[1] <= y + wh and server_parmeters.mouse[2]


def drowtext(screen, x, y, size, text):
    """Draw text"""
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color.black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def first_sean(screen, clock):
    """Te main menu"""
    screen.fill(color.white)

    finese = False

    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                finese = True
                return "quit"

        if server_parmeters.pos.value == -1:
            return "quit"

        screen.fill(color.white)
        drowtext(screen, 350, 100, 50, "welcome to flying squirrel")
        drowtext(screen, 350, 200, 30, "choose a game")

        if button(screen, 300, 300, 80, 80, color.red, "snake", True):
            server_screen.sending_info()
            server_parmeters.mouse[2] = 0
            return "s"
        if button(screen, 400, 300, 80, 80, color.red, "pong", True):
            server_screen.sending_info()
            server_parmeters.mouse[2] = 0
            return "p"

        pygame.display.flip()
        server_screen.sending_info()
        clock.tick(server_parmeters.fr)


def snake_speed(screen, clock):
    """The snake speed selection screen"""
    screen.fill(color.white)
    finese = False
    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finese = True
                return "quit"

        if server_parmeters.pos.value == -1:
            return "quit"
        screen.fill(color.white)
        drowtext(screen, 350, 150, 50, "chose a snake speed")

        if button(screen, 200, 300, 80, 80, color.blue, "6", True):
            server_screen.sending_info()
            return 6

        if button(screen, 300, 300, 80, 80, color.blue, "10", True):
            server_screen.sending_info()
            return 10

        if button(screen, 400, 300, 80, 80, color.blue, "12", True):
            server_screen.sending_info()
            return 12

        if button(screen, 500, 300, 80, 80, color.blue, "15", True):
            server_screen.sending_info()
            return 15

        pygame.display.flip()
        server_screen.sending_info()
        clock.tick(server_parmeters.fr)


def black_screen(screen, clock, time1):
    """A black screen"""
    quity = time1
    finese = False

    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finese = True
                return "quit"

        if server_parmeters.pos.value == -1:
            return "quit"
        screen.fill(color.black)
        if quity == 0:
            return "hi"
        quity -= 1

        pygame.display.flip()

        server_screen.sending_info()
        clock.tick(server_parmeters.fr)


def loading(screen, clock, time1):
    """A loading screen"""
    finese = False
    quity = time1
    b = 16
    j = b-1
    c = 0
    cmax = 6
    rangel = 150
    while not finese:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finese = True

        if server_parmeters.pos.value == -1:
            return "quit"
        screen.fill(color.white)
        drowtext(screen, 350, 100, 40, "loading ...")
        for i in xrange(0, b):
            if i != j:
                pygame.draw.circle(screen, color.red, [350+int(rangel*math.sin(i*(math.pi*2/b))),
                                                       350+int(rangel*math.cos(i*(math.pi*2/b)))], 20)
        # pygame.draw.circle(screen, color.green, pygame.mouse.get_pos(), 10)
        c += 1
        if c == cmax:
            c = 0
            j -= 1
            pygame.display.flip()
            server_screen.sending_info()

        if j == -1:
            j = b-1

        if quity == 0:
            return "hi"
        quity -= 1

        clock.tick(server_parmeters.fr)