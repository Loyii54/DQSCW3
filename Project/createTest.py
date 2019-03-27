from tkinter import *
from data import *

class createTest(Frame):

    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.createTestMain()

    def createTestMain(self):
        Label(self,
            text = """To create a Question, follow this format:
            Question, answer 1, answer 2, answer 3, answer 4, real answer number
            Create each Question on a new line.
            i.e.
            What is the first letter of the alphabet?, A, B, C, D, 1
            How many neckbones does a giraffe have? 5, 6, 7, 8, 3
            """).grid(row=0, column=0,  columnspan=5, padx=5, pady=5)


        self.var_test_name = StringVar()
        Label(self, text="Test name:").grid(row=1, column=0,padx=5, pady=5, sticky='NE')
        test_name_text = Entry(self, textvariable=self.var_test_name)
        test_name_text.grid(row=1, column=1,padx=5, pady=5, sticky='W')

        Label(self, text="Test:").grid(row=2, column=0,padx=5, pady=5, sticky='NE')
        self.text_test = Text(self, height = 10)
        self.text_test.grid(row=2, column=1, columnspan=5, padx=5, pady=5)
        scroll = Scrollbar(self,command= self.text_test.yview)
        self.text_test.configure(yscrollcommand=scroll.set)
        scroll.grid(row=2, column=6, sticky='ns')

        self.test_type = IntVar()

        radio_summativeTest = Radiobutton(self, text= "Summative Test", variable=self.test_type, value=1)
        radio_formativeTest = Radiobutton(self, text= "Formative Test", variable=self.test_type, value=2)
        radio_summativeTest.grid(row=3, column=1,padx=5, pady=5)
        radio_formativeTest.grid(row=3, column=2,padx=5, pady=5)


        button_createTestSubmit = Button(self, text="Create",
            command=self.createTestSubmit)
        button_createTestSubmit.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

    def createTestSubmit(self):
        test_name = self.var_test_name.get()
        test_content = self.text_test.get('1.0', END)
        test_type = self.test_type.get()
        Tests(testName=test_name, testContent=test_content, testType=test_type).createTest()
