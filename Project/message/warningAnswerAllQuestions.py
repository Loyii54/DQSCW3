from tkinter import *
from data import *

class warningAnswerAllQuestions(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.warningAnswerAllQuestionsMain()

    def warningAnswerAllQuestionsMain(self):
        Label(self, text="You need to answer all questions").grid(row=0, column=0, padx=5, pady=5)
        Button(self, text="Ok", command=self.quit).grid(row=1, column=0, padx=5, pady=5)

    def quit(self):
        self.master.destroy()
