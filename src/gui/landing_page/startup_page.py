from ..register_page.register_page import *
from Tkinter import *
from src.constants import *
from src.services import *


class StartPage(Frame):
    email = None
    password = None
    data_service = DataService()
    router = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.router = controller
        self.__init_title_frame()
        self.__init_login_frame()
        self.__init_footer_frame()

    def __init_title_frame(self):
        heading_frame = Frame(self, bg='grey', width=600, height=100)
        heading_frame.pack_propagate(False)
        heading_frame.pack()
        label = Label(heading_frame, text=APP_NAME, font=FONT_VERDANA, bg='black', fg='white')
        label.pack(fill=X)

    def __init_login_frame(self):
        login_frame = Frame(self, width=600, height=300)
        login_frame.pack_propagate(False)
        login_frame.pack()
        Label(login_frame, text="E-mail", font=FONT_VERDANA).grid(row=0, sticky=W, padx=20, pady=15)
        Label(login_frame, text="Password", font=FONT_VERDANA).grid(row=1, sticky=W, padx=20, pady=15)
        email_entry = Entry(login_frame)
        email_entry.grid(row=0, column=1)
        password_entry = Entry(login_frame, show='*')
        password_entry.grid(row=1, column=1)
        login_button = Button(login_frame, text="LOGIN", fg='red', width=10, height=2, bg='black',
                              command=lambda: self.__login(email_entry, password_entry))
        login_button.grid(row=3, column=1)

    def __init_footer_frame(self):
        footer_frame = Frame(self, bg='grey', width=600, height=100)
        footer_frame.pack(fill=X, side='bottom')
        f = Label(footer_frame, text="Forgot Password ?", font=FONT_VERDANA)
        f.bind("<Button-1>", lambda x: self.go_to_register_page())
        f.grid(row=0, column=0, sticky=E, padx=20)

        r = Label(footer_frame, text="Register here", font=FONT_VERDANA)
        r.grid(row=0, column=1, sticky=E, padx=20)
        footer_frame.pack_propagate(False)
        return footer_frame

    def go_to_register_page(self):
        self.router.show_frame('RegisterPage')

    def __login(self, email, password):
        self.email = email.get()
        self.password = password.get()
        print "logging in ...", self.email, self.password
        print self.data_service.check_credentials(self.email, self.password)



