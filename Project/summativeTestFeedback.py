from tkinter import *
from tkinter import messagebox
from data import *

class summativeTestFeedback(Frame):

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
        user = Users().getCurrentUser()
        testNumber = int(Tests().getCurrentTest()[0])
        testRetrieve = Test_record(user=user, testNumber=testNumber).getTestScore()
        # FORMAT -- Retrieve = [user, testNumber, trial, response, score, totalQuestions]
        correctAnswers = testRetrieve[4]
        totalQuestions = testRetrieve[5]
        var_correctAnswers = StringVar()
        var_correctAnswers.set("You scored: " + str(correctAnswers) + '/' + str(totalQuestions))

        Label(self.frameInCanvas, textvariable=var_correctAnswers).grid(row=0, column=0, padx=5, pady=5)

        Button(self.frameInCanvas, text="Back", command=self.back).grid(row=1, column=0, padx=5, pady=5)

    def back(self):
        """
            Empty currentTest() and switch frame to Student
        """
        Tests().currentTest()
        self.master.switch_frame('Student')

    def onFrameConfigure(self, event):
        '''
            Reset the scroll region to encompass the inner frame
        '''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
