class Employee:

    def __init__(self, eid, name, salary):
        self.eid = eid
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.__dict__}"

    def give_increment(self):
        self.salary += (self.salary * 10) / 100


class Manager(Employee):

    def __init__(self, eid, name, salary, team):
        self.team = team
        super(Manager, self).__init__(eid, name, salary)

    def give_increment(self):  # override shortcut control + "o"
        self.salary += (self.salary * 12) / 100


class Developer(Employee):

    def __init__(self, eid, name, salary, programming_lang):
        self.prog = programming_lang
        super(Developer, self).__init__(eid, name, salary)

    def give_increment(self):
        self.salary += (self.salary * 15) / 100


e1 = Employee(1, "rahul", 500000)
m1 = Manager(2, "prashant", 600000, "team-A")
d1 = Developer(3, "Gopal", 700000, "Python")
e1.give_increment()
print(e1.salary)
m1.give_increment()
print(m1.salary)
d1.give_increment()
print(d1.salary)
