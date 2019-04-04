from tkinter import *
from Project.data import *
import shelve

class Result():                 # i'm using this code to normalize the data and turn it into an object so the rest of the code can understand it easier
    def __init__(self,student,name,attempts,scores):
        self.studentID=student
        self.testname=name
        self.scores=scores
        self.mark=self.calc_mark()
        self.attempts=attempts

    def calc_mark(self):
        right=0
        ss=self.scores
        for s in ss:
            if s==1:
                right+=1
        return (right,len(ss))

    def __str__(self):
        return str(self.studentID)+", "+str(self.testname)+": "+str(self.mark[0])+"/"+str(self.mark[1])

class statsView(Frame):
    def __init__(self,master):
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
        Button(self.frameInCanvas, text="Back", command=self.back).grid(row=5, column=0, padx=5, pady=5)
        self.outputTextBox=Text(self.frameInCanvas)
        self.outputTextBox.grid(row=2,column=0,rowspan=3,columnspan=3,padx=5,pady=5)
        Label(self.frameInCanvas, text="Generate stats").grid(row=1, column=0, padx=5, pady=5)
        Button(self.frameInCanvas, text="Formative", command=self.genFormativeStats).grid(row=1, column=1, padx=5, pady=5)
        Button(self.frameInCanvas, text="Summative", command=self.genSummativeStats).grid(row=1, column=2, padx=5, pady=5)

    def back(self):
        self.master.switch_frame('Lecturer')

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def genFormativeStats(self):
        self.outputTextBox.delete(1.0, END)
        self.outputTextBox.insert(INSERT,"testing formative button")

    def genSummativeStats(self):
        self.outputTextBox.delete(1.0, END)
        outputText=""
        #outputText+=self.compileStats(1,"S")+"\n"
        #outputText+=self.compileStats(2,"S")+"\n"
        #outputText+=self.compileStats(3,"S")
        self.outputTextBox.insert(INSERT,outputText)

    def getStudentStats(self):
        studentList=[]
        names,passwords,types=Users().openData()
        for t in range(len(types)):
            if types[t]=='s':
                studentList.append(names[t])
        testNumber = Tests().getCurrentTest()[0]
        trials = Test_record(user=user, testNumber=testNumber).getTrials()
        testRetrieve = Test_record(user=user, testNumber=testNumber, trial=trials[-1]).getTestScore()
        # FORMAT -- Retrieve = [user, testNumber, trial, response, score, totalQuestions]
        responseList = testRetrieve[3]
        self.results_list=[]

        correctAnswers = testRetrieve[4]
        totalQuestions = testRetrieve[5]


    def compileStats(self,stat_num,SorF): # 1 gives you the
        # a result istaken as  a 4-length list [student,testname,attemptstaken,answers]
        results_list=[[i[0],i[1],i[2],i[3:]] for i in results]
        results_list_str=[str(r) for r in results_list]

        if stat_num in [1,3]:
            stat1=[len(results_list) for i in range(results_list[1].mark[1])]
            for r in results_list:
                for rs in range(len(stat1)):
                    stat1[rs]=stat1[rs]-r.scores[rs]    #stat1 is the list of how much of each question the qtudents got wrong
            if stat_num==1:
                return_list=""
                for i in range(len(stat1)):
                    return_list+=str(i+1)+": wrong"+str(stat1[i]*100/len(results_list))+"% of the time\n" #forma
                return return_list

            else:
                return ("question "+str(stat1.index(max(stat1))+1)+" was the worst-answered question with "+str(max(stat1)*100/len(results_list))+"% of students getting it wrong.")
        if stat_num==2:
            stat2=""
            for i in results_list:
                stat2+= i.studentID+" took"+str(i.attempts) +" to complete the test.\n"
            return stat2

"""
this code generates 1 of 3 statistics about the test results.
1: how often each question was answered incorrectly as a percentage
2: how many attempts each student took to do the test
3: the question answered incorrectly most often, aka an extension of 1:

i generated random test records to test this code but
this was done with no knowledge of how to get the data as i didn't work on the majority of the code

i can attempt to format the inputs in a way that works nicely with the rest of the code, but it might take a while
"""
