from Tkinter import *
FONT_VERDANA = ('Verdana', 18)


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        # heading_frame = Frame(self, bg='green', width=X, height='200')
        # heading_frame.pack()
        label = Label(self, text='Start Page', font=FONT_VERDANA, bg='black', fg='white')
        label.pack(fill=X)
        #
        # button = Button(self, text='Visit Page 1', command=lambda: controller.show_frame(PageOne))
        # button.pack()
        #
        # button2 = Button(self, text='Visit Page 2', command=lambda: controller.show_frame(PageTwo))
        # button2.pack()


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


