from tkinter import *
from tkinter import messagebox
from data import *
from summativeTestFeedback import summativeTestFeedback

class takeTest(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.takeTestMain()

    def takeTestMain(self):
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

            var_questionVariable = IntVar()
            self.var_questionsDict[Question] = var_questionVariable
            Label(self, text = Question).grid(row=rowCounter, column=0, padx=5, pady=5)
            Radiobutton(self, text=Answer1, variable=self.var_questionsDict[Question], value=5-REALAnswer).grid(row=rowCounter+1, column=0, padx=5, pady=5)
            Radiobutton(self, text=Answer2, variable=self.var_questionsDict[Question], value=6-REALAnswer).grid(row=rowCounter+1, column=1, padx=5, pady=5)
            Radiobutton(self, text=Answer3, variable=self.var_questionsDict[Question], value=7-REALAnswer).grid(row=rowCounter+1, column=2, padx=5, pady=5)
            Radiobutton(self, text=Answer4, variable=self.var_questionsDict[Question], value=8-REALAnswer).grid(row=rowCounter+1, column=3, padx=5, pady=5)
            rowCounter+=2

        Button(self, text='Submit', command=self.testSubmit).grid(row=rowCounter, column=1, columnspan=2, padx=5, pady=5)


    def testSubmit(self):
        responseList =[]
        for Question, Response in self.var_questionsDict.items():
            responseList.append(Response.get())
        if 0 in responseList:
            messagebox.showwarning("Warning", "You need to answer all questions")
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

                frame3 = Toplevel(self.master)
                frame3.state('zoomed')
                frame3.title(Users().getCurrentUser())
                summativeTestFeedback(frame3)
