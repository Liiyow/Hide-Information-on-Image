from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
from stegano import lsb
red=open("")
fil=open("fiiri.py","a")


def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),
        title="select Image file",filetypes=(("PNG file","*.png"),
        ("JPG File","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img
    aqri()
def aqri():
    try:
        clear_message=lsb.reveal(filename)
        fil.write(clear_message)
    except:
        print()
def hide():
    global secret
    n=str(filename)
    messsage=text1.get(1.0,END)
    secret=lsb.hide(str(filename),messsage)
def show():
    try:
        clear_message=lsb.reveal(filename)
        text1.delete(1.0,END)
        text1.insert(END,clear_message)
        fil.write(clear_message)
    except:
        print()
def save():
    secret.save("hiden.png")

root=Tk()
root.title("hide Text information On Image")
root.geometry("700x500+250+180")
root.resizable(False,False)
root.configure(bg="#2f4155")
icon=PhotoImage(file="logo.jpg")
root.iconphoto(False,icon)
log=PhotoImage(file="logo.png")
Label(root,image=log,bg="#2f4155").place(x=10,y=0)
Label(root,text="CYBER SCIENCE",bg="#2d4155",fg="white",font=("arial",25,"bold")).place(x=100,y=20)
f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)
lbl=Label(f,bg="black")
lbl.place(x=40,y=10)
f2=Frame(root,bd=3,bg="white",width=340,height=280,relief=GROOVE)
f2.place(x=350,y=80)
text1=Text(f2,font="Robote 20",bg="white",fg="black",relief=GROOVE)
text1. place(x=0,y=0,width=320,height=295)
scrollbar1=Scrollbar(f2)
scrollbar1.place(x=320,y=300)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)
f3=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f3.place(x=10,y=370)

Button(f3,text="Open Image",width=10,height=2,font=("arial",12,"bold"),command=showimage).place(x=20,y=30)
Button(f3,text="Save Image",width=10,height=2,font=("arial",12,"bold"),command=save).place(x=180,y=30)
Label(f3,text="Picture,Image,Photo",bg="#2f4155",fg="yellow").place(x=20,y=5)


f4=Frame(root,bd=3,bg="#2f4155",width=330,height=100,relief=GROOVE)
f4.place(x=360,y=370)

Button(f4,text="hide data",width=10,height=2,font=("arial",12,"bold"),command=hide).place(x=20,y=30)
Button(f4,text="show data",width=10,height=2,font=("arial",12,"bold"),command=show).place(x=180,y=30)
Label(f4,text="Picture,Image,Photo",bg="#2f4155",fg="yellow").place(x=20,y=5)


root.mainloop()
