# -*- coding: utf-8 -*-

class IMPO:
    def __init__(self , socket ,name,ip,pos,mouse,tread):
        self.socket = socket
        self.name = name
        self.ip = ip
        self.pos= pos
        self.mouse= mouse
        self.tread = tread




    def __str__(self):
        return "hi"