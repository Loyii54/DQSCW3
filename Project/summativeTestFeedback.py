from tkinter import *
from tkinter import messagebox
from data import *

class summativeTestFeedback(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.summativeTestFeedbackMain()

    def summativeTestFeedbackMain(self):
        user = Users().getCurrentUser()
        testNumber = int(Tests().getCurrentTest()[0])
        testRetrieve = Test_record(user=user, testNumber=testNumber).getTestScore()
        #Retrieve = [user, testNumber, trial, response, score, totalQuestions]
        correctAnswers = testRetrieve[4]
        totalQuestions = testRetrieve[5]
        var_correctAnswers = StringVar()
        var_correctAnswers.set("You scored: " + str(correctAnswers) + '/' + str(totalQuestions))
        Label(self, textvariable=var_correctAnswers).grid(row=0, column=0, padx=5, pady=5)

        Button(self, text="Back", command=self.back).grid(row=1, column=0, padx=5, pady=5)

    def back(self):
        self.master.destroy()
