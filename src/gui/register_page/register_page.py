from Tkinter import *
from src.constants import *
from .validator import *
import tkMessageBox


class RegisterPage(Frame):

    user_name = None
    password = None
    re_entered_password = None
    info_text = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.__init_title_frame()
        self.__init__register_frame()

    def __init_title_frame(self):
        heading_frame = Frame(self, bg='grey', width=600, height=35)
        heading_frame.pack_propagate(False)
        heading_frame.pack()
        label = Label(heading_frame, text=APP_NAME, font=FONT_VERDANA, bg='black', fg='white')
        label.pack(fill=X)

    def __init__register_frame(self):
        register_frame = Frame(self, bg='white', width=400, height=150)
        register_frame.pack_propagate(False)
        register_frame.pack()
        Label(register_frame, text='Username', font=FONT_VERDANA).grid(row=0, column=0, sticky=W, pady=5)
        Label(register_frame, text='Password', font=FONT_VERDANA).grid(row=1, column=0, sticky=W, pady=5)
        Label(register_frame, text='Re-enter Password', font=FONT_VERDANA).grid(row=2, column=0, sticky=W, pady=5)
        user_name_entry = Entry(register_frame)
        user_name_entry.grid(row=0, column=1)
        password_entry = Entry(register_frame, show='*')
        password_entry.grid(row=1, column=1)
        re_password_entry = Entry(register_frame, show='*')
        re_password_entry.grid(row=2, column=1)
        submit_button = Button(register_frame, text='REGISTER', fg='red', width=5, height=2, bg='black',
                               command=lambda: self.__register(
                                   user_name_entry,
                                   password_entry,
                                   re_password_entry))
        submit_button.grid(row=3, column=1, padx=(100, 0))

    def __register(self, user_name, password, re_entered_password):
        self.user_name = user_name.get()
        self.password = password.get()
        self.re_entered_password = re_entered_password.get()
        errors = check_registration_input(self.user_name, self.password, self.re_entered_password)
        if len(errors) > 0:
            RegisterPage.show_popup_error_window(errors)
        else:
            new_user_credential = DataService.create_user_credential(self.user_name, self.password)
            if new_user_credential is not None:
                RegisterPage.show_popup_success_window(self.user_name)
            else:
                RegisterPage.show_popup_user_creation_failed_window()

    @staticmethod
    def show_popup_error_window(errors):
        tkMessageBox.showwarning('Error in registration', '\n'.join(errors))

    @staticmethod
    def show_popup_success_window(user_name):
        tkMessageBox.showinfo('Congrats !!', 'Registration successful for User Name : ' + user_name)

    @staticmethod
    def show_popup_user_creation_failed_window():
        tkMessageBox.showwarning('Error in registration', 'User could not be created. Please Try again.')

        # button1 = Button(self, text='Back to Home', command=lambda: controller.show_frame(StartPage))
        # button1.pack()
        #
        # button2 = Button(self, text='Page Two', command=lambda: controller.show_frame(PageTwo))
        # button2.pack()
