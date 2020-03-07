# -*- coding: utf-8 -*-
from Tkinter import *
import config

def hi():
    config.name= E1.get()
    E1.delete (0,1000)
    top.destroy()

def reg():
    global top
    top = Tk()
    text1 = StringVar()
    label = Label( top, textvariable=text1)

    text1.set("welcome to itay's flying squirrel \n\n")
    label.pack()

    text2 = StringVar()
    labe2 = Label( top, textvariable=text2)

    text2.set("plese log in")
    labe2.pack()

    text4 = StringVar()
    global E1
    E1 = Entry(top, bd =5,textvariable= text4)

    E1.pack(side = RIGHT)

    text3 = StringVar()
    labe3 = Label(top, textvariable=text3 )
    text3.set("\n\nenter your name\n\n")
    labe3.pack( side = LEFT)

    B = Button(top, text ="sing in", command = hi)

    B.pack(side = BOTTOM)

    top.mainloop()
    return config.name


