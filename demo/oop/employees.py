class Employee:
    def __init__(self, name, job, email=None):
        self.name = name
        self.job = job
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.job} - {self.email}"

    def changejob(self, newjob):
        self.job = newjob


class SalariedEmployee(Employee):
    def __init__(self, name, job, email, salary):
        super().__init__(name, job, email)
        self.salary = salary

    def getsalary(self):
        return self.salary

    # Overriding
    def __str__(self):
        return f"{super().__str__()} - {self.salary}"


class Consultant(Employee):
    def __init__(self, name, job, email, hours, rate):
        super().__init__(name, job, email)
        self.hours = hours
        self.rate = rate

    def getsalary(self):
        return self.hours * self.rate

    def __str__(self):
        return f"{super().__str__()} - {self.hours} - {self.rate}"


c = Consultant("Scott", "Sr.Prog", "scott@gmail.com", 150, 2000)
c.changejob("TL")
print(c)
s = SalariedEmployee("Mark", "DBA", "mark@microsoft.com", 300000)
print(s)

print(isinstance(c, Consultant))
print(isinstance(c, Employee))
print(isinstance(c, SalariedEmployee))
print(issubclass(Consultant, Employee))

print(Employee.__bases__)