from src.gui.landing_page import *
from Tkinter import *


class Application(Tk):

    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage,):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        f = self.frames[cont]
        f.tkraise()


if __name__ == '__main__':
    app = Application()
    app.mainloop()