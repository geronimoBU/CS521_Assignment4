# Build GUI with tkinter (Tkinter in 2.X) with buttons that change color and grow

from tkinter import *
import random
import threading

class MyGui:
    """
    A GUI with buttons that change color and make the label grow
    """
    colors = ['blue', 'green', 'red', 'orange', 'brown', 'yellow']

    def __init__(self, parent, title ='popup', colors = None):
        self.parent = Frame(parent)
        parent.title(title)

        self.fontsize = 40
        self.random = random.SystemRandom()

        self.label = Label(parent, text= "SPAM",fg= "green", font= ("gothic {0}".format(self.fontsize)))
        self.label.pack()

        self.spam_button = Button(parent, text="Spam", highlightbackground= "green", command=lambda: self.reply())
        self.spam_button.pack(side= "left")
        self.grow_button = Button(parent, text="Grow", highlightbackground= "green", command=lambda: self.grow())
        self.grow_button.pack(side= "left")
        self.stop_button = Button(parent, text="Stop", highlightbackground= "green", command=lambda: self.stop())
        self.stop_button.pack(side= "left")

        if colors != None:
            self.colors = colors

    def reply(self):
        self.color = random.choice(self.colors)
        self.fontsize +=5
        self.label.config(font=('gothic {0}'.format(self.fontsize)), fg= self.color)
        self.spam_button.config(highlightbackground= self.color)

    def grow (self):
        self.growing = True
        self.grower()

    def grower(self):
        try:
            if self.growing == True and self.stop(True) != False:
                self.fontsize += 5
                self.label.config(font=('gothic {0}'.format(self.fontsize)))
                t = threading.Timer(0.1, self.grower)
                t.setDaemon = True
                t.start()
                print("Growing!")
            else:
                print("Growing Stops")
        except Exception as error:
            print(str(error))

    def stop(self, event=None):
        if event == True:
            self.growing = True
        else:
            self.growing = False
        return self.growing

class MySubGui(MyGui):
    colors = ['white', 'black']
    def __init__(self, parent, colors=None):
        super().__init__(parent, colors)

#USE TO TEST
MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()
