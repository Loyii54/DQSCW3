from tkinter import *
from Project.data import *
""" Import all frames in the application here """
from Project.student import student
from Project.login import login
from Project.takeTest import takeTest
from Project.summativeTestFeedback import summativeTestFeedback
from Project.viewAnswerStudent import viewAnswerStudent
from Project.lecturer import lecturer
from Project.createTest import createTest
from Project.formativeTestFeedback import formativeTestFeedback
from Project.Modify import Modify
from Project.modifyTest import modifyTest
from Project.viewTest import viewTest
from Project.viewTestSummativeLecturer import viewTestSummativeLecturer
from Project.viewIndividualTestSummativeLecturer import viewIndividualTestSummativeLecturer
from Project.statsGen import statsView,Result
from Project.viewTestFormativeLecturer import viewTestFormativeLecturer
from Project.viewIndividualTestFormativeLecturer import viewIndividualTestFormativeLecturer

class App(Tk):
    def __init__(self):
        """
            Initialise the frames imported and move Login Frame to front.
        """
        Tk.__init__(self)

        """
            Code To change frames derived from Steven M. Vascellaro at
            https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
            Multi-frame tkinter application v2.3
        """
        """
            Scrollbar code at the start of each frame class is derived from Steven Bryan Oakley
            Details on login.py
        """
        self.current_frame = None
        self.pages = {'Login': login,
                 'Student': student,
                 'takeTest': takeTest,
                 'summativeTestFeedback': summativeTestFeedback,
                 'viewAnswerStudent': viewAnswerStudent,
                 "Lecturer": lecturer,
                 "createTest": createTest,
                 'formativeTestFeedback': formativeTestFeedback,
                 'modify': Modify,
                 'modifyTest': modifyTest,
                 'viewTest': viewTest,
                 'viewTestSummativeLecturer': viewTestSummativeLecturer,
                 'viewIndividualTestSummativeLecturer': viewIndividualTestSummativeLecturer,
                 'viewStats': statsView,
                 'viewTestFormativeLecturer': viewTestFormativeLecturer,
                 'viewIndividualTestFormativeLecturer': viewIndividualTestFormativeLecturer
                 }

        self.switch_frame('Login')

    def switch_frame(self, frame_name):
        """
            Destroys current frame and replaces it with a new one.
        """
        if self.current_frame is not None:
            self.current_frame.destroy()

        new_frame = self.pages[frame_name](self)
        self.current_frame = new_frame

        self.current_frame.pack(side=TOP, fill='both', expand=True)



app = App()
app.title('Application')
app.state('zoomed')
app.mainloop()


