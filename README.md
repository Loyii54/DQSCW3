"# DQSCW3"
This is the 4th reprogram of this system
This system opens new windows instead of deleting widgets which is much simplier and less buggy




-------For Team------

***To create a new window***
open new file called NAME_OF_CLASS.py
use below as template

from tkinter import *
from data import *

class NAME_OF_CLASS(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.METHOD_NAME()

    def METHOD_NAME(self):
        PASTE TK WIDGET CODE HERE

+++++++USE THIS AT END OF FILE FOR DEBUGGING+++++++
root = Tk()
root.title("Login")
root.state('zoomed')
app = NAME_OF_CLASS(root)
root.mainloop()





***To insert window into the app***
delete code at end of file used for debugging

FROM NAME_OF_CLASS.PY IMPORT *

frame = Toplevel(root)
frame.state('zoomed')
frame.title('TITLE')
NAME_OF_CLASS(frame)



***Data storage***
All data is currently stored in data.py
I will update this part if needed (if you don't understand)
