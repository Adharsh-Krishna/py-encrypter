from Tkinter import *
from src.constants import *
from src.services import *


class StartPage(Frame):
    email = None
    password = None
    data_service = DataService()

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__init_title_frame()
        self.__init_login_frame()
        footer_frame = self.__init_footer_frame()

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
        footer_frame.pack_propagate(False)
        footer_frame.pack(fill=X, side='bottom')
        return footer_frame

    def __login(self, email, password):
        self.email = email.get()
        self.password = password.get()
        print "logging in ...", self.email, self.password
        print self.data_service.check_credentials(self.email, self.password)


# class PageOne(Frame):
#
#     def __init__(self, parent, controller):
#         Frame.__init__(self, parent)
#         label = Label(self, text='Page One!!!', font=FONT_VERDANA)
#         label.pack(pady=10,padx=10)
#
#         button1 = Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
#         button1.pack()
#
#         button2 = Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
#         button2.pack()


