from Tkinter import *
FONT_VERDANA = ('Verdana', 18)
APP_NAME = 'Py Encrypter'


class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        heading_frame = Frame(self, bg='grey', width=600, height=500)
        heading_frame.pack_propagate(False)
        heading_frame.pack()
        label = Label(heading_frame, text=APP_NAME, font=FONT_VERDANA, bg='black', fg='white')
        label.pack(fill=X)

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


