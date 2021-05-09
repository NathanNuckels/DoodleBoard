from tkinter import *
from tkinter.messagebox import showinfo
import time

objects=[]
def saveFile():
    global objects
    print(objects)
    if objects[1][2].get()=="":
        showinfo("No filename","You must enter a directory. Although there is a project file, this program does other things. Create a folder in the same location as this file and enter its name.")
    elif objects[1][2].get().endswith("/"):
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
        showinfo("All clear","looks good to me.")

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

new()