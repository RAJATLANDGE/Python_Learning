# if birds looks like a duck, walks like a duck, swims like a duck and quack likes a duck then it is a duck.

# looks = attribute
# walks, swims, quack  = behaviour


class Maharashtrian:

    def speak_in_marathi(self):
        pass

    def speak_in_hindi(self):
        print("i am from maharashtra and talk in hindi")

class Gujrati:

    def speak_in_gujrati(self):
        pass

    def speak_in_hindi(self):
        print("i am from gujrat and talk in hindi")


def speak_in_hindi(obj):
    obj.speak_in_hindi()

m1 = Maharashtrian()
g1 = Gujrati()

speak_in_hindi(m1)
speak_in_hindi(g1)

class Bird:
    def fly(self):
        print("fly with wings")

class Airplane:
    def fly(self):
        print("fly with fuel")

class Fish:
    def swim(self):
        print("fish swim in sea")

for obj in Bird(),Airplane(),Fish():
    obj.fly()