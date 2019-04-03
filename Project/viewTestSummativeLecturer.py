from tkinter import *
from tkinter import messagebox
from data import *

class viewTestSummativeLecturer(Frame):

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
        currentTest = Tests().getCurrentTest()
        usernames, passwords, usertypes = Users().openData()

        userCounter = 0
        studentList = []
        for user in usertypes:
            if user == 's':
                studentList.append(usernames[userCounter])
                userCounter += 1

        self.buttonList = []
        rowCounter=10
        studentCoutner=0
        self.takenTestList = []

        for student in studentList:
            try:
                testTrials = Test_record(user=student, testNumber=currentTest[0]).getTrials()
                self.takenTestList.append(student)
                Label(self.frameInCanvas, text=student).grid(row=rowCounter, column=0, padx=5, pady=5)
                self.buttonList.append(Button(self.frameInCanvas, text="View test", command=lambda: self.viewTest(student)))
                self.buttonList[studentCoutner].grid(row=rowCounter, column=1, padx=5, pady=5)
                rowCounter+=1
                studentCoutner += 1
            except:
                pass

        all_student_scores = []
        for student in self.takenTestList:
            user = student
            Student_test_record = Test_record(user=user, testNumber=Tests().getCurrentTest()[0]).getTestScore()
            all_student_scores.append(Student_test_record)

        totalScore = 0
        for student_score in all_student_scores:
            totalScore += student_score[4]
        averageScore = totalScore/len(all_student_scores)

        Label(self.frameInCanvas, text='Students on average scored: '+ str(averageScore) + '/' + str(Test_record(user=user, testNumber=Tests().getCurrentTest()[0]).getTestScore()[5])).grid(row=0,column=0,columnspan=2,padx=5,pady=5)

        Button(self.frameInCanvas, text='Back', command=self.back).grid(row=rowCounter, column=0, padx=5, pady=5)

    def viewTest(self, student):
        Users(username=student).viewUser()
        self.master.switch_frame('viewIndividualTestSummativeLecturer')

    def back(self):
        Tests().currentTest()
        self.master.switch_frame('Lecturer')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
