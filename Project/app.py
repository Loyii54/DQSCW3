from tkinter import *
from tkinter import messagebox
from data import *
from student import student

class appLogin(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.login()

    def login(self):
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)
        self.var_username = StringVar()
        self.var_username.set('student')
        self.var_password = StringVar()
        self.var_password.set('password')

        label_username = Label(self, text='Username: ')
        label_password = Label(self, text='Password: ')
        label_username.grid(row=0, column=0, padx=5, pady=5)
        label_password.grid(row=1, column=0, padx=5, pady=5)

        enter_username = Entry(self, textvariable=self.var_username)
        enter_password = Entry(self, textvariable=self.var_password, show='*')
        enter_username.grid(row=0, column=1, padx=5, pady=5)
        enter_password.grid(row=1, column=1, padx=5, pady=5)

        self.button_login = Button(self, text="Login", command=self.login_command)
        self.button_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def login_command(self):
        if Users(username=self.var_username.get(), password=self.var_password.get()).checkData() == (1, 's'):
            Users(username=self.var_username.get(), password=self.var_password.get()).currentUser()
            frame1 = Toplevel(root)
            frame1.state('zoomed')
            frame1.title(Users().getCurrentUser())
            student(frame1)
            self.wait_window(frame1)

        elif Users(username=self.var_username.get(), password=self.var_password.get()).checkData() == (1, 't'):
            Users(username=self.var_username.get(), password=self.var_password.get()).currentUser()
            frame1 = Toplevel(root)
            frame1.state('zoomed')
            frame1.title(Users().getCurrentUser())
            lecturer(frame1)
            self.wait_window(frame1)
        else:
            messagebox.showwarning('Login failed', 'Incorrect username or password')


root = Tk()
root.title("Login")
root.state('zoomed')
app = appLogin(root)
root.mainloop()
