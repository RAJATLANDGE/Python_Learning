# user define exception or customized exception or programmatic exception


class TooYoungException(Exception):

    def __init__(self, message):
        self.message = message


class Matrimony:

    def __init__(self,name, age, gender):
        self.name = name
        if (gender == "M" and age<23) or (gender == "F" and age <21):
            raise TooYoungException("You are too young to registered in Matrimony")
        else:
            print("successfully registered for matrimony site")
        self.age = age
        self.gender =  gender

Robin = Matrimony("Robin", 50,"M")
# Games = Matrimony("Games", 14, "M")
Natasha = Matrimony("Natasha", 22, "F")
try:
    Sonu = Matrimony("Sonu", 15, "F")
except TooYoungException as tye:
    print(tye.message)

