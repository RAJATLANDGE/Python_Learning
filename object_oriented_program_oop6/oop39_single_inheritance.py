

class Employee:

    def __init__(self, eid, name, last_name, pay):
        self.eid = eid
        self.name = name
        self.last_name = last_name
        self.salary = pay
        self.leaves = 10

    def __str__(self):
        return f"{self.__dict__}"

    def apply_for_leave(self, count):
        if count < self.leaves:
            self.leaves -= count
            print(f"Your Are Granted With {count} leave")
        else:
            print("you cannot take more leaves")

    def salary_raise(self):
        self.salary = self.salary * 1.20


class PermanentEmployee(Employee):

    def __init__(self,eid, name, last_name, pay, privilage_leaves, hra):
        self.privilage_leaves = privilage_leaves
        self.hra = hra

        super().__init__(eid, name, last_name, pay)

    def mediclaim(self):
        pass

    def Pf(self):
        pass

class ContractEmployee(Employee):
    pass


pe = PermanentEmployee(1, "Rajat", "landge", 800000 ,10, 5000)
e = Employee(2, "shubham", "satpute", 700000)
print(pe)
print(e)
print(pe.leaves)
pe.apply_for_leave(9)
print(pe.leaves)