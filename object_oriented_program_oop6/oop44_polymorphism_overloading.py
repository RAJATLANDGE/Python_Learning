from datetime import datetime

from object_oriented_program_oop6.oop37_medicine_example import Medicine


class Student:

    def __init__(self, phy, chem, bio = None,  maths= None):
        if maths:                                                              # this is constructer overloading
            self.maths = maths

        self.phy = phy

        if bio:
            self.bio = bio

        self.chem = chem

    def __str__(self):
        return f"{self.__dict__}"

    def __add__(self, other):
        return Student(self.phy + other.phy, self.chem + other.chem)

    def engg_admission(self):                                            # this is called method overloading
        if hasattr(self, "maths"):
            print(" you have alloted with PCM course")
        else:
            print(" you have alloted with PCB course")


s1 = Student(89, 56, 78, 98)
print(s1)
s2 = Student(78, 55)
print(s2)
s3= Student(58,63,79,76)
print(s3)

s2.engg_admission()
print(hasattr(s1, "engg_admission"))
print(hasattr(s1,"chem"))

print("-----")
print(isinstance(4, int))
d = []
if isinstance(d, list):
    d.append(25)

if isinstance(d, dict):
    pass

if isinstance(d, (list, dict, tuple)):
    pass
print(d)

def test(x: int, y: float, z: str) -> str:                # this is called signature
    pass

def test1(a: list, b: dict) -> tuple:
    pass

def test2(a: list, b: dict) -> str:
    pass

def test3(x: int, y: float) -> str:
    pass


crocin = Medicine(1, "crocin", "cipla", 5, datetime(2023,3,18), datetime(2020,3,18), 55)
crocin1 = Medicine(2, "crocin", "cipla", 5, datetime(2023,3,18), datetime(2020,3,18), 75)

print(1+15)
print(1.5+2.5)
print("s"+"d")
print(True+False)
print([1,2]+[3,4])
# print(crocin + crocin1)
print(crocin)

# var = crocin > crocin1
# print(var)

s4 = s1+s3
print(s4)
print(type(s4))


# refere oop37 for polymarisation overloading example