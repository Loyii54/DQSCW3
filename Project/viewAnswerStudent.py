from tkinter import *
from tkinter import messagebox
from data import *


class viewAnswerStudent(Frame):

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
        #Initialise for looping over questions
        rowCounter = 1

        try:
            #If user has taken the test, display test score
            user = Users().getCurrentUser()
            testNumber = Tests().getCurrentTest()[0]
            trials = Test_record(user=user, testNumber=testNumber).getTrials()
            testRetrieve = Test_record(user=user, testNumber=testNumber, trial=trials[-1]).getTestScore()
            # FORMAT -- Retrieve = [user, testNumber, trial, response, score, totalQuestions]
            responseList = testRetrieve[3]
            correctAnswers = testRetrieve[4]
            totalQuestions = testRetrieve[5]
            var_correctAnswers = StringVar()
            var_correctAnswers.set("You scored: " + str(correctAnswers) + '/' + str(totalQuestions))
            Label(self.frameInCanvas, textvariable=var_correctAnswers).grid(row=0, column=0, padx=5, pady=5, sticky='W')

            #Obtain test information
            testNumber, testName, testContent, testType, deadline = Tests().getCurrentTest()
            cleanTestContent = testContent.rstrip()
            testQuestions = cleanTestContent.split('\n')

            #Initialise for looping over questions
            questionCounter = 0

            for question in testQuestions:
                #Loop over questions and create labels showing the questions and answers.
                #If user has taken the test, display test answers as well as response
                questionList = question.split(', ')
                Question = questionList[0]
                Answer1 = questionList[1]
                Answer2 = questionList[2]
                Answer3 = questionList[3]
                Answer4 = questionList[4]
                REALAnswer = int(questionList[5])
                REALAnswerKey = {1:[4,5,6,7], 2:[3,4,5,6], 3:[2,3,4,5], 4:[1,2,3,4]}
                answerList = ['A) '+Answer1,'B) '+Answer2, 'C) '+Answer3, 'D) '+Answer4]

                correctAnswer = StringVar()
                correctAnswer.set("Correct answer is: " + answerList[REALAnswer-1])
                youAnswered = StringVar()

                youAnswered.set("You answered: " + answerList[REALAnswerKey[REALAnswer].index(responseList[questionCounter])])

                Label(self.frameInCanvas, text=Question).grid(row=rowCounter, column=0, columnspan=4, padx=5, pady=5, sticky='W')
                Label(self.frameInCanvas, text='A) '+Answer1).grid(row=rowCounter+1, column=0, padx=5, pady=5)
                Label(self.frameInCanvas, text='B) '+Answer2).grid(row=rowCounter+1, column=1, padx=5, pady=5)
                Label(self.frameInCanvas, text='C) '+Answer3).grid(row=rowCounter+1, column=2, padx=5, pady=5)
                Label(self.frameInCanvas, text='D) '+Answer4).grid(row=rowCounter+1, column=3, padx=5, pady=5)
                Label(self.frameInCanvas, textvariable=correctAnswer).grid(row=rowCounter+2, column=0, columnspan=3, padx=5, pady=5, sticky='W')
                Label(self.frameInCanvas, textvariable=youAnswered).grid(row=rowCounter+2, column=4, padx=5, pady=5, sticky='W')

                rowCounter += 3
                questionCounter += 1

        except:
            #If user has not taken the test, display "You did not attempt this test."
            Label(self.frameInCanvas, text='You did not attempt this test.').grid(row=0, column=0, padx=5, pady=5, sticky='W')

            #Obtain test information
            testNumber, testName, testContent, testType, deadline = Tests().getCurrentTest()
            cleanTestContent = testContent.rstrip()
            testQuestions = cleanTestContent.split('\n')

            for question in testQuestions:
                #Loop over questions and create labels showing the questions and answers.
                #If user has not taken the test, display test answers ONLY
                questionList = question.split(', ')
                Question = questionList[0]
                Answer1 = questionList[1]
                Answer2 = questionList[2]
                Answer3 = questionList[3]
                Answer4 = questionList[4]
                REALAnswer = int(questionList[5])
                answerList = ['A) '+Answer1,' B)'+Answer2, 'C)'+Answer3, 'D)'+Answer4]
                correctAnswer = StringVar()
                correctAnswer.set("Correct answer is: " + answerList[REALAnswer-1])

                Label(self.frameInCanvas, text=Question).grid(row=rowCounter, column=0, columnspan=4, padx=5, pady=5, sticky='W')
                Label(self.frameInCanvas, text='A) '+Answer1).grid(row=rowCounter+1, column=0, padx=5, pady=5)
                Label(self.frameInCanvas, text='B) '+Answer2).grid(row=rowCounter+1, column=1, padx=5, pady=5)
                Label(self.frameInCanvas, text='C) '+Answer3).grid(row=rowCounter+1, column=2, padx=5, pady=5)
                Label(self.frameInCanvas, text='D) '+Answer4).grid(row=rowCounter+1, column=3, padx=5, pady=5)
                Label(self.frameInCanvas, textvariable=correctAnswer).grid(row=rowCounter+2, column=0, columnspan=3, padx=5, pady=5, sticky='W')

                rowCounter += 3

        finally:
            Button(self.frameInCanvas, text="Back", command=self.back).grid(row=rowCounter, column=0, padx=5, pady=5)

    def back(self):
        """
            Clear currentTest() and switch frame to student
        """
        Tests().currentTest()
        self.master.switch_frame('Student')

    def onFrameConfigure(self, event):
        '''
            Reset the scroll region to encompass the inner frame
        '''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
