# -*- coding: utf-8 -*-
import os
import time
import threading
import socket
import select
import pygame
import math
import random
from PIL import Image, ImageChops
from impo import *
from massages_to_send import *
import server_snake
from multiprocessing import Process, Queue, Pipe, Value

def send_waiting_messages(wlist):

    while(not mts.empty()):
        message = mts.get()
        (cs, data) = message
        client_socket = limpo[cs].socket
        if client_socket in wlist:
            if(data == "quit")  :
                pass
            client_socket.send(data+"endend")


def server1():

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 1720))
    server_socket.listen(5)
    open_client_sockets = []
    global mts
    mts = Queue()
    global limpo
    limpo = {}




    while True:

        rlist, wlist, xlist = select.select( [server_socket] + open_client_sockets,  open_client_sockets, [])


        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address)= server_socket.accept()
                open_client_sockets.append(new_socket)
                limpo[str(new_socket)]= IMPO(new_socket,"name",address,Value('i', 1),"")




            else:
                data = current_socket.recv(1024)
                if data == "":

                    open_client_sockets.remove(current_socket)
                    print "Connection with client closed."
                elif len(data)==1:
                    limpo[str(current_socket)].pos.value = (int(data))

                elif data[-4::] == "name":
                    limpo[str(current_socket)].name= data[:-4:]

                    lat = open("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+limpo[str(new_socket)].name+".png", "w")
                    lat.close()
                    img1 = Image.open('C:\Users\Itay\PycharmProjects\itay\project\images\p3.png')
                    diff = ImageChops.difference(img1,img1)
                    diff.save("C:\Users\Itay\PycharmProjects\itay\project\images\\send"+limpo[str(new_socket)].name+".png")
                    diff.close()
                    img1.close()



                    limpo[str(current_socket)].tread = Process(target=server_snake.main_sean,args=(limpo[str(current_socket)].name,
                                                     limpo[str(current_socket)].pos,str(limpo[str(current_socket)].socket) ,mts,))
                    limpo[str(current_socket)].tread.start()

                else:
                    mts.put((current_socket, 'Hello, ' + data))
        send_waiting_messages(wlist)

def main():
    """
    Add Documentation here
    """


    serv = threading.Thread(target=server1)
    serv.start()


if __name__ == '__main__':
    main()




