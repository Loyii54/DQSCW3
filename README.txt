Create python file called CLASS_NAME.py and use below

------------------------------------------------------------------------------------------------------------------------------------------

#Imports for the window
from tkinter import *
from data import *

#Class for the window
class CLASS_NAME(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.main()

    def main(self):
        INSERT TKINTER CODE HERE


#USE BELOW FOR DEBUGGING
root = Tk()
root.title("Login")
root.state('zoomed')
app = CLASS_NAME(root)
root.mainloop()

==========================================================================================================================================

After making sure everything works
Delete "#USE BELOW FOR DEBUGGING"

Import your file into app.py and add a string of your class and the actual class into self.pages dictionary in app.py.

Add the below to the place where you want your window to pop up whenever a command is performed (usually a button click).

    self.master.switch_frame('STRING OF YOUR CLASS IN SELF.PAGES DICTIONARY IN APP.PY')

------------------------------------------------------------------------------------------------------------------------------------------

For futher reference you may use app.py, student.py, takeTest.py, summativeTestFeedback.py as reference

------------------------------------------------------------------------------------------------------------------------------------------

Then replace your __init__() in your code with the following.

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


Also add the following to the end of your class.

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


!!!IMPORTANT!!!
Then replace all self in your tkinter widgets to self.frameInCanvas
    i.e.
        Label(self, text='Hi')
        vvv
        Label(self.frameInCanvas, text='Hi')


This will add a scrollbar into your window by putting the frame into the canvas

==========================================================================================================================================

Tips on writing your Tkinter code:

Don't use messagebox for now, it messes up the order of the windows. View takeTest.py for warningAnswerAllQuestions as an example to get around this warningAnswerAllQuestions.py is saved in message folder

self.master.destroy() destroys the current window
self.master.master.destroy() destroys the parent window (which will also destroy the current window)
self.wait_window(frame) can be used to halt any actions on a certain window until the 'frame' window is closed
    i.e. The current window will not destroy until the child window 'frame' is destroyed
        frame = Toplevel(self.master)
        frame.state('zoomed')
        frame.title(Users().getCurrentUser())
        summativeTestFeedback(frame)
        self.wait_window(frame)
        self.master.destroy()

Remember to import your tkinter code python file into app.py

'try, except' can be used to test for errors and hence run another code. Used to replace 'if, else' if the if statement will cause an error
    i.e. This will try to getTrials(), if getTrials() gives an error (due to it not been initalized), it will run another code which does not
         require the Trial number
        try:
            Test_record(user=Users().getCurrentUser(), testNumber=i).getTrials()
            self.buttonList.append(Button(self, text='Take test',state="disabled", command=lambda i=i: self.takeTest(i)))
            self.buttonList[i].grid(row=rowCounter, column=1, padx=5, pady=5)
        except:
            self.buttonList.append(Button(self, text='Take test',command=lambda i=i: self.takeTest(i)))
            self.buttonList[i].grid(row=rowCounter, column=1, padx=5, pady=5)

==========================================================================================================================================

data.py uses shelve to keep results, it is rather simple look it up on google.

------------------------------------------------------------------------------------------------------------------------------------------

Users class stores in "Users.db" - main purpose is for user data
Main paramaters:
username String
password String



Initialize with Storing a dictionary of users in ['users']
{'username' : ['student', 'student2', 'lecturer'],
 'password' : ['password', 'password','password'],
 'usertype' : ['s', 's', 't']}

opendata()          returns lists for usernames, passwords, usertypes
                        ['student', 'student2', 'lecturer']
                        ['password', 'password','password']
                        ['s', 's', 't']
checkdata()         checks if input data is correct (checks if password matches username)
currentUser()       changes ['currentuser'] to the current user that has logged in
                        'student'
getCurrentUser()    returns whats inside ['currentuser'] (the current user that has logged in)

------------------------------------------------------------------------------------------------------------------------------------------

Tests class stores in "Tests.db" - main purpose is for Test data
Main parameters:
testNumber Integer
testName String
testContent String
testType Character
deadline datetime

['Test'] contains a list of all the tests
each test is a list contain its content
[[testNumber0, testName0, testContent0, testType0, deadline0],
 [testNumber1, testName1, testContent1, testType1, deadline1],...]

getNumberOfTests()  returns the number of tests saved in tests['Tests']
createTest()        creates a test from the input given using this format
                        [testNumber(the test id), testName, testContent, testType, deadline]
getTest()           returns a list of all the tests
currentTest()       changes ['currentTest'] to the current test being viewed in the app in this format
                        [testNumber, testName, testContent, testType, deadline]
getCurrentTest()    returns whats inside ['currentTest'] (the current test being viewed in the app)

------------------------------------------------------------------------------------------------------------------------------------------

Test_record class stores in "Test_records.db" - main purpose is to store test results
Main parameters:
user            String
testNumber      Integer
trial           Integer
response        List
score           Integer
totalQuestions  Integer

saveTestScore()     changes ['user.testNumber.trial'] to test results data in a list in this format
                        [user, testNumber, trial, response, score, totalQuestions]
getTestScore()      returns test results saved in ['user.testNumber.trial']
getTrials()         return a list of tries (saved in ['user.testNumber']) that a student has attempted in a certain test

==========================================================================================================================================
