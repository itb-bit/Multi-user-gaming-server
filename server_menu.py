# -*- coding: utf-8 -*-
import pygame
import math
import random
import server_parmeters
import server_screen
from multiprocessing import Process, Queue, Pipe, Value,Array
import color

def botten(screen,x,y,ww,wh,color1,text = "",chanse=False):

    if (chanse):
        if server_parmeters.mouse[0] >=x and server_parmeters.mouse[0] <= x+ww and server_parmeters.mouse[1] >=y and server_parmeters.mouse[1]<= y+wh :
            pygame.draw.rect(screen, color.gray,(x,y,ww,wh))
        else:
            pygame.draw.rect(screen, color1,(x,y,ww,wh))

    else:
        pygame.draw.rect(screen, color1,(x,y,ww,wh))
    drowtext(screen,x+ww/2,y+wh/2,20,text)
    return server_parmeters.mouse[0] >=x and server_parmeters.mouse[0] <= x+ww and server_parmeters.mouse[1] >=y and server_parmeters.mouse[1]<= y+wh  and server_parmeters.mouse[2]

def drowtext(screen,x,y,size,text):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text,True,color.black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
def first_sean(screen,clock):
    screen.fill(color.white)

    finese= False

    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                finese = True
                return "quit"

        if server_parmeters.pos.value ==-1:
            return "quit"

        screen.fill(color.white)
        drowtext(screen,350,100,50,"welcome to flying squirrel")
        drowtext(screen,350,200,30,"choose a game")

        if  (botten(screen,200,300,80,80,color.red,"snake",True)):
            server_screen.sending_info()
            server_parmeters.mouse[2] =0
            return "s"
        if  (botten(screen,300,300,80,80,color.red,"pong",True)):
            server_screen.sending_info()
            server_parmeters.mouse[2] =0
            return "p"
        if  (botten(screen,400,300,80,80,color.red,"actung",True)):
            server_screen.sending_info()
            server_parmeters.mouse[2] =0
            return "a"
        if  (botten(screen,500,300,80,80,color.red,"tetris",True)):
            server_screen.sending_info()
            server_parmeters.mouse[2] =0
            return "t"


        pygame.display.flip()
        server_screen.sending_info()
        clock.tick(server_parmeters.fr)

def snake_speed(screen,clock):

    screen.fill(color.white)
    finese= False
    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finese = True
                return "quit"

        if server_parmeters.pos.value ==-1:
            return "quit"
        screen.fill(color.white)
        drowtext(screen,350,150,50,"chose a snake speed")

        if  (botten(screen,200,300,80,80,color.blue,"6",True)):
            server_screen.sending_info()

            return 6
        if  (botten(screen,300,300,80,80,color.blue,"10",True)):
            server_screen.sending_info()

            return 10
        if  (botten(screen,400,300,80,80,color.blue,"12",True)):
            server_screen.sending_info()

            return 12
        if  (botten(screen,500,300,80,80,color.blue,"15",True)):
            server_screen.sending_info()

            return 15


        pygame.display.flip()
        server_screen.sending_info()
        clock.tick(server_parmeters.fr)
def black_screen(screen,clock,time1):



    quity = time1
    t = False

    finese= False

    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finese = True
                return "quit"

        if server_parmeters.pos.value ==-1:
            return "quit"
        screen.fill(color.black)
        if  quity == 0:
            return "hi"
        quity -= 1


        pygame.display.flip()
        if  not t:
            server_screen.sending_info()
            t = True
        clock.tick(server_parmeters.fr)

def loading(screen,clock,time1):

    finese= False
    quity = time1
    b = 16
    j = b-1
    c =0
    cmax =6
    rangel = 150
    while not finese:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finese = True
        screen.fill(color.white)
        drowtext(screen,350,100,40,"loading ...")
        for i in  xrange(0,b) :
            if  i !=j:
                pygame.draw.circle(screen, color.red, [350+ int(rangel*math.sin(i*(math.pi*2/b))),350+ int(rangel*math.cos(i*(math.pi*2/b)))], 20)
        pygame.draw.circle(screen, color.green, pygame.mouse.get_pos(), 10)
        c +=1
        if c==cmax:
            c= 0
            j-=1
        if  j==-1:
            j=b-1


        if  quity == 0:
            return "hi"
        quity -= 1

        pygame.display.flip()
        server_screen.sending_info()
        clock.tick(server_parmeters.fr)

def main():
    """
    Add Documentation here
    """



if __name__ == '__main__':
    main()

