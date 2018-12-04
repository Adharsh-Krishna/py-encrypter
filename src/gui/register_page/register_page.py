from Tkinter import *
from src.constants import *


class RegisterPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__init_title_frame()

    def __init_title_frame(self):
        heading_frame = Frame(self, bg='grey', width=600, height=100)
        heading_frame.pack_propagate(False)
        heading_frame.pack()
        label = Label(heading_frame, text=APP_NAME, font=FONT_VERDANA, bg='black', fg='white')
        label.pack(fill=X)

    def __init__register_frame(self):
        register_frame = Frame(self, bg='grey', width=600, height=100)
        register_frame.pack_propagate(False)
        register_frame.pack()

        # button1 = Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        # button1.pack()
        #
        # button2 = Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
        # button2.pack()
