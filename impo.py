# -*- coding: utf-8 -*-

class IMPO:
    def __init__(self , socket ,name,ip,pos,mouse,tread,com):
        self.socket = socket
        self.name = name
        self.ip = ip
        self.pos= pos
        self.mouse= mouse
        self.tread = tread
        self.com = com




    def __str__(self):
        return "hi"