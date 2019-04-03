from tkinter import *
from tkinter import messagebox
from data import *

class lecturer(Frame):

    def __init__(self, master):
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
        varUser = StringVar()
        varUser.set("Welcome " + Users().getCurrentUser())
        Label(self.frameInCanvas, textvariable=varUser).grid(row=0, column=0, padx=5, pady=5)

        Label(self.frameInCanvas, text="Create test").grid(row=1, column=0, padx=5, pady=5)
        Button(self.frameInCanvas, text="Create", command=self.createTest).grid(row=1, column=1,padx=5, pady=5)

        Label(self.frameInCanvas, text="Modify test").grid(row=2, column=0, padx=5, pady=5)
        Button(self.frameInCanvas, text="Modify", command=self.ModifyTest).grid(row=2, column=1, padx=5, pady=5)

        Label(self.frameInCanvas, text="View test").grid(row=3, column=0, padx=5, pady=5)
        Button(self.frameInCanvas, text="View", command=self.ViewTest).grid(row=3, column=1, padx=5, pady=5)

        Button(self.frameInCanvas, text="Logout", command=self.logout).grid(row=4, column=0, padx=5, pady=5)


    def logout(self):
        Users().currentUser()
        self.master.switch_frame('Login')

    def createTest(self):
        tests = shelve.open("Data/Tests.db")
        tests['questionList'] = []
        tests.sync()
        tests.close()
        self.master.switch_frame('createTest')

    def ModifyTest(self):
        self.master.switch_frame('modifyTest')

    def ViewTest(self):
        self.master.switch_frame('viewTest')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
