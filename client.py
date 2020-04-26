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
import pickle


def client():

    config.name = gui_for_pro.reg()
    my_socket = socket.socket()
    my_socket.connect((raw_input("Enter your server ip: ") ,1720))

    t = True
    f = True
    last_mouse = range(3)
    data = ""

    config.lat = np.zeros((700,700,3),dtype=np.uint8)
    config.old = np.zeros((700,700,3),dtype=np.uint8)


    lat_pos= 0

    while True:
        rlist, wlist, xlist = select.select( [my_socket] ,  [my_socket], [])
        if config.fin:
            my_socket.send("")
            break

        if f:
            f=False
            my_socket.send(str(config.name)+"name")

        elif config.pos!=lat_pos:
            my_socket.send(str(config.pos)+"pos")
            lat_pos = config.pos
        elif config.mouse!=last_mouse:

            my_socket.send( str(config.mouse[0]) +" "+ str(config.mouse[1])+ " "+str(config.mouse[2])+ "mouse" )
            last_mouse[0] =  config.mouse[0]
            last_mouse[1] =  config.mouse[1]
            last_mouse[2] =  config.mouse[2]

        if  len(rlist)>0:

            data +=my_socket.recv(5000000)
            #print data
            if len(data) >6 and data[-6::]=="endend":

                data = data[:-6:]

                if  data == "quit":

                    config.fin = True
                    break


                while(config.img):
                    pass
                config.img= True
                config.old = config.lat
                diff = np.frombuffer((((data.decode("zlib")))), dtype=np.uint8).reshape(700, 700,3)
                config.lat =np.bitwise_xor(config.old,diff)
                config.img= False
                data = ""
                if t:
                    graf = threading.Thread(target=game1)
                    graf.start()
                    t = False
    my_socket.close()


def game1():
    ww = 700
    wh = 700
    pygame.init()
    size = (ww,wh)
    fr = 60

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
            elif  event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:

                    config.pos = 0
                if event.key == pygame.K_DOWN:

                    config.pos = 0
                if event.key == pygame.K_RIGHT:

                    config.pos = 0
                if event.key == pygame.K_LEFT:

                    config.pos = 0
        config.mouse[0] = pygame.mouse.get_pos()[0]
        config.mouse[1] = pygame.mouse.get_pos()[1]
        config.mouse[2] = pygame.mouse.get_pressed()[0]
        while(config.img):
                pass
        config.img= True
        pygame.surfarray.blit_array(screen, config.lat)

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




