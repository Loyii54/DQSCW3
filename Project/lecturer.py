from tkinter import *
from data import *
from createTest import createTest

class lecturer(Frame):

    def __init__(self, master):
        self.master = master
        Frame.__init__(self,master)
        self.grid()
        self.lecturerMain()

    def lecturerMain(self):
        varUser = StringVar()
        varUser.set("Welcome " + Users().getCurrentUser())
        Label(self, textvariable=varUser).grid(row=0, column=0, padx=5, pady=5)

        Label(self, text="Create test").grid(row=1, column=0, padx=5, pady=5)
        Button(self, text="Create", command=self.createTest).grid(row=1, column=1,padx=5, pady=5)

        Button(self, text="Logout", command=self.quitLecturer).grid(row=2, column=0, padx=5, pady=5)

    def quitLecturer(self):
        self.master.destroy()

    def createTest(self):
        frame2 = Toplevel(self.master)
        frame2.state('zoomed')
        frame2.title(Users().getCurrentUser())
        createTest(frame2)
