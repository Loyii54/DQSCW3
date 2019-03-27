import shelve
# USE THIS TO INITIALIZE THE USERS student AND lecturer

# users = shelve.open("Users.db")
# users['users'] = {
#     'username' : ['student', 'lecturer'],
#     'password' : ['password', 'password'],
#     'usertype' : ['s', 't']
# }
# users.sync()
# users.close()

class Users():
    def __init__(self, username = '', password = ''):
        self.datafile = "Users.db"
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

# tests = shelve.open("Tests.db")
# tests['Tests'] = []
# tests.sync()
# tests.close()

class Tests():
    def __init__(self, testNumber=0, testName='', testContent='', testType=''):
        self.datafile = "Tests.db"
        self.testNumber = testNumber
        self.testName = testName
        self.testContent = testContent
        self.testType = testType

    def getNumberOfTests(self):
        tests = shelve.open(self.datafile)
        contents = tests['Tests']
        tests.close()
        return len(contents)

    def createTest(self):
        tests = shelve.open(self.datafile)
        numberOfTests = self.getNumberOfTests()
        temp = tests['Tests']
        temp.append([numberOfTests, self.testName, self.testContent, self.testType])
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
        tests['currentTest'] = [self.testNumber, self.testName, self.testContent, self.testType]
        tests.sync()
        tests.close()

    def getCurrentTest(self):
        tests = shelve.open(self.datafile)
        contents = tests['currentTest']
        tests.close()
        return contents


class Test_record():
    def __init__(self, user='', testNumber=0, trial=0, response=[], score=0, totalQuestions=0):
        self.datafile = "Test_records.db"
        self.user = user
        self.testNumber = testNumber
        self.trial = trial
        self.response = response
        self.score = score
        self.totalQuestions = totalQuestions

    def saveTestScore(self):
        testRecord = shelve.open(self.datafile)
        testRecord[self.user + str(self.testNumber) + "." + str(self.trial)] = [self.user, self.testNumber, self.trial, self.response, self.score, self.totalQuestions]
        if self.trial == 0:
            testRecord[self.user + str(self.testNumber)] = [0]
        else:
            self.saveTrials()
        testRecord.sync()
        testRecord.close()

    def saveTrials(self):
        testRecord = shelve.open(self.datafile)
        temp = testRecord[self.user + str(self.testNumber)]
        temp.append(self.trial)
        testRecord[self.user + str(self.testNumber)] = temp
        testRecord.sync()
        testRecord.close()

    def getTestScore(self):
        testRecord = shelve.open(self.datafile)
        contents = testRecord[self.user + str(self.testNumber) + "." + str(self.trial)]
        testRecord.close()
        return contents