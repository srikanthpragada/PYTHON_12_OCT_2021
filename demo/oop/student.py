class Student:
    courses = {'python': 5000, 'java': 10000, '.net': 7500}

    @staticmethod
    def gettotalfee(course):
        return Student.courses[course]

    def __init__(self, name, course, feepaid=0):
        if course not in Student.courses:
            raise ValueError("Invalid course name")

        self.name = name
        self.course = course
        self.feepaid = feepaid

    def payment(self, amount):
        self.feepaid += amount

    @property
    def dueamount(self):
        return self.totalfee() - self.feepaid

    def totalfee(self):
        return Student.gettotalfee(self.course)

    def __str__(self):
        return f"{self.name} - {self.course} - {self.totalfee()} - {self.feepaid}"



print(Student.gettotalfee('python'))

s1 = Student('Bill', 'javaee', 5000)
s1.payment(2000)
print(s1)
print(s1.dueamount)
