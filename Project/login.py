from tkinter import *
from tkinter import messagebox
from data import *

class login(Frame):

    def __init__(self, master):
        """
            Create a canvas in the Frame such that a scrollbar can be put into the window, then create a frame in the canvas for the widgets.
        """
        Frame.__init__(self,master)

        self.canvas = Canvas(self, borderwidth=0)
        self.frameInCanvas = Frame(self.canvas)
        self.verticalScrollBar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.verticalScrollBar.set)

        self.verticalScrollBar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((5,5), window=self.frameInCanvas, anchor="nw",
                                  tags="self.frameInCanvas")

        self.frameInCanvas.bind("<Configure>", self.onFrameConfigure)

        self.main()

    def main(self):
        """
            Tkinter widgets to be put in the frame in the canvas.
        """
        self.var_username = StringVar()
        self.var_username.set('student')
        self.var_password = StringVar()
        self.var_password.set('password')

        label_username = Label(self.frameInCanvas, text='Username: ')
        label_password = Label(self.frameInCanvas, text='Password: ')
        label_username.grid(row=0, column=0, padx=5, pady=5)
        label_password.grid(row=1, column=0, padx=5, pady=5)

        enter_username = Entry(self.frameInCanvas, textvariable=self.var_username)
        enter_password = Entry(self.frameInCanvas, textvariable=self.var_password, show='*')
        enter_username.grid(row=0, column=1, padx=5, pady=5)
        enter_password.grid(row=1, column=1, padx=5, pady=5)

        self.button_login = Button(self.frameInCanvas, text="Login", command=self.login_command)
        self.button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def login_command(self):
        """
            Checks if username and password is valid and splits to student or lecturer frame depending on the input.
        """
        if Users(username=self.var_username.get(), password=self.var_password.get()).checkData() == (1, 's'):
            #If username and password is correct and user is a Student
            Users(username=self.var_username.get()).currentUser()
            self.master.switch_frame('Student')

        elif Users(username=self.var_username.get(), password=self.var_password.get()).checkData() == (1, 't'):
            #If username and password is correct and user is a Lecturer
            #NOT FINISHED
            Users(username=self.var_username.get()).currentUser()
            self.master.switch_frame('Lecturer')

        else:
            #If something is incorrect
            messagebox.showwarning('Login failed', 'Incorrect username or password')

    def onFrameConfigure(self, event):
        '''
            Reset the scroll region to encompass the inner frame.
        '''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
