# -*- coding: utf-8 -*-
import pygame
import math
import random
import time
from impo import *
from PIL import Image, ImageChops
import threading
import mmap
from server_menu import  first_sean
import server_snake
import server_parmeters

def main_sean(name,pos,socket,mts,mouse ):
    ww=700
    wh=700




    pygame.init()
    size =(ww,wh)

    fr =60

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(str(name))

    sspeed=6

    lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+name+".png", "w")
    old = open("C:\Users\Itay\PycharmProjects\itay\project\images\\erly"+name+".png", "w")
    diff = open("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+name+".png", "w")

    lat.close()
    old.close()
    diff.close()

    old = open("C:\Users\Itay\PycharmProjects\itay\project\images\\null.png", "rb")
    lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+name+".png", "wb")
    lat.seek(0)
    lat.truncate()
    old.seek(0)
    lat.write(old.read())

    lat.close()
    old.close()

    server_parmeters.mouse = mouse
    server_parmeters.pos = pos
    server_parmeters.name = name
    server_parmeters.socket = socket
    server_parmeters.mts = mts
    server_parmeters.screen = screen


    new = mmap.mmap(-1, 200)
    oldy = mmap.mmap(-1, 200)
    diffy = mmap.mmap(-1, 200)




    g =  first_sean(screen,clock)
    if(g == "s"):
        server_snake.main_sean(screen,clock,name,socket,mts)
    elif(g== "p"):
        pass
    elif(g== "a"):
        pass
    elif(g== "t"):
        pass




    pygame.quit()






def sending_info():
    tm =time.time()


    lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+server_parmeters.name+".png", "rb")
    old = open("C:\Users\Itay\PycharmProjects\itay\project\images\\erly"+server_parmeters.name+".png", "wb")
    old.seek(0)
    old.truncate()
    lat.seek(0)
    old.write(lat.read())
    old.close()
    lat.close()

    # print time.time() - tm

    lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+server_parmeters.name+".png","wb")
    lat.seek(0)
    lat.truncate()
    lat.close()

    # print time.time() - tm

    diff = open("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+server_parmeters.name+".png", "wb")
    diff.seek(0)
    diff.truncate()
    diff.close()

     # print time.time() - tm

    pygame.image.save(server_parmeters.screen,"C:\Users\Itay\PycharmProjects\itay\project\images\\send"+server_parmeters.name+".png")
    img1 = Image.open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+server_parmeters.name+".png")
    img2= Image.open("C:\Users\Itay\PycharmProjects\itay\project\images\\erly"+server_parmeters.name+".png")



    diff = ImageChops.difference(img1,img2)
    diff.save("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+server_parmeters.name+".png")

    diff.close()
    img1.close()
    img2.close()

    # print time.time() - tm

    dif = open("C:\Users\Itay\PycharmProjects\itay\project\images\\diff"+server_parmeters.name+".png","rb")

    print dif.read()
    print "---------------------------"
    dif.seek(0)

    server_parmeters.mts.put((server_parmeters.socket, dif.read()))
    dif.close()
    # print time.time() - tm



def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()