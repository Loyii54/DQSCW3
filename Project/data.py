import shelve
import datetime
# USE THIS TO INITIALIZE THE USERS student AND lecturer

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
        self.datafile = "Data/Users.db"
        self.username = username
        self.password = password

    def openData(self):
        users = shelve.open(self.datafile)
        userinfo = users['users']
        usernames = userinfo['username']
        passwords = userinfo['password']
        usertypes = userinfo['usertype']
        users.close()
        return usernames, passwords, usertypes

    def checkData(self):
        usernames, passwords, usertypes = self.openData()
        if self.username in usernames:
            position = usernames.index(self.username)
            if self.password == passwords[position]:
                return 1, usertypes[position]
            else:
                return 0
        else:
            return 0

    def currentUser(self):
        users = shelve.open(self.datafile)
        users['currentuser'] = self.username
        users.sync()
        users.close()

    def getCurrentUser(self):
        users = shelve.open(self.datafile)
        currentUser = users['currentuser']
        users.close()
        return currentUser

# initialize Tests.db

# tests = shelve.open("Data/Tests.db")
# tests['Tests'] = []
# tests.sync()
# tests.close()

class Tests():
    def __init__(self, testNumber=0, testName='', testContent='', testType='', deadline=datetime.datetime(2019, 4, 1, 00, 00)):
        self.datafile = "Data/Tests.db"
        self.testNumber = testNumber
        self.testName = testName
        self.testContent = testContent
        self.testType = testType
        self.deadline = deadline

    def getNumberOfTests(self):
        tests = shelve.open(self.datafile)
        contents = tests['Tests']
        tests.close()
        return len(contents)

    def createTest(self):
        tests = shelve.open(self.datafile)
        numberOfTests = self.getNumberOfTests()
        temp = tests['Tests']
        temp.append([numberOfTests, self.testName, self.testContent, self.testType, self.deadline])
        tests['Tests'] = temp
        tests.sync()
        tests.close()

    def getTest(self):
        tests = shelve.open(self.datafile)
        contents = tests['Tests']
        tests.close()
        return contents

    def currentTest(self):
        tests = shelve.open(self.datafile)
        tests['currentTest'] = [self.testNumber, self.testName, self.testContent, self.testType, self.deadline]
        tests.sync()
        tests.close()

    def getCurrentTest(self):
        tests = shelve.open(self.datafile)
        contents = tests['currentTest']
        tests.close()
        return contents


class Test_record():
    def __init__(self, user='', testNumber=0, trial=0, response=[], score=0, totalQuestions=0):
        self.datafile = "Data/Test_records.db"
        self.user = user
        self.testNumber = testNumber
        self.trial = trial
        self.response = response
        self.score = score
        self.totalQuestions = totalQuestions

    def saveTestScore(self):
        testRecord = shelve.open(self.datafile, writeback=True)
        testRecord[self.user + "." + str(self.testNumber) + "." + str(self.trial)] = [self.user, self.testNumber, self.trial, self.response, self.score, self.totalQuestions]
        if self.trial == 0:
            testRecord[str(self.user + '.' + str(self.testNumber))] = [0]
        else:
            testRecord[self.user + '.' + str(self.testNumber)].append(self.trial)
        testRecord.sync()
        testRecord.close()


    def getTrials(self):
        testRecord = shelve.open(self.datafile)
        contents = testRecord[self.user + '.' + str(self.testNumber)]
        testRecord.close()
        return contents

    def getTestScore(self):
        testRecord = shelve.open(self.datafile)
        contents = testRecord[self.user + "." + str(self.testNumber) + "." + str(self.trial)]
        testRecord.close()
        return contents
