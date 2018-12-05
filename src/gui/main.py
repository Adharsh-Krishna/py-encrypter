from src.gui.landing_page import *
from src.gui.register_page import *
from src.gui.home_page import *
from Tkinter import *


class Application(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.container = self.__init__container()
        self.__init__frames()
        self.show_frame('StartPage')

    def __init__container(self):
        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

    def __init__frames(self):
        self.pages = {
            'StartPage': StartPage,
            'RegisterPage': RegisterPage,
            'HomePage': HomePage
        }
        for p in dict.keys(self.pages):
            page = self.pages[p](self.container, self)
            self.pages[p] = page
            page.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        f = self.pages[page_name]
        f.tkraise()


if __name__ == '__main__':
    app = Application()
    app.minsize(400, 200)
    app.maxsize(400, 200)
    app.mainloop()