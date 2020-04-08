# -*- coding: utf-8 -*-
import pygame
import math
import random
import time
from impo import *
from PIL import Image, ImageChops
import server_parmeters


def drow_scoewer(screen,x,y,color,border,scower):
    pygame.draw.rect(screen, color,(border+x*(1+scower)+1,border+y*(1+scower)+1,scower,scower))

def drowtext(screen,x,y,size,text):
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(text,True,(0,0,0))
    textRect = text.get_rect()
    textRect.center = (x, y)
    screen.blit(text, textRect)

def main_sean(screen,clock,name,socket,mts):
    ww=700
    wh=700




    scower = 30
    border = (ww-(scower*20+20))/2
    white =(255,255,255)
    gray =(100,100,100)
    red = (255,0,0)
    blue =(0,0,255)
    green = (0,255,0)
    black =(0,0,0)
    fr =60



    speed=6


    t =0
    mt =0

    lenf= 3
    snake = {}
    last_point =[4,4]

    finese= False
    chenes= True
    apple = [14,14]
    lost = False

    old = open("C:\Users\Itay\PycharmProjects\itay\project\images\\erly"+name+".png", "w")
    old.close()
    dif = open("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+name+".png","w")
    dif.close()


    while not finese:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mts.put((socket, "quit"))
                finese = True
                print 2




        if(last_point[0]==apple[0] and last_point[1]==apple[1]):
            lenf +=1
            while(True):
                apple[0]=random.randrange(20)
                apple[1]=random.randrange(20)
                if last_point[0]==apple[0] and last_point[1]==apple[1]:
                    pass
                else:
                    l = False
                    for i in snake:

                        if int(i[0:i.find(",")])==apple[0] and int(i[i.find(",")+1:])==apple[1]:
                            l = True
                    if  not l:
                        break



        screen.fill(gray)
        pygame.draw.rect(screen, white,(border,border,ww-border*2,ww-border*2))
        for i in xrange(0,21):
            pygame.draw.line(screen, black,(border,border+scower*i+i),(ww-border,border+scower*i+i), 1)
        for i in xrange(0,21):
            pygame.draw.line(screen, black,(border+scower*i+i,border),(border+scower*i+i,ww-border ), 1)

        score =  (lenf - 3)
        drowtext(screen,350,30,30,"score " + str(score))





        for i in snake:
            drow_scoewer(screen,int(i[0:i.find(",")]),int(i[i.find(",")+1:]),blue,border,scower)


        drow_scoewer(screen,apple[0],apple[1],red,border,scower)

        drow_scoewer(screen,last_point[0],last_point[1],green,border,scower)

        if mt ==60/speed:


            mt = 0
            snake[str(last_point[0])+","+str(last_point[1])] = t+lenf
            t+=1
            for i in snake.copy():
                if (snake[i]== t):
                    snake.pop(i)

            if server_parmeters.pos.value ==1:
                last_point=[last_point[0]+1,last_point[1]]
                if last_point[0]+1==21:
                    last_point[0]= 0
            if server_parmeters.pos.value==2:
                last_point=[last_point[0],last_point[1]+1]
                if last_point[1]+1==21:
                    last_point[1]= 0
            if server_parmeters.pos.value==3:
                last_point=[last_point[0]-1,last_point[1]]
                if last_point[0]-1==-2:
                    last_point[0]= 19
            if server_parmeters.pos.value==4:
                last_point=[last_point[0],last_point[1]-1]
                if last_point[1]-1==-2:
                    last_point[1]= 19

            for i in snake:

                if int(i[0:i.find(",")])==last_point[0] and int(i[i.find(",")+1:])==last_point[1]:
                    lost= True
                    break



        pygame.draw.circle(screen, green, pygame.mouse.get_pos(), 10)

        if mt ==0:
            tm =time.time()


            lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+name+".png", "rb")
            old = open("C:\Users\Itay\PycharmProjects\itay\project\images\\erly"+name+".png", "wb")
            old.seek(0)
            old.truncate()
            lat.seek(0)
            old.write(lat.read())
            old.close()
            lat.close()

            # print time.time() - tm

            lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+name+".png","wb")
            lat.seek(0)
            lat.truncate()
            lat.close()

            # print time.time() - tm

            diff = open("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+name+".png", "wb")
            diff.seek(0)
            diff.truncate()
            diff.close()

            # print time.time() - tm

            pygame.image.save(screen,"C:\Users\Itay\PycharmProjects\itay\project\images\\send"+name+".png")
            img1 = Image.open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+name+".png")
            img2= Image.open("C:\Users\Itay\PycharmProjects\itay\project\images\\erly"+name+".png")



            diff = ImageChops.difference(img1,img2)
            diff.save("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+name+".png")

            diff.close()
            img1.close()
            img2.close()

            # print time.time() - tm

            dif = open("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+name+".png","rb")


            mts.put((socket, dif.read()))
            dif.close()
            # print time.time() - tm

        if lost:
            # print 1
            mts.put((socket, "quit"))
            finese = True

        else:
            mt +=1
        pygame.display.flip()

        clock.tick(fr)


    pygame.quit()
