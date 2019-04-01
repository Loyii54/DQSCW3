from tkinter import *
from data import *
""" Import all frames in the application here """
from student import student
from login import login
from takeTest import takeTest
from summativeTestFeedback import summativeTestFeedback

class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.current_frame = None
        self.pages = {'Login': login,
                 'Student': student,
                 'takeTest': takeTest,
                 'summativeTestFeedback': summativeTestFeedback,
                 }

        self.switch_frame('Login')

    def switch_frame(self, frame_name):
        """Destroys current frame and replaces it with a new one."""
        if self.current_frame is not None:
            self.current_frame.destroy()

        new_frame = self.pages[frame_name](self)
        self.current_frame = new_frame

        if frame_name == 'Login':
            self.current_frame.pack(side=TOP, fill='both', expand=True)
        else:
            self.current_frame.pack(side=TOP, fill='both', expand=True)



def main():
    app = App()
    app.title('Application')
    app.state('zoomed')
    app.mainloop()

if __name__ == '__main__':
    main()
