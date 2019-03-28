from tkinter import *
from tkinter import messagebox
from data import *
from formativeTestAnswers import formativeTestAnswers

class formativeTestFeedback(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.formativeTestFeedbackMain()

    def formativeTestFeedbackMain(self):
        user = Users().getCurrentUser()
        testNumber = int(Tests().getCurrentTest()[0])
        getTrials = Test_record(user=user, testNumber=testNumber).getTrials()
        testRetrieve = Test_record(user=user, testNumber=testNumber, trial=getTrials[-1]).getTestScore()
        #testRetrieve = [user, testNumber, trial, response, score, totalQuestions]
        correctAnswers = testRetrieve[4]
        totalQuestions = testRetrieve[5]

        var_correctAnswers = StringVar()
        var_correctAnswers.set("You scored: " + str(correctAnswers) + '/' + str(totalQuestions))
        Label(self, textvariable=var_correctAnswers).grid(row=0, column=0, padx=5, pady=5)

        if getTrials[-1] < 2:
            var_trialsLeft = StringVar()
            var_trialsLeft.set("You have " + str(2 - getTrials[-1]) + " trys(s) left.")
            Label(self, textvariable=var_trialsLeft).grid(row=1, column=0, padx=5, pady=5)
            Button(self, text="Retry", command=self.retry).grid(row=2, column=0, padx=5, pady=5)
            Button(self, text="Back", command=self.back).grid(row=2, column=1, padx=5, pady=5)
        else:
            Button(self, text="Back", command=self.back).grid(row=1, column=1, padx=5, pady=5)

    def retry(self):
        frame3 = Toplevel(self.master)
        frame3.state('zoomed')
        frame3.title(Users().getCurrentUser())
        formativeTestAnswers(frame3)
        self.wait_window(frame3)

    def back(self):
        self.master.master.destroy()
