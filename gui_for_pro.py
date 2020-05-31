# -*- coding: utf-8 -*-
from Tkinter import *
import config

def hi():
    config.name= E1.get()
    E1.delete (0,1000)
    config.sip= E2.get()
    E2.delete (0,1000)
    top.destroy()

def reg():
    global top
    top = Tk()
    text1 = StringVar()
    label = Label( top, textvariable=text1)

    text1.set("welcome to itay's flying squirrel")
    label.grid(row=0,column=3)

    text2 = StringVar()
    labe2 = Label( top, textvariable=text2)

    text2.set("plese log in")
    labe2.grid(row=1,column=3)

    text4 = StringVar()
    global E1
    E1 = Entry(top, bd =5,textvariable= text4)

    E1.grid(row=6,column=4)

    text3 = StringVar()
    labe3 = Label(top, textvariable=text3 )
    text3.set("enter your name")
    labe3.grid(row=6,column=2)



    text5 = StringVar()
    global E2
    E2 = Entry(top, bd =5,textvariable= text5)

    E2.grid(row=8,column=4)

    text6 = StringVar()
    labe6 = Label(top, textvariable=text6 )
    text6.set("enter your server ip")
    labe6.grid(row=8,column=2)

    B = Button(top, text ="sing in", command = hi)

    B.grid(row=11,column=3)

    top.mainloop()
    return config.name

def main():
    """
    Add Documentation here
    """
    reg()

if __name__ == '__main__':
    main()
