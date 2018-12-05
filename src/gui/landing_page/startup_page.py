from Tkinter import *
from src.constants import *
from .validator import *
import tkMessageBox


class StartPage(Frame):
    user_name = None
    password = None
    router = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.router = controller
        self.__init_title_frame()
        self.__init_login_frame()
        self.__init_footer_frame()

    def __init_title_frame(self):
        heading_frame = Frame(self, bg='grey', width=400, height=35)
        heading_frame.pack_propagate(False)
        heading_frame.pack()
        label = Label(heading_frame, text=APP_NAME, font=FONT_VERDANA, bg='black', fg='white')
        label.pack(fill=X)

    def __init_login_frame(self):
        login_frame = Frame(self, width=400, height=50)
        login_frame.pack_propagate(False)
        login_frame.pack()
        Label(login_frame, text="Username :", font=FONT_VERDANA).grid(row=0, sticky=W, padx=20, pady=10)
        Label(login_frame, text="Password :", font=FONT_VERDANA).grid(row=1, sticky=W, padx=20, pady=10)
        user_name_entry = Entry(login_frame)
        user_name_entry.grid(row=0, column=1)
        password_entry = Entry(login_frame, show='*')
        password_entry.grid(row=1, column=1)
        login_button = Button(login_frame, text="LOGIN", fg='red', width=5, bg='black',
                              command=lambda: self.__login(user_name_entry, password_entry))
        login_button.grid(row=2, column=1, padx=(120, 0))

    def __init_footer_frame(self):
        footer_frame = Frame(self, bg='black', width=600, height=100, borderwidth=1)
        footer_frame.pack(fill=X, side='bottom')
        forgot_password_label = Label(footer_frame, text="Forgot Password ?", font=FONT_VERDANA, bg="black", fg="white")
        forgot_password_label.grid(row=0, column=0, sticky=E, padx=50, pady=10)

        register_label = Label(footer_frame, text="Register here", font=FONT_VERDANA, bg="black", fg="white")
        register_label.bind("<Button-1>", lambda x: self.go_to_register_page())
        register_label.grid(row=0, column=1, sticky=E, padx=50, pady=10)
        footer_frame.pack_propagate(False)
        return footer_frame

    def go_to_register_page(self):
        self.router.show_frame('RegisterPage')

    def __login(self, user_name, password):
        self.user_name = user_name.get()
        self.password = password.get()
        print "trying to log in ...", self.user_name, self.password
        credentials_correct = check_credentials(self.user_name, self.password)
        if credentials_correct is True:
            self.router.show_frame('HomePage')
        else:
            StartPage.show_popup_incorrect_credentials_window()

    @staticmethod
    def show_popup_incorrect_credentials_window():
        tkMessageBox.showwarning('Incorrect Credentials', 'User Name or Password incorrect.')

