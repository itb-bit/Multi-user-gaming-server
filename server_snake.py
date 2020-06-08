# -*- coding: utf-8 -*-
import pygame
import random
import server_parmeters
import server_screen
import color


def drow_scoewer(screen, x, y, color1, border, scower):
    """Drawing squares in grid"""
    pygame.draw.rect(screen, color1, (border+x*(1+scower)+1, border+y*(1+scower)+1, scower, scower))


def drowtext(screen, x, y, size, text):
    """Draw text"""
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text, True, color.black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def main_sean(screen, clock, speed=6):
    """The game snake"""
    ww = 700
    wh = 700
    scower = 30
    border = (ww-(scower*20+20))/2
    fr = 60
    t = 0
    mt = 0

    lenf = 3
    snake = {}
    last_point = [4, 4]

    finese = False
    chenes = True
    apple = [14, 14]
    lost = False
    last = 1

    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
        if server_parmeters.pos.value == -1:
            return "quit"

        if last_point[0] == apple[0] and last_point[1] == apple[1]:
            lenf += 1
            while True:
                apple[0] = random.randrange(20)
                apple[1] = random.randrange(20)
                if last_point[0] == apple[0] and last_point[1] == apple[1]:
                    pass
                else:
                    l = False
                    for i in snake:

                        if int(i[0:i.find(",")]) == apple[0] and int(i[i.find(",")+1:]) == apple[1]:
                            l = True
                    if not l:
                        break

        screen.fill(color.gray)
        pygame.draw.rect(screen, color.white, (border, border, ww-border*2, ww-border*2))
        for i in xrange(0, 21):
            pygame.draw.line(screen, color.black, (border, border+scower*i+i), (ww-border, border+scower*i+i), 1)
        for i in xrange(0, 21):
            pygame.draw.line(screen, color.black, (border+scower*i+i, border), (border+scower*i+i, ww-border), 1)

        score = (lenf - 3)
        drowtext(screen, 350, 30, 30, "score " + str(score))

        for i in snake:
            drow_scoewer(screen, int(i[0:i.find(",")]), int(i[i.find(",")+1:]), color.blue, border, scower)

        drow_scoewer(screen, apple[0], apple[1], color.red, border, scower)

        drow_scoewer(screen, last_point[0], last_point[1], color.green, border, scower)

        if lost:
            # print 1
            return score

        else:
            mt += 1

        if mt == 60/speed:

            mt = 0
            snake[str(last_point[0]) + "," + str(last_point[1])] = t+lenf
            t += 1
            for i in snake.copy():
                if snake[i] == t:
                    snake.pop(i)

            if server_parmeters.pos.value != 0:
                last = server_parmeters.pos.value

            if last % 2 == 1:
                last_point = [last_point[0]+1, last_point[1]]
                if last_point[0]+1 == 21:
                    last_point[0] = 0
            elif (last/2) % 2 == 1:
                last_point = [last_point[0], last_point[1]+1]
                if last_point[1]+1 == 21:
                    last_point[1] = 0
            elif (last/4) % 2 == 1:
                last_point = [last_point[0]-1, last_point[1]]
                if last_point[0]-1 == -2:
                    last_point[0] = 19
            elif (last/8) % 2 == 1:
                last_point = [last_point[0], last_point[1]-1]
                if last_point[1]-1 == -2:
                    last_point[1] = 19

            for i in snake:

                if int(i[0:i.find(",")]) == last_point[0] and int(i[i.find(",")+1:]) == last_point[1]:
                    lost = True
                    break

            # pygame.draw.circle(screen, color.green, pygame.mouse.get_pos(), 10)

            pygame.display.flip()

            server_screen.sending_info()

        clock.tick(fr)