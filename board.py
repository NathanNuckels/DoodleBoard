from tkinter import *

class Drawboard:
    def __init__(self,data,path):
        self.data=data
        self.path=path
        self.tk=Tk()
        #self.tk.withdraw()
        self.tk.title("Draw Board - "+self.path+"/project.dlp")
        self.open=True
        print(self.data)
        self.board=Canvas(self.tk,width=self.data['Width'],height=self.data['Height'])
        self.objects=[
            Label(self.tk,text="Brush Size:"),
            Entry(self.tk),
            Button(self.tk,text="Set Brush Size"),
            Label(self.tk,text="Hex Color:"),
            Entry(self.tk),
            Button(self.tk,text="Set Color")
        ]
    def run(self):
        self.board.grid(row=0,column=0,rowspan=99)

        for i in range(len(self.objects)):
            self.objects[i].grid(row=i,column=1,sticky=NSEW)
    def loop(self):
        self.tk.update()