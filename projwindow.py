import os.path
from tkinter import *
from tkinter import filedialog

import newproject
import webbrowser


# noinspection PyPep8Naming
class Proj:
    # noinspection SpellCheckingInspection
    def __init__(self):
        self.tk = Tk()
        self.tk.withdraw()
        self.looping = True
        self.console = Text(self.tk, width=80, height=10)
        self.new = Button(self.tk, text="New", command=self.newProj)
        self.open = Button(self.tk, text="Open", command=self.openFile)
        # noinspection SpellCheckingInspection
        self.gitbutton = Button(self.tk, text="Check for updates", command=self.git)
        self.quitbutton = Button(self.tk, text="Exit", command=self.stop)
        self.console.grid(row=0, column=0, rowspan=4)
        self.new.grid(row=0, column=1, ipadx=20, sticky=NSEW)
        self.open.grid(row=1, column=1, ipadx=20, sticky=NSEW)
        self.gitbutton.grid(row=2, column=1, ipadx=20, sticky=NSEW)
        self.quitbutton.grid(row=3, column=1, ipadx=20, sticky=NSEW)
        self.console.insert(END,"Welcome to DoodleBoard. Current version: ")
        with open('version.dll','r+') as f:
            self.console.insert(END,f.read()+"\n")

    def newProj(self):
        self.console.insert(END,"Creating new project...\n")
        newproject.new()

    def openFile(self):
        self.console.insert(END,"Opening project...\n")
        proj=filedialog.askdirectory()
        proj+="/"
        self.console.insert(END,proj+"\n")
        if os.path.isfile(proj+"project.dlp"):
            self.console.insert(END,proj+"project.dlp")
        else:
            self.console.insert(END,"Failed to load. no 'project.dlp' file.\n")

    def git(self):
        self.console.insert(END,"Opened Github. read the latiest version and compare it with your version.\n")
        webbrowser.open("https://github.com/NathanNuckels/DoodleBoard/blob/master/README.md", new=1)

    def stop(self):
        self.looping = False

    def show(self):
        self.tk.deiconify()

    def delete(self):
        self.tk.destroy()

    def loop(self):
        self.tk.update()
