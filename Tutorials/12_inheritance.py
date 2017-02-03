# inheritance
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, score):
        Person.__init__(self, firstName, lastName, idNumber)
        self.score = score
    def calculate(self):
        a = sum(self.score)/len(self.score)
        if a>=90:
            return "O"
        elif a>=80:
            return "E"
        elif a>=70:
            return "A"
        elif a>=55:
            return "P"
        elif a>=40:
            return "D"
        else:
            return "T"

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()