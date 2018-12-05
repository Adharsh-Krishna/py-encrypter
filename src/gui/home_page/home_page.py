from Tkinter import *


class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.router = controller
