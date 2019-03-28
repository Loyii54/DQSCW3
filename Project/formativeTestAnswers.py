from tkinter import *
from tkinter import messagebox
from data import *

class formativeTestAnswers(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.formativeTestAnswersMain()

    def formativeTestAnswersMain(self):
        testNumber, testName, testContent, testType = Tests().getCurrentTest()
        cleanTestContent = testContent.rstrip()
        testQuestions = cleanTestContent.split('\n')

        rowCounter = 1
        self.var_questionsDict = {}
        for question in testQuestions:
            questionList = question.split(', ')
            Question = questionList[0]
            Answer1 = questionList[1]
            Answer2 = questionList[2]
            Answer3 = questionList[3]
            Answer4 = questionList[4]
            REALAnswer = int(questionList[5])

