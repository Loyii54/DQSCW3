from tkinter import *
from tkinter import messagebox
import datetime
from data import *


class takeTest(Frame):

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
        testNumber, testName, testContent, testType, deadline = Tests().getCurrentTest()

        if datetime.datetime.now() > deadline:
            messagebox.showwarning('Past Deadline', 'It is already past deadline!')
            self.master.switch_frame('Student')
        else:
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

                var_questionVariable = IntVar()
                self.var_questionsDict[Question] = var_questionVariable
                Label(self.frameInCanvas, text = Question).grid(row=rowCounter, column=0, columnspan=4, padx=5, pady=5, sticky="W")
                Radiobutton(self.frameInCanvas, text=Answer1, variable=self.var_questionsDict[Question], value=5-REALAnswer).grid(row=rowCounter+1, column=0, padx=5, pady=5)
                Radiobutton(self.frameInCanvas, text=Answer2, variable=self.var_questionsDict[Question], value=6-REALAnswer).grid(row=rowCounter+1, column=1, padx=5, pady=5)
                Radiobutton(self.frameInCanvas, text=Answer3, variable=self.var_questionsDict[Question], value=7-REALAnswer).grid(row=rowCounter+1, column=2, padx=5, pady=5)
                Radiobutton(self.frameInCanvas, text=Answer4, variable=self.var_questionsDict[Question], value=8-REALAnswer).grid(row=rowCounter+1, column=3, padx=5, pady=5)
                rowCounter+=2

            Button(self.frameInCanvas, text='Submit', command=self.testSubmit).grid(row=rowCounter, column=1, columnspan=2, padx=5, pady=5)



    def testSubmit(self):
        deadline = Tests().getCurrentTest()[4]
        if datetime.datetime.now() > deadline:
            Tests().currentTest()
            messagebox.showwarning('Past Deadline', 'It is already past deadline!')
            self.master.switch_frame('Student')
        else:
            responseList =[]
            for Question, Response in self.var_questionsDict.items():
                responseList.append(Response.get())

            if 0 in responseList:
                messagebox.showwarning('Warning', 'Please answer all questions')

            else:
                totalQuestions = 0
                correctAnswers = 0

                for attempt in responseList:
                    totalQuestions += 1
                    if attempt == 4:
                        correctAnswers += 1

                testNumber = int(Tests().getCurrentTest()[0])
                testType = int(Tests().getCurrentTest()[3])
                if testType == 1:
                    user = Users().getCurrentUser()
                    Test_record(user=user, testNumber=testNumber, response=responseList, score=correctAnswers, totalQuestions=totalQuestions).saveTestScore()

                    self.master.switch_frame('summativeTestFeedback')

                else:
                    messagebox.showwarning('Not Implemented', 'This has not been implemented yet')
                    # formativeTestFeedback.py is not implemented yet
                    # self.master.switch_frame('formativeTestFeedback')


    def quit(self):
        self.master.switch_frame('summativeTestFeedback')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
