# -*- coding: utf-8 -*-
import threading
import socket
import select
from multiprocessing import Process, Queue, Value, Array
from impo import *
import server_screen
import server_var
import server_pong


def send_waiting_messages(wlist):
    """Moving between single-player games and multiple-player games"""
    while not server_var.mts.empty():
        message = server_var.mts.get()
        (cs, data) = message
        try:
            client_socket = server_var.limpo[cs].socket
            if client_socket in wlist:
                if data == "quit":
                    pass
                client_socket.send(data+"endend")
        except:
            pass


def multyplayer():
    """Moving between single-player games and multiple-player games"""
    emty_pong = True
    pongs = []

    while True:
        for i in server_var.limpo.values():
            if i.com.value == 2:

                if emty_pong:
                    name2 = Array('c', 'name')
                    pos2 = Value('i', 1)
                    socket2 = Queue()
                    mouse2 = Array('i', range(3))
                    com2 = Value('i', 1)

                    i.tread = Process(target=server_pong.main_pong, args=(server_var.mts, i.name, i.pos, str(i.socket),
                                                                          i.mouse, i.com, name2, pos2, socket2, mouse2,
                                                                          com2,))
                    pongs.append(i.tread)
                    i.tread.start()
                    i.com.value = 0
                else:

                    name2.value = i.name
                    i.pos = pos2
                    socket2.put(str(i.socket))
                    i.mouse = mouse2
                    i.com = com2
                    i.com.value = 0

                emty_pong = not emty_pong

            if i.com.value == 1:

                i.tread = Process(target=server_screen.main_sean, args=(i.name, i.pos, str(i.socket),
                                                                        server_var.mts, i.mouse, i.com,))
                i.tread.start()
                i.com.value = 0


def server1():
    """The server"""
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 1720))
    server_socket.listen(5)
    open_client_sockets = []

    server_var.mts = Queue()

    server_var.limpo = {}
    mgames = threading.Thread(target=multyplayer)
    mgames.start()

    while True:

        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets,  open_client_sockets, [])

        for current_socket in rlist:
            if current_socket is server_socket:
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
                server_var.limpo[str(new_socket)] = IMPO(new_socket, "name", address, Value('i', 1),
                                                         Array('i', range(3)), "", Value('i', 0))

            else:
                try:
                    data = current_socket.recv(1024)
                    # print data
                    if data == "":

                        open_client_sockets.remove(current_socket)
                        print "Connection with client closed."
                        server_var.limpo[str(current_socket)].pos.value = -1
                        del server_var.limpo[str(current_socket)]

                    elif data[-3::] == "pos":
                        server_var.limpo[str(current_socket)].pos.value = (int(data[:-3:]))

                    elif data[-4::] == "name":
                        server_var.limpo[str(current_socket)].name = data[:-4:]

                        server_var.limpo[str(current_socket)].tread = \
                            Process(target=server_screen.main_sean,
                                    args=(server_var.limpo[str(current_socket)].name,
                                          server_var.limpo[str(current_socket)].pos,
                                          str(server_var.limpo[str(current_socket)].socket), server_var.mts,
                                          server_var.limpo[str(current_socket)].mouse,
                                          server_var.limpo[str(current_socket)].com,))
                        server_var.limpo[str(current_socket)].tread.start()
                    elif data[-5::] == "mouse":
                        data = data[:-5:]

                        b = data.split(" ")

                        server_var.limpo[str(current_socket)].mouse[0] = int(b[0])
                        server_var.limpo[str(current_socket)].mouse[1] = int(b[1])
                        if len(b[2]) == 1:
                            server_var.limpo[str(current_socket)].mouse[2] = int(b[2])
                        else:
                            server_var.limpo[str(current_socket)].mouse[2] = 0
                    else:
                        pass
                except:
                    open_client_sockets.remove(current_socket)
                    print "Connection with client closed."
                    server_var.limpo[str(current_socket)].pos.value = -1
                    del server_var.limpo[str(current_socket)]

        send_waiting_messages(wlist)


def main():
    """
    Add Documentation here
    """

    serv = threading.Thread(target=server1)
    serv.start()


if __name__ == '__main__':
    main()