from tkinter import *
from tkinter.messagebox import showinfo
import time
import sys
import os
tk=None
objects=[]
def saveFile():
    global objects
    global tk
    if objects[1][2].get()=="":
        showinfo("No filename","You must enter a directory. Although there is a project file, this program does other things. Create a folder in the same location as this file and enter its name.")
    elif not objects[1][2].get().endswith("/"):
        showinfo("Is it REALLY a folder?","Prove it by typeing a / at the end")
    elif objects[1][0].get()=="":
        showinfo("No Canvas width", "You must enter the canvas width. 1920 or 1280 are good")
    elif not objects[1][0].get().isnumeric():
        showinfo("NaN","The width must be a number")
    elif objects[1][1].get()=="":
        showinfo("No Canvas height", "You must enter a canvas height. 1080 or 720 work good")
    elif not objects[1][1].get().isnumeric():
        showinfo("NaN","The height must be a number")
    else:
        projFolder=objects[1][2].get()
        proj={
            'Width':objects[1][0].get(),
            'Height':objects[1][1].get()
        }
        filedata=""
        for key in proj:
            filedata+=key+"|"+proj[key]+"\n"
        if not os.path.isdir(projFolder):
            os.mkdir(projFolder)
        with open(projFolder+"Data.dll",'w+') as f:
            f.write(filedata)
        showinfo("Sucsess","Project created.")
        tk.destroy()

def new():
    global objects
    tk=Tk()
    title="Doodle Board"
    tk.title(title)
    fontdata=("Helvetica",12)
    objects=[
        [
            Label(tk,text="Width:",font=fontdata),
            Label(tk,text="Height:",font=fontdata),
            Label(tk,text="File Name:",font=fontdata)
        ],
        [
            Entry(tk),
            Entry(tk),
            Entry(tk)
        ],
        Button(tk, text="Save", command=saveFile, font=fontdata)
    ]
    objects[0][2].grid(row=0,column=0,padx=8,pady=8)
    objects[1][2].grid(row=0,column=1,ipady=4,ipadx=4,sticky=NSEW)
    objects[0][0].grid(row=1,column=0,padx=8,pady=8)
    objects[1][0].grid(row=1,column=1,ipady=4,ipadx=4,sticky=NSEW)
    objects[0][1].grid(row=2,column=0,padx=8,pady=8)
    objects[1][1].grid(row=2,column=1,ipady=4,ipadx=4,sticky=NSEW)

    objects[2].grid(row=99,column=0,columnspan=2,sticky=NSEW)

    while 1:
        tk.update()
        time.sleep(1/60)

#new()