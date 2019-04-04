from tkinter import *
from tkinter import messagebox
from Project.data import *

class viewTestFormativeLecturer(Frame):

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
        studentCounter=0
        self.takenTestList = []
        for student in studentList:
            try:
                testTrials = Test_record(user=student, testNumber=currentTest[0]).getTrials()
                self.takenTestList.append(student)
                Label(self.frameInCanvas, text=student).grid(row=rowCounter, column=0, padx=5, pady=5)
                self.buttonList.append(Button(self.frameInCanvas, text='View test', command=lambda: self.viewTest(studentCounter)))
                self.buttonList[studentCounter].grid(row=rowCounter, column=1, padx=5, pady=5)
                rowCounter+=1
                studentCounter += 1
            except:
                pass

        all_student_scores = []
        for student in self.takenTestList:
            try:
                user = student
                Student_test_record = Test_record(user=user, testNumber=Tests().getCurrentTest()[0]).getTestScore()
                all_student_scores.append(Student_test_record)
            except:
                pass

        totalScore = 0
        number_of_question = 0
        for question in Tests().getCurrentTest()[2].rstrip().split('\n'):
            number_of_question += 1

        for student_score in all_student_scores:
            totalScore += student_score[4]
        try:
            averageScore = totalScore/len(all_student_scores)

            Label(self.frameInCanvas, text='Students on average scored: '+ str(averageScore) + '/' + str(number_of_question)).grid(row=0,column=0,columnspan=2,padx=5,pady=5)

            Button(self.frameInCanvas, text='Back', command=self.back).grid(row=rowCounter, column=0, padx=5, pady=5)
        except:
            Label(self.frameInCanvas, text='Students on average scored: '+ str(0) + '/' + str(number_of_question)).grid(row=0,column=0,columnspan=2,padx=5,pady=5)

            Button(self.frameInCanvas, text='Back', command=self.back).grid(row=rowCounter, column=0, padx=5, pady=5)

    def viewTest(self, number):
        # print("viewing test result for "+self.takenTestList[number]+" aka "+str(number))
        Users(username=self.takenTestList[number-1]).viewUser()
        self.master.switch_frame('viewIndividualTestFormativeLecturer')

    def back(self):
        Tests().currentTest()
        self.master.switch_frame('Lecturer')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
