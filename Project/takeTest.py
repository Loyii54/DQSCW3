from tkinter import *
from tkinter import messagebox
import datetime
from data import *


class takeTest(Frame):

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
        testNumber, testName, testContent, testType, deadline = Tests().getCurrentTest()

        if datetime.datetime.now() > deadline:
            #Check if past deadline, if so switch frame to Student
            Tests().currentTest()
            messagebox.showwarning('Past Deadline', 'It is already past deadline!')
            self.master.switch_frame('Student')
        else:
            #Get contents of test
            cleanTestContent = testContent.rstrip()
            testQuestions = cleanTestContent.split('\n')

            #Initialise for looping over questions
            rowCounter = 1
            self.var_questionsDict = {}

            for question in testQuestions:
                #Looping over questions and creating labels and radiobuttons for each question
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
                Radiobutton(self.frameInCanvas, text='A) '+Answer1, variable=self.var_questionsDict[Question], value=5-REALAnswer).grid(row=rowCounter+1, column=0, padx=5, pady=5)
                Radiobutton(self.frameInCanvas, text='B) '+Answer2, variable=self.var_questionsDict[Question], value=6-REALAnswer).grid(row=rowCounter+1, column=1, padx=5, pady=5)
                Radiobutton(self.frameInCanvas, text='C) '+Answer3, variable=self.var_questionsDict[Question], value=7-REALAnswer).grid(row=rowCounter+1, column=2, padx=5, pady=5)
                Radiobutton(self.frameInCanvas, text='D) '+Answer4, variable=self.var_questionsDict[Question], value=8-REALAnswer).grid(row=rowCounter+1, column=3, padx=5, pady=5)
                rowCounter += 2

            Button(self.frameInCanvas, text='Submit', command=self.testSubmit).grid(row=rowCounter, column=1, columnspan=2, padx=5, pady=5)



    def testSubmit(self):
        """
            Checks if valid, if so save test results and switch fame to summativeTestFeedback / formativeTestFeedback(NOT IMPLEMENTED)
        """
        deadline = Tests().getCurrentTest()[4]

        if datetime.datetime.now() > deadline:
            #Check if past deadline, if so switch frame to Student
            Tests().currentTest()
            messagebox.showwarning('Past Deadline', 'It is already past deadline!')
            self.master.switch_frame('Student')

        else:
            responseList =[]
            for Question, Response in self.var_questionsDict.items():
                responseList.append(Response.get())

            if 0 in responseList:
                #Checks if all questions are answered
                messagebox.showwarning('Warning', 'Please answer all questions')

            else:
                #Loops over each question response and adds up totalQuestion and correctAnswers, then save the test response using Test_record.saveTestScore()
                totalQuestions = 0
                correctAnswers = 0

                for attempt in responseList:
                    totalQuestions += 1
                    if attempt == 4:
                        correctAnswers += 1

                testNumber = int(Tests().getCurrentTest()[0])
                testType = int(Tests().getCurrentTest()[3])
                if testType == 1:
                    #Switch frame to summativeTestFeedback if test is a summative test
                    user = Users().getCurrentUser()
                    Test_record(user=user, testNumber=testNumber, response=responseList, score=correctAnswers, totalQuestions=totalQuestions).saveTestScore()

                    self.master.switch_frame('summativeTestFeedback')

                else:
                    user=Users().getCurrentUser()
                    try:
                        trial = Test_record(user=user, testNumber=testNumber).getTrials()[-1] + 1
                        Test_record(user=user, testNumber=testNumber, trial=trial, response=responseList, score=correctAnswers, totalQuestions=totalQuestions).saveTestScore()
                    except:
                        Test_record(user=user, testNumber=testNumber, response=responseList, score=correctAnswers, totalQuestions=totalQuestions).saveTestScore()

                    self.master.switch_frame('formativeTestFeedback')

    def onFrameConfigure(self, event):
        '''
            Reset the scroll region to encompass the inner frame
        '''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
