import shelve
import datetime

# INITIALISE users
# users = shelve.open("Data/Users.db")
# users['users'] = {
#     'username' : ['student', 'student2', 'lecturer'],
#     'password' : ['password', 'password','password'],
#     'usertype' : ['s', 's', 't']
# }
# users.sync()
# users.close()

class Users():
    def __init__(self, username = '', password = ''):
        """
            Contains database for User information
        """
        self.datafile = "Data/Users.db"
        self.username = username
        self.password = password

    def openData(self):
        """
            Returns lists for usernames, passwords, usertypes
                ['student', 'student2', 'lecturer']
                ['password', 'password','password']
                ['s', 's', 't']

            REQUIRED: NONE
        """
        users = shelve.open(self.datafile)
        userinfo = users['users']
        usernames = userinfo['username']
        passwords = userinfo['password']
        usertypes = userinfo['usertype']
        users.close()
        return usernames, passwords, usertypes

    def checkData(self):
        """
            Checks if input data is correct (checks if password matches username)

            REQUIRED: username, password
        """
        usernames, passwords, usertypes = self.openData()
        if self.username in usernames:
            position = usernames.index(self.username)
            if self.password == passwords[position]:
                return 1, usertypes[position]
            else:
                return 0
        else:
            return 0

    def viewUser(self):
        """
            Changes ['viewuser'] to the current user that has logged in
                i.e. 'student'

            REQUIRED: username
        """
        users = shelve.open(self.datafile)
        users['viewuser'] = self.username
        users.sync()
        users.close()

    def getViewUser(self):
        """
            Returns whats inside ['viewuser'] (the current user that has logged in)

            REQUIRED: NONE
        """
        users = shelve.open(self.datafile)
        currentUser = users['viewuser']
        users.close()
        return currentUser

    def currentUser(self):
        """
            Changes ['currentuser'] to the current user that has logged in
                i.e. 'student'

            REQUIRED: username
        """
        users = shelve.open(self.datafile)
        users['currentuser'] = self.username
        users.sync()
        users.close()

    def getCurrentUser(self):
        """
            Returns whats inside ['currentuser'] (the current user that has logged in)

            REQUIRED: NONE
        """
        users = shelve.open(self.datafile)
        currentUser = users['currentuser']
        users.close()
        return currentUser

#INITIALISE tests

# tests = shelve.open("Data/Tests.db")
# tests['Tests'] = []
# tests.sync()
# tests.close()

class Tests():
    def __init__(self, testNumber=0, testName='', testContent='', testType='', deadline=datetime.datetime(2019, 4, 1, 00, 00)):
        """
            Contains database for Test information
        """
        self.datafile = "Data/Tests.db"
        self.testNumber = testNumber
        self.testName = testName
        self.testContent = testContent
        self.testType = testType
        self.deadline = deadline

    def getNumberOfTests(self):
        """
            Returns the number of tests saved in tests['Tests']

            REQUIRED: NONE
        """
        tests = shelve.open(self.datafile)
        contents = tests['Tests']
        tests.close()
        return len(contents)

    def createTest(self):
        """
            Creates a test from the input given using this format
                [testNumber(the test id), testName, testContent, testType, deadline]

            REQUIRED: testName, testContent, testType, deadline
        """
        tests = shelve.open(self.datafile)
        numberOfTests = self.getNumberOfTests()
        temp = tests['Tests']
        temp.append([numberOfTests, self.testName, self.testContent, self.testType, self.deadline])
        tests['Tests'] = temp
        tests.sync()
        tests.close()

    def getTest(self):
        """
            Returns a list of all the tests
                [[testNumber0, testName0, testContent0, testType0, deadline0],
                [testNumber1, testName1, testContent1, testType1, deadline1],...]

            REQUIRED: NONE
        """
        tests = shelve.open(self.datafile)
        contents = tests['Tests']
        tests.close()
        return contents

    def currentTest(self):
        """
            Changes ['currentTest'] to the current test being viewed in the app in this format
                [testNumber, testName, testContent, testType, deadline]

            REQUIRED: testNumber, testName, testContent, testType, deadline
        """
        tests = shelve.open(self.datafile)
        tests['currentTest'] = [self.testNumber, self.testName, self.testContent, self.testType, self.deadline]
        tests.sync()
        tests.close()

    def getCurrentTest(self):
        """
            Returns whats inside ['currentTest'] (the current test being viewed in the app)

            REQUIRED: NONE
        """
        tests = shelve.open(self.datafile)
        contents = tests['currentTest']
        tests.close()
        return contents

    def modifyTest(self):
        """
            Modify given test

            REQUIRED: testNumber, testName, testContent, testType, deadline
        """
        tests = shelve.open(self.datafile)
        temp = tests['Tests']
        temp[self.testNumber] = [self.testNumber ,self.testName, self.testContent, self.testType, self.deadline]
        tests['Tests'] = temp
        tests.sync()
        tests.close()

class Test_record():
    def __init__(self, user='', testNumber=0, trial=0, response=[], score=0, totalQuestions=0):
        """
            Contains database for Test Records information
        """
        self.datafile = "Data/Test_records.db"
        self.user = user
        self.testNumber = testNumber
        self.trial = trial
        self.response = response
        self.score = score
        self.totalQuestions = totalQuestions

    def saveTestScore(self):
        """
            Changes ['user.testNumber.trial'] to test results data in a list in this format
                [user, testNumber, trial, response, score, totalQuestions]

            REQUIRED: user, testNumber, trial, response, score, totalQuestions
        """
        testRecord = shelve.open(self.datafile, writeback=True)
        testRecord[self.user + "." + str(self.testNumber) + "." + str(self.trial)] = [self.user, self.testNumber, self.trial, self.response, self.score, self.totalQuestions]
        if self.trial == 0:
            testRecord[str(self.user + '.' + str(self.testNumber))] = [0]
        else:
            testRecord[self.user + '.' + str(self.testNumber)].append(self.trial)
        testRecord.sync()
        testRecord.close()


    def getTrials(self):
        """
            Return a list of tries (saved in ['user.testNumber']) that a student has attempted in a certain test

            REQUIRED: user, testNumber
        """
        testRecord = shelve.open(self.datafile)
        contents = testRecord[self.user + '.' + str(self.testNumber)]
        testRecord.close()
        return contents

    def getTestScore(self):
        """
            Returns test results saved in ['user.testNumber.trial']

            REQUIRED: user, testNumber, trial
        """
        testRecord = shelve.open(self.datafile)
        contents = testRecord[self.user + "." + str(self.testNumber) + "." + str(self.trial)]
        testRecord.close()
        return contents
