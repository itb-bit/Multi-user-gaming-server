# -*- coding: utf-8 -*-
from PIL import Image

import socket
import select
import msvcrt
import pygame
import math
import random
import threading
import time
import config
import numpy as np
import os
from Tkinter import *
import gui_for_pro
from PIL import Image, ImageChops





def client():
    config.name = gui_for_pro.reg()



    my_socket = socket.socket()



    my_socket.connect((raw_input("Enter your server ip: ") ,1720))

    t = True
    f = True
    data =""

    lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"lates.png", "w")
    lat.close()
    img1 = Image.open('C:\Users\Itay\PycharmProjects\itay\project\images\p3.png')
    diff = ImageChops.difference(img1,img1)
    diff.save("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"lates.png")
    diff.close()
    img1.close()




    while True:
        rlist, wlist, xlist = select.select( [my_socket] ,  [my_socket], [])

        if f:
            f=False
            my_socket.send(str(config.name)+"name")

        elif config.pos!=0:
            my_socket.send(str(config.pos))
            config.pos =0

        if  len(rlist)>0:

            data +=my_socket.recv(5000000)
            if len(data) >6 and data[-6::]=="endend":

                data = data[:-6:]
                if  data == "quit":

                    config.fin = True
                    break
                # print data

                while(config.img):
                    pass
                config.img= True

                old = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"old.png", "w")
                dif = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"diff.png", "w")
                old.close()

                dif.close()

                lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"lates.png","rb")
                old = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"old.png","wb")
                old.seek(0)
                old.truncate()
                lat.seek(0)
                old.write(lat.read())
                old.close()
                lat.close()

                dif = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"diff.png", "wb")
                dif.seek(0)
                dif.truncate()
                dif.close()

                lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"lates.png","wb")
                lat.seek(0)
                lat.truncate()
                lat.close()

                dif = open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"diff.png", "wb")
                dif.write(data)
                dif.close()

                old= Image.open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"old.png")
                dif= Image.open("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"diff.png")
                let =(ImageChops.difference(old,dif))
                let.save("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"lates.png")

                old.close()
                dif.close()
                let.close()

                config.img= False
                data =""
                if t:

                    graf = threading.Thread(target=game1)
                    graf.start()
                    t = False


    my_socket.close()






def game1():
    #global config.pos       # Optional if you treat a as read-only


    ww=700
    wh=700

    pygame.init()
    size =(ww,wh)



    white =(255,255,255)
    gray =(100,100,100)
    red = (255,0,0)
    blue =(0,0,255)
    green = (0,255,0)
    black =(0,0,0)

    fr =10

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("player1"+config.name)
    config.fin = False
    while not config.fin:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.fin = True
            elif  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    config.pos = 4
                if event.key == pygame.K_DOWN:

                    config.pos = 2
                if event.key == pygame.K_RIGHT:

                    config.pos = 1
                if event.key == pygame.K_LEFT:

                    config.pos = 3
        while(config.img):
                pass
        config.img= True
        p = pygame.image.load("C:\Users\Itay\PycharmProjects\itay\project\images\\"+config.name+"lates.png")
        screen.blit(p, (0,0))
        config.img= False




        pygame.display.flip()
        clock.tick(fr)


    pygame.quit()

def main():
    """
    Add Documentation here
    """


    client1 = threading.Thread(target=client)

    client1.start()



if __name__ == '__main__':
    main()




