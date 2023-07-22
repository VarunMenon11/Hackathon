from os import *
import os
from telnetlib import STATUS

from tkinter import *
from turtle import left

import time
 


root =Tk()

root.title("Elemental Fun")
winWidth = root.winfo_reqwidth()
winwHeight = root.winfo_reqheight()
posRight = int(root.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(root.winfo_screenheight() / 2 - winwHeight / 2)
root.geometry("+{}+{}".format(posRight, posDown))
#root.geometry("2048x1070")


bg = PhotoImage(file="C:/Users/Varun/Documents/College Stuff/Hackthon/17014/Picture/Background14.png")
my_label = Label(master = root, image=bg)
my_label.place(x=0, y=0)



def aClick():
    mylabel =os.startfile(r"C:/Users/Varun/Documents/17014/Meter Bridge/final/meter bridge.blend.exe")
    
    
def bClick():
    mylabel =os.startfile(r"C:\Users\Varun\Document/17014/Game Folder/Coil/game/abc12.exe")
    

def cClick():
    mylabel =os.startfile(r"C:\Users\Varun\Document/17014/Game Folder/Virus/POOOOOJAAAAA/pujwa virus.blend.exe")


def dClick():
    mylabel =os.startfile(r"C:\Users\Varun\Document/17014/Game Folder/Resultant/sample/sample/asdfasdfasdfasdfasdf.blend.exe")

def eClick():
    mylabel =os.startfile(r"")

def fClick():
    mylabel =os.startfile(r"")

def gClick():
    mylabel =os.startfile(r"")
    
def hClick():
    mylabel =os.startfile(r"")

def oClick():
    myButtona = Button(root, text="Metre Bridge",bd=0 ,bg='#F6CADC', fg='black',font=('Arial',20), command=aClick)
    myButtona.place(x= 290, y=300)

    myButtonb = Button(root, text="Coil",bg='#F6CADC',bd=0, fg='black',font=('Arial',20) , command=bClick)
    myButtonb.place(x=665, y=450)
            
    myButtonc = Button(root, text="Virus",bd=0,bg='#F6CADC', fg='black',font=('Arial',20), command=cClick)
    myButtonc.place(x=1010, y=570)
            
    myButtond = Button(root, text="Resultant",bd=0 ,bg='#F6CADC', fg='black',font=('Arial',20), command=dClick)
    myButtond.place(x=1150, y=680)

    myButtone = Button(root, text="Experiment 1",bd=0,bg='#C4DFFB', fg='black',font=('Arial',20), command=eClick)
    myButtone.place(x=540, y=240)

    myButtonf = Button(root, text="Experiment2",bd=0,bg='#C4DFFB', fg='black',font=('Arial',20), command=fClick)
    myButtonf.place(x=840, y=390)

    myButtong = Button(root, text="Experiment3",bd=0,bg='#C4DFFB', fg='black',font=('Arial',20), command=gClick)
    myButtong.place(x=1070, y=510)

    myButtonh = Button(root, text="Experiment4",bd=0,bg='#C4DFFB', fg='black',font=('Arial',20), command=hClick)
    myButtonh.place(x=1270, y=620)
        

myButton = Button(root, text="Start" ,bd=0,bg='#F57F4F', fg='black',font=('Arial',35)  , command=oClick)
myButton.place(x=50, y=110)

Exit = Button(root, text="Exit",bd=0, bg="#C4DFFB" ,fg='Black',font=('Arial', 35), command= exit)
Exit.place(x=1700, y=800)

Labl1 = Label(text='Elemental Fun', font=('Broadway',60), bg="#C4DFFB", bd=0)
Labl1.place(x=1100, y= 110)

Labl2 = Label(text="Learning Through Games", font=('Broadway', 20),bg="#C4DFFB", bd=0, width=40)
Labl2.place(x=1080, y =200)

Labl3 = Label(text="Made by Silient Finishers",font=('Broadway', 20),bg="#C4DFFB", bd=0, width=40)
Labl3.place(x=1080, y =250)

labl4 = Label(text="WASD to move",font=('Broadway', 20),bg="#C4DFFB", bd=0, width=40)
labl4.place(x= 1380, y = 500)

labl5 = Label(text="Mouse to look around",font=('Broadway', 20),bg="#C4DFFB", bd=0, width=40)
labl5.place(x= 1380, y = 450)

labl6 = Label(text="Left click to interact",font=('Broadway', 20),bg="#C4DFFB", bd=0, width=40)
labl6.place(x= 1380, y = 550)

Stats = Button(text="Stats",font=('Broadway', 20),bg="#C4DFFB", bd=1, width=10)
Stats.place(x=600, y=110)




root.mainloop()
