from tkinter import *
from data import *

class modifyTest(Frame):

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
        rowCounter = 0
        self.buttonList = []
        for i in range(Tests().getNumberOfTests()):
            tests = Tests().getTest()
            varTestLabelText = StringVar()
            varTestLabelText.set(tests[i][1])

            TestLabel = Label(self.frameInCanvas, textvariable=varTestLabelText)
            TestLabel.grid(row=rowCounter, column=0, padx=5, pady=5)

            self.buttonList.append(Button(self.frameInCanvas, text='Modify test', command=lambda i=i: self.modifyTest(i)))
            self.buttonList[i].grid(row=rowCounter, column=1, padx=5, pady=5)

            rowCounter += 1

        Button(self.frameInCanvas, text="Back", command=self.back).grid(row=rowCounter+1, column=0, padx=5, pady=5)

    def modifyTest(self, testNumber):
        tests = Tests().getTest()
        testNumber, testName, testContent, testType, deadline = tests[testNumber]
        Tests(testNumber=testNumber, testName=testName, testContent=testContent, testType=testType, deadline=deadline).currentTest()
        self.master.switch_frame('modify')

    def back(self):
        self.master.switch_frame('Lecturer')



    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
