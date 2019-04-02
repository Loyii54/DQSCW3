from tkinter import *
from tkinter import messagebox
import datetime
from data import *

class student(Frame):

    def __init__(self, master):
        """Create a canvas in the Frame such that a scrollbar can be put into the window, then create a frame in the canvas for the widgets."""
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
        varUser = StringVar()
        varUser.set("Welcome " + Users().getCurrentUser())
        Label(self.frameInCanvas, textvariable=varUser).grid(row=0, column=0, padx=5, pady=5)
        Button(self.frameInCanvas, text="Refresh Page", command=self.refresh).grid(row=0, column=1, padx=5, pady=5)

        rowCounter=1
        self.buttonList = []
        self.viewTestButtonList = []
        if range(Tests().getNumberOfTests()) == range(0,0):
            Label(self.frameInCanvas, text="You have no Tests.").grid(row=rowCounter, column=0, padx=5, pady=5)

        else:
            for i in range(Tests().getNumberOfTests()):
                tests = Tests().getTest()
                testType = int(tests[i][3])
                deadline = tests[i][4]
                varTestLabelText = StringVar()
                if testType ==1:
                    varTestLabelText.set(tests[i][1] + " (Summative Test) (Deadline: " + str(deadline.strftime("%Y-%m-%d %H:%M")) + ')' )
                else:
                    varTestLabelText.set(tests[i][1] + " (Formative Test) (Deadline: " + str(deadline.strftime("%Y-%m-%d %H:%M")) + ')' )
                TestLabel = Label(self.frameInCanvas, textvariable=varTestLabelText)
                TestLabel.grid(row=rowCounter, column=0, padx=5, pady=5)
                if datetime.datetime.now() < deadline:
                    try:
                        Test_record(user=Users().getCurrentUser(), testNumber=i).getTrials()
                        self.buttonList.append(Button(self.frameInCanvas, text='Take test',state="disabled", command=lambda i=i: self.takeTest(i)))
                        self.buttonList[i].grid(row=rowCounter, column=1, padx=5, pady=5)

                    except:
                        self.buttonList.append(Button(self.frameInCanvas, text='Take test',command=lambda i=i: self.takeTest(i)))
                        self.buttonList[i].grid(row=rowCounter, column=1, padx=5, pady=5)

                else:
                    self.buttonList.append(Button(self.frameInCanvas, text='Past Deadline',state="disabled", command=lambda i=i: self.takeTest(i)))
                    self.buttonList[i].grid(row=rowCounter, column=1, padx=5, pady=5)
                    self.viewTestButtonList.append(Button(self.frameInCanvas, text='View Score', command=lambda i=i: self.viewScore(i)))
                    self.viewTestButtonList[i].grid(row=rowCounter, column=2, padx=5, pady=5)

                rowCounter += 1

        Button(self.frameInCanvas, text="Logout", command=self.logout).grid(row=rowCounter+1, column=0, padx=5, pady=5)

    def takeTest(self, testNumber):
        tests = Tests().getTest()
        testNumber, testName, testContent, testType, deadline = tests[testNumber]
        Tests(testNumber=testNumber, testName=testName, testContent=testContent, testType=testType, deadline=deadline).currentTest()
        if testType == 2:
            messagebox.showwarning('Not Implemented', 'This has not been implemented yet')
        else:
            self.master.switch_frame('takeTest')

    def viewScore(self, testNumber):
        tests = Tests().getTest()
        testNumber, testName, testContent, testType, deadline = tests[testNumber]
        Tests(testNumber=testNumber, testName=testName, testContent=testContent, testType=testType, deadline=deadline).currentTest()
        if testType == 2:
            messagebox.showwarning('Not Implemented', 'This has not been implemented yet')
        else:
            self.master.switch_frame('viewAnswerStudent')

    def refresh(self):
        self.master.switch_frame('Student')

    def logout(self):
        Users().currentUser()
        self.master.switch_frame('Login')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
