# -*- coding: utf-8 -*-

import pygame
import math
import numpy as np
import time
import pong_parmeters
import color


def drowtext(screen, x, y, size, text):
    """Draw white text"""
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color.white)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def drowtextbl(screen, x, y, size, text):
    """Draw black text"""
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color.black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def main_pong(mts, name1, pos1, socket1, mouse1, com1, name2, pos2, socket2, mouse2, com2):
    """The function responsible for the order of the screens in Pong"""
    ww = 700
    wh = 700

    pygame.init()
    size = (ww, wh)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(str("pong"))

    pong_parmeters.mouse1 = mouse1
    pong_parmeters.pos1 = pos1
    pong_parmeters.name1 = name1
    pong_parmeters.socket1 = socket1
    pong_parmeters.mouse2 = mouse2
    pong_parmeters.pos2 = pos2
    pong_parmeters.name2 = name2
    pong_parmeters.socket2q = socket2
    pong_parmeters.socket2 = ""
    pong_parmeters.mts = mts
    pong_parmeters.screen = screen

    pong_parmeters.lat = np.zeros((700, 700, 3), dtype=np.uint8)
    pong_parmeters.old = np.zeros((700, 700, 3), dtype=np.uint8)

    finish = False
    while pong_parmeters.socket2q.empty():
        loading(screen, clock, 96)
    black_screen(screen, clock, 10)
    pong_parmeters.socket2 = pong_parmeters.socket2q.get()
    t = pong(screen, clock)
    if t == "quit":
        finish = True

    if finish:
        mts.put((pong_parmeters.socket1, "quit"))
        mts.put((pong_parmeters.socket2, "quit"))
    else:
        black_screen(screen, clock, 3)
        com1.value = 1
        com2.value = 1

    pygame.quit()


def black_screen(screen, clock, time1):
    """A black screen"""
    quity = time1
    finese = False

    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finese = True
                return "quit"

        if pong_parmeters.pos1.value == -1:
            return "quit"

        screen.fill(color.black)
        if quity == 0:
            return "hi"
        quity -= 1

        pygame.display.flip()

        sending_info()
        clock.tick(pong_parmeters .fr)


def loading(screen, clock, time1):
    """A loading screen"""
    finese = False
    quity = time1
    b = 16
    j = b-1
    c = 0

    rangel = 150
    while not finese:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finese = True
        screen.fill(color.white)
        drowtextbl(screen, 350, 100, 40, "searching for a worthy opponent ...")
        for i in xrange(0, b):
            if i != j:
                pygame.draw.circle(screen, color.red, [350 + int(rangel*math.sin(i*(math.pi*2/b))),
                                                       350 + int(rangel*math.cos(i*(math.pi*2/b)))], 20)
        pygame.draw.circle(screen, color.green, pygame.mouse.get_pos(), 10)

        c += 1
        if c == 6:
            c = 0
            j -= 1
            pygame.display.flip()
            sending_info()
        if j == -1:
            j = b-1

        if quity == 0:
            return "hi"
        quity -= 1

        clock.tick(pong_parmeters.fr)


def sending_info():
    """Sending information to client"""
    tm = time.time()

    pong_parmeters.old = pong_parmeters.lat

    # print time.time() - tm
    pong_parmeters.lat = pygame.surfarray.array3d(pong_parmeters.screen)

    # print time.time() - tm
    diff = np.bitwise_xor(pong_parmeters.old, pong_parmeters.lat)

    # print time.time() - tm
    en = diff.tobytes()

    # print time.time() - tm
    c = en.encode("zlib")

    # print time.time() - tm
    pong_parmeters.mts.put((pong_parmeters.socket1, c))
    if pong_parmeters.socket2 != "":
        pong_parmeters.mts.put((pong_parmeters.socket2, c))

    # print time.time() - tm

    # print "___________"


def pong(screen, clock):
    """The game pong"""
    t = 0
    mt = 0

    p1p = 300

    p1c = 0

    p1s = 0
    p2s = 0

    speed = 8
    p2p = 300

    p2c = 0
    len = 80

    br = 10
    b = [350, 350]
    bm = [-6, 1]

    p1s = 0
    p2s = 0
    finese = False
    chenes = True

    lost = False
    ww = 700
    wh = 700

    pygame.init()

    fr = 60
    speed = 10

    ttnm = 0

    while not finese:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

        if pong_parmeters.pos1.value == -1:
            return "quit"
        if pong_parmeters.pos2.value == -1:
            return "quit"

        if pong_parmeters.pos1.value/8 % 2 == 1:
            p2c = -speed
        if pong_parmeters.pos1.value/2 % 2 == 1:

            p2c = speed

        if pong_parmeters.pos2.value/8 % 2 == 1:

            p1c = -speed
        if pong_parmeters.pos2.value/2 % 2 == 1:

            p1c = speed

        if p2c == -speed and pong_parmeters.pos1.value/8 % 2 == 0:

            p2c = 0
        if p2c == speed and pong_parmeters.pos1.value/2 % 2 == 0:

            p2c = 0

        if p1c == -speed and pong_parmeters.pos2.value/8 % 2 == 0:

            p1c = 0
        if p1c == speed and pong_parmeters.pos2.value/2 % 2 == 0:

            p1c = 0

        screen.fill(color.black)

        for i in xrange(0, 14):
            pygame.draw.rect(screen, color.white, [345, i*50+25, 10, 25])

        if p2p + p2c >= 0 and p2p + p2c + len < wh:
            p2p += p2c
        if p1p + p1c >= 0 and p1p + p1c + len < wh:
            p1p += p1c

        drowtext(screen, 500, 100, 50, str(p2s))
        drowtext(screen, 200, 100, 50, str(p1s))

        if p2s == 11:
            return 2
        if p1s == 11:
            return 1

        pygame.draw.rect(screen, color.white, [50, p1p, 20, len])

        pygame.draw.rect(screen, color.white, [630, p2p, 20, len])

        if b[1] + bm[1] - br < 0 or b[1] + bm[1] + br >= wh:
            bm[1] = -bm[1]

        if b[0] + bm[0] - br < 0:
            b = [350, 350]
            bm = [6, 1]
            p2s += 1

        if b[0] + bm[0] + br >= ww:
            b = [350, 350]
            bm = [-6, 1]
            p1s += 1

        if b[0] + bm[0]  >= 50 and b[0] + bm[0] <= 70:
            if p1p < b[1] + br and p1p + 40 > b[1] + br:
                bm[0] = -bm[0]
                bm[1] -= 2
            elif p1p  + len < b[1] - br and p1p +len  - 40 > b[1] - br:
                bm[0] = - bm[0]
                bm[1] += 2
            elif p1p < b[1] and p1p + len > b[1]:
                bm[0] = -bm[0]
                bm[1] = bm[1]

        if b[0] + bm[0] + br >= 630 and b[0] + bm[0] - br <= 650:
            if p2p < b[1] + br and p2p + 40 > b[1] + br:
                bm[0] = -bm[0]
                bm[1] -= 2
            elif p2p + len < b[1] - br and p2p + len - 40 > b[1] - br:
                bm[0] = -bm[0]
                bm[1] += 2
            elif p2p < b[1] + br and p2p + len > b[1] - br:
                bm[0] = -bm[0]
                bm[1] = bm[1]
        b = np.add(b, bm)

        #pygame.draw.circle(screen, color.gray, b, br)

        pygame.display.flip()

        if ttnm == 0:
            sending_info()
            ttnm = 2
        ttnm -= 1
        clock.tick(fr)