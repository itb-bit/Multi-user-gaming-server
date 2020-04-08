# -*- coding: utf-8 -*-
import pygame
import math
import random
import server_parmeters
import server_screen

def botten(screen,x,y,ww,wh,color,text = "",chanse=False):
    gray =(0,0,0)
    if (chanse):
        if server_parmeters.mouse[0] >=x and server_parmeters.mouse[0] <= x+ww and server_parmeters.mouse[1] >=y and server_parmeters.mouse[1]<= y+wh :
            pygame.draw.rect(screen, gray,(x,y,ww,wh))
        else:
            pygame.draw.rect(screen, color,(x,y,ww,wh))

    else:
        pygame.draw.rect(screen, color,(x,y,ww,wh))
    drowtext(screen,x+ww/2,y+wh/2,20,text)
    return server_parmeters.mouse[0] >=x and server_parmeters.mouse[0] <= x+ww and server_parmeters.mouse[1] >=y and server_parmeters.mouse[1]<= y+wh  and server_parmeters.mouse[2]

def drowtext(screen,x,y,size,text):
    black =(0,0,0)
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text,True,black)
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)
def first_sean(screen,clock):

    ww=700
    wh=700


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

    t = 20
    tm = 0

    screen.fill(white)

    finese= False

    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finese = True

        drowtext(screen,350,100,50,"welcome to flying squirrel")

        drowtext(screen,350,200,30,"choose a game")

        if  (botten(screen,200,300,80,80,red,"snake",True)):
            return "s"
        if  (botten(screen,300,300,80,80,red,"pong",True)):
            return "p"
        if  (botten(screen,400,300,80,80,red,"actung",True)):
            return "a"
        if  (botten(screen,500,300,80,80,red,"tetris",True)):
            return "t"
        if tm ==t :
            tm= 0
            server_screen.sending_info()
        tm +=1
        pygame.display.flip()
        clock.tick(fr)




def main():
    """
    Add Documentation here
    """



if __name__ == '__main__':
    main()

