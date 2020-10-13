class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print "Name:", self.lastName + ",", self.firstName
		print "ID:", self.idNumber

class Student(Person):

    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
   
    # Write your constructor here
    def __init__(self,firstName,lastName,idNum,scores):
        self.firstName=firstName
        self.lastName=lastName
        self.idNumber=idNum
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.

    # Write your function here
    def calculate(self):
        sum = 0
        for score in self.scores:
            sum = sum + score
            
        total = sum/len(self.scores)
        
        if(100>=total>=90):
            return 'O'
        elif(90>total>=80):
            return 'E';
        elif(80>total>=70):
            return 'A';
        elif(70>total>=55):
            return 'P';
        elif(55>total>=40):
            return 'D';
        else:
            return 'T';        

line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input()) # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()