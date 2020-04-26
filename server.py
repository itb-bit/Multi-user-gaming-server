# -*- coding: utf-8 -*-
import threading
import socket
import select
from multiprocessing import Process, Queue, Value,Array

from impo import *
import server_screen


def send_waiting_messages(wlist):

    while(not mts.empty()):
        message = mts.get()
        (cs, data) = message
        try:
            client_socket = limpo[cs].socket
            if client_socket in wlist:
                if(data == "quit")  :
                    pass
                client_socket.send(data+"endend")
        except:
            pass


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
                limpo[str(new_socket)]= IMPO(new_socket,"name",address,Value('i', 1),Array('i', range(3)),"")




            else:
                try:
                    data = current_socket.recv(1024)
                    # print data
                    if data == "":

                        open_client_sockets.remove(current_socket)
                        print "Connection with client closed."
                        limpo[str(current_socket)].pos.value = -1
                        del limpo[str(current_socket)]


                    elif data[-3::] == "pos":
                        limpo[str(current_socket)].pos.value = (int(data[:-3:]))

                    elif data[-4::] == "name":
                        limpo[str(current_socket)].name= data[:-4:]

                        limpo[str(current_socket)].tread = Process(target=server_screen.main_sean,args=(limpo[str(current_socket)].name,
                                limpo[str(current_socket)].pos,str(limpo[str(current_socket)].socket) ,mts,(limpo[str(current_socket)].mouse),))
                        limpo[str(current_socket)].tread.start()
                    elif data[-5::] == "mouse":
                        data= data[:-5:]

                        b = (data).split(" ")

                        limpo[str(current_socket)].mouse[0] = int(b[0])
                        limpo[str(current_socket)].mouse[1] = int(b[1])
                        if  len(b[2]) ==1:
                            limpo[str(current_socket)].mouse[2] = int(b[2])
                        else:
                            limpo[str(current_socket)].mouse[2] = 0
                    else:
                        pass
                except:
                    open_client_sockets.remove(current_socket)
                    print "Connection with client closed."
                    limpo[str(current_socket)].pos.value = -1
                    del limpo[str(current_socket)]


        send_waiting_messages(wlist)

def main():
    """
    Add Documentation here
    """


    serv = threading.Thread(target=server1)
    serv.start()


if __name__ == '__main__':
    main()




