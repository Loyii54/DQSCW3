from tkinter import *
from data import *
from takeTest import takeTest

class student(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.studentMain()

    def studentMain(self):
        varUser = StringVar()
        varUser.set("Welcome " + Users().getCurrentUser())
        Label(self, textvariable=varUser).grid(row=0, column=0, padx=5, pady=5)

        buttonList = []
        rowCounter=1
        for i in range(Tests().getNumberOfTests()):
            tests = Tests().getTest()
            varTestLabelText = StringVar()
            varTestLabelText.set(tests[i][1])
            TestLabel = Label(self, textvariable=varTestLabelText)
            TestLabel.grid(row=rowCounter, column=0, padx=5, pady=5)
            buttonList.append(Button(self, text='Take test', command=lambda i=i: self.takeTest(i)))
            buttonList[i].grid(row=rowCounter, column=1, padx=5, pady=5)

        Button(self, text="Logout", command=self.quitStudent).grid(row=rowCounter+1, column=0, padx=5, pady=5)

    def takeTest(self, testNumber):
        tests = Tests().getTest()
        currentTest = tests[testNumber]
        testNumber, testName, testContent, testType = currentTest
        Tests(testNumber=testNumber, testName=testName, testContent=testContent, testType=testType).currentTest()

        frame2 = Toplevel(self.master)
        frame2.state('zoomed')
        frame2.title(Users().getCurrentUser())
        takeTest(frame2)

    def quitStudent(self):
        self.master.destroy()
