# -*- coding: utf-8 -*-

import time
import numpy as np
from server_menu import *
import server_snake
import server_parmeters


def main_sean(name, pos, socket, mts, mouse, com):
    """Responsible for the screen on which one player's games are running"""
    ww = 700
    wh = 700

    pygame.init()
    size = (ww, wh)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(str(name))

    server_parmeters.mouse = mouse
    server_parmeters.pos = pos
    server_parmeters.name = name
    server_parmeters.socket = socket
    server_parmeters.mts = mts
    server_parmeters.screen = screen

    server_parmeters.lat = np.zeros((700, 700, 3), dtype=np.uint8)
    server_parmeters.old = np.zeros((700, 700, 3), dtype=np.uint8)

    finish = False

    while not finish:
        g = first_sean(screen, clock)
        if g == "s":
            s = snake_speed(screen, clock)
            if s == "quit":
                finish = True
            else:
                t = server_snake.main_sean(screen, clock, s)
                if t == "quit":
                    finish = True
        elif g == "p":

            t = loading(screen, clock, 30)
            if t == "quit":
                    finish = True
            else:
                black_screen(screen, clock, 3)
                com.value = 2
            break

        elif g == "quit":
            finish = True

    pygame.quit()
    if finish:
        mts.put((socket, "quit"))


def sending_info():
    """Sending information to client"""
    tm = time.time()

    server_parmeters.old = server_parmeters.lat

    # print time.time() - tm
    server_parmeters.lat = pygame.surfarray.array3d(server_parmeters.screen)

    # print time.time() - tm
    diff = np.bitwise_xor(server_parmeters.old, server_parmeters.lat)

    # print time.time() - tm
    en = diff.tobytes()

    # print time.time() - tm
    c = en.encode("zlib")

    # print time.time() - tm
    server_parmeters.mts.put((server_parmeters.socket, c))

    time.time() - tm

    # print "___________"