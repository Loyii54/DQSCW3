from tkinter import *
from data import *

class Modify(Frame):

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

        #Test Type

        lblType = Label(self.frameInCanvas, text='Specify the type of Assessment:', font=('MS', 12, 'bold'))
        lblType.grid(row=3, column=0)
        lblFrmtv = Label(self.frameInCanvas, text = 'Formative \n Assessment', font=('MS', 9, 'bold'))
        lblFrmtv.grid(row=1, column=1, rowspan=2)
        lblSmtv = Label(self.frameInCanvas, text = 'Summative \n Assessment', font=('MS', 9, 'bold'))
        lblSmtv.grid(row=1, column=2, rowspan=2)

        self.varQ1 = IntVar()
        self.varQ1.set(currentTest[3])

        R1Q1 = Radiobutton(self.frameInCanvas, variable=self.varQ1, value=2)
        R1Q1.grid(row=3, column=1)

        R2Q1 = Radiobutton(self.frameInCanvas, variable=self.varQ1, value=1)
        R2Q1.grid(row=3, column=2)

        #Deadline

        self.var_deadline = StringVar()
        self.var_deadline.set(str(currentTest[4].strftime("%Y-%m-%d %H:%M")))

        Label(self.frameInCanvas, text="Specify Deadline (e.g. '2019-12-01 00:00'):", font=('MS', 12, 'bold')).grid(row=5,column=0)
        deadline_text = Entry(self.frameInCanvas, textvariable=self.var_deadline)
        deadline_text.grid(row=5,column=1)

        #Test Name

        self.var_testName = StringVar()
        self.var_testName.set(currentTest[1])

        Label(self.frameInCanvas, text="Enter Test Name:", font=('MS', 12, 'bold')).grid(row=6,column=0)
        testname_text = Entry(self.frameInCanvas, textvariable=self.var_testName)
        testname_text.grid(row=6,column=1)


        #Test Content
        testContent = currentTest[2]

        cleanTestContent = testContent.rstrip()

        testQuestions = cleanTestContent.split('\n')

        rowcounter = 7
        self.var_answersDict = {}
        self.var_questionsDict = {}
        self.var_questionNameDict = {}
        radiobuttonDict = {}
        for question in testQuestions:
            radiobuttonDict[question] = []
            questionList=question.split(', ')
            question_name = questionList[0]
            Answer1 = questionList[1]
            Answer2 = questionList[2]
            Answer3 = questionList[3]
            Answer4 = questionList[4]
            REALAnswer = int(questionList[5])


            var_answer1 = StringVar()
            var_answer1.set(Answer1)

            var_answer2 = StringVar()
            var_answer2.set(Answer2)

            var_answer3 = StringVar()
            var_answer3.set(Answer3)

            var_answer4 = StringVar()
            var_answer4.set(Answer4)

            self.var_answersDict[question] = [var_answer1, var_answer2, var_answer3, var_answer4]

            var_questionAnswer = IntVar()
            self.var_questionsDict[question]= var_questionAnswer


            var_questionName = StringVar()
            var_questionName.set(question_name)
            self.var_questionNameDict[question] = var_questionName

            Label(self.frameInCanvas, text="Question " + str(question), font=('MS', 12, 'bold')).grid(row=rowcounter, column=0, sticky="W")

            Label(self.frameInCanvas, text="Enter Question:", font=('MS', 9, 'bold')).grid(row=rowcounter+1, column=0)
            Entry(self.frameInCanvas, textvariable=self.var_questionNameDict[question]).grid(row=rowcounter+1, column=1)

            radiobuttonDict[question].append(Radiobutton(self.frameInCanvas, variable=self.var_questionsDict[question], value=1))
            radiobuttonDict[question][0].grid(row=rowcounter+2, column=0)
            Entry(self.frameInCanvas, textvariable=self.var_answersDict[question][0]).grid(row=rowcounter+2, column=1)

            radiobuttonDict[question].append(Radiobutton(self.frameInCanvas, variable=self.var_questionsDict[question], value=2))
            radiobuttonDict[question][1].grid(row=rowcounter+2, column=2)
            Entry(self.frameInCanvas, textvariable=self.var_answersDict[question][1]).grid(row=rowcounter+2, column=3)

            radiobuttonDict[question].append(Radiobutton(self.frameInCanvas, variable=self.var_questionsDict[question], value=3))
            radiobuttonDict[question][2].grid(row=rowcounter+2, column=4)
            Entry(self.frameInCanvas, textvariable=self.var_answersDict[question][2]).grid(row=rowcounter+2, column=5)

            radiobuttonDict[question].append(Radiobutton(self.frameInCanvas, variable=self.var_questionsDict[question], value=4))
            radiobuttonDict[question][3].grid(row=rowcounter+2, column=6)
            Entry(self.frameInCanvas, textvariable=self.var_answersDict[question][3]).grid(row=rowcounter+2, column=7)


            if REALAnswer == 1:
            	radiobuttonDict[question][0].select()
            elif REALAnswer == 2:
            	radiobuttonDict[question][1].select()
            elif REALAnswer == 3:
            	radiobuttonDict[question][2].select()
            else:
            	radiobuttonDict[question][3].select()

            rowcounter += 3

        Button_Submit = Button(self.frameInCanvas, text="Finish", command=self.storeAssessment).grid(row=rowcounter+3, column=0)

    def storeAssessment(self):
        testName = self.var_testName.get()

        currentTest = Tests().getCurrentTest()

        testContentA = currentTest[2]

        cleanTestContent = testContentA.rstrip()

        testQuestions = cleanTestContent.split('\n')

        questionsList = []


        for question in testQuestions:
            questionName = self.var_questionNameDict[question]
            questionAnswers = self.var_answersDict[question]
            RealAnswer = self.var_questionsDict[question]
            Question = str(questionName.get()) + ', ' + str(questionAnswers[0].get()) + ', ' + str(questionAnswers[1].get()) + ', ' + str(questionAnswers[2].get()) + ', ' + str(questionAnswers[3].get()) + ', ' + str(RealAnswer.get())
            questionsList.append(Question)

        testContent = ''
        for question in questionsList:
            testContent = testContent + question + '\n'

        testType = self.varQ1.get()

        deadlineError = False

        try:
            deadline = datetime.datetime.strptime(self.var_deadline.get(), "%Y-%m-%d %H:%M")
        except:
            deadlineError = True

        testContentError = False


        try:
            cleanTestContent = testContent.rstrip()
            testQuestions = cleanTestContent.split('\n')
            for question in testQuestions:
                questionList=question.split(', ')
                Question = questionList[0]
                Answer1 = questionList[1]
                Answer2 = questionList[2]
                Answer3 = questionList[3]
                Answer4 = questionList[4]
                REALAnswer = int(questionList[5])
        except:
            testContentError = True

        if (self.varQ1.get()==0):
            messagebox.showwarning('Warning','Please Specify Assessment Type')
        elif testContentError == True:
            messagebox.showwarning('Warning','Please Check Your Questions')
        elif deadlineError == True:
            messagebox.showwarning('Warning','Please Check The Deadline')
        elif testName == '':
            messagebox.showwarning('Warning','Please Check The Test Name')
        else:
            Tests(testNumber=Tests().getCurrentTest()[0], testName=testName, testContent=testContent, testType=testType, deadline=deadline).modifyTest()
            messagebox.showinfo('Success','Test Modified')
            self.master.switch_frame('Lecturer')


    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
