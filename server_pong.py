# -*- coding: utf-8 -*-

import pygame
import math
import random
import numpy as np
import time
import server_parmeters



def drowtext(screen,x,y,size,text):
    white =(255,255,255)
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text,True,white)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)


def pong(screen,clock):

    t =0
    mt =0

    p1p = 300

    p1c = 0

    p1s =0
    p2s=0

    speed =8
    p2p =300

    p2c =0
    len = 80

    br = 10
    b = [350,350]
    bm = [-6,1]

    p1s=0
    p2s = 0
    finese= False
    chenes= True

    lost = False
    ww=700
    wh=700

    pygame.init()




    white =(255,255,255)
    gray =(100,100,100)
    red = (255,0,0)
    blue =(0,0,255)
    green = (0,255,0)
    black =(0,0,0)
    lblue = (51, 204, 255)
    orenge = (255, 153, 51)
    yellow = (255, 255, 0)
    perpole = (153, 0, 204)



    fr =60
    speed =10


    while not finese:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return "quit"

        if server_parmeters.pos.value ==-1:
            return "quit"

        if server_parmeters.pos== 1:
            p2c = -speed
        if server_parmeters.pos== 2:

            p2c = speed

        if event.key == pygame.K_w:

            p1c = -speed
        if event.key == pygame.K_s:

            p1c = speed

        if event.key == pygame.K_UP:

            p2c = 0
        if event.key == pygame.K_DOWN:

            p2c = 0

        if event.key == pygame.K_w:

            p1c = 0
        if event.key == pygame.K_s:

            p1c = 0





        screen.fill(black)

        for i in xrange(0,14) :
            pygame.draw.rect(screen, white,[345,i*50+25,10,25])


        if (p2p + p2c  >=0 and p2p + p2c +len  < wh):
            p2p = p2p +p2c
        if (p1p + p1c  >=0 and p1p + p1c +len  < wh):
            p1p = p1p +p1c

        drowtext(screen,500,100,50,str(p2s))
        drowtext(screen,200,100,50,str(p1s))

        pygame.draw.rect(screen, white,[50,p1p,20,len])

        pygame.draw.rect(screen, white,[630,p2p,20,len])


        if (b[1]+bm[1] -br <0 or b[1]+bm[1] +br  >= wh):
            bm[1] = - bm[1]
        if (b[0]+bm[0] -br <0):
            b= [350,350]
            bm = [6,1]
            p2s +=1
        if (b[0]+bm[0] +br  >= ww):

            b= [350,350]
            bm = [-6,1]
            p1s +=1

        if (b[0]+bm[0]  >= 50 and b[0]+bm[0]  <= 70):
            if(p1p < b[1] + br  and p1p + 40 > b[1] + br ):
                bm[0] = - bm[0]
                bm[1] = bm[1] -2
            elif(p1p  + len< b[1] - br  and p1p +len  - 40 > b[1]  -br ):
                bm[0] = - bm[0]
                bm[1] = bm[1] +2
            elif(p1p < b[1]   and p1p +len   > b[1]  ):
                bm[0] = - bm[0]
                bm[1] = bm[1]


        if (b[0]+bm[0] +br >= 630 and b[0]+bm[0] -br <= 650):
            if(p2p < b[1] + br  and p2p + 40 > b[1] + br ):
                bm[0] = - bm[0]
                bm[1] = bm[1] -2
            elif(p2p  + len< b[1] - br  and p2p +len  - 40 > b[1]  -br ):
                bm[0] = - bm[0]
                bm[1] = bm[1] +2
            elif(p2p < b[1] + br  and p2p +len   > b[1]  -br ):
                bm[0] = - bm[0]
                bm[1] = bm[1]
        b = np.add(b,bm)


        pygame.draw.circle(screen, gray, b, br)

        pygame.draw.circle(screen, green, pygame.mouse.get_pos(), 10)


        pygame.display.flip()

        clock.tick(fr)



def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()