# Access modifier =  it has three types
# 1) Public access modifier   - easily accessible from any part of the program.
# 2) Protected access modifier- should be only accessed in te class or in a class derived from it. denoted by "_" before name of class
# 3) Private access modifier  - should be accessed within the class only, it is the most secure access modifier. denoted by "__"
class TeslaCar:

    def __init__(self, model, engine, cylinder ):
        self.model = model
        self._engine = engine
        self.__cylinder = cylinder

    def __str__(self):
        return f"{self.__dict__}"

    def test_drive(self):                       # public access modifier
        pass

    def _open_engine(self):                     # protected access modifier
        pass

    def __repair_cylinder(self):                #private access modifier
        pass

    def open_cylinder(self):                     #private AM access only in own class.
        print(self.__cylinder)


class RegisteredDealer(TeslaCar):

    def __init__(self, model, engine, cylinder):
        super().__init__(model, engine, cylinder)

    def change_engine(self,new):                   # protected AM always access only in child class
        self._engine = new

    def disply_engine(self):
        print(self._engine)



model_X =TeslaCar(2020, "V4", 1000)
print(model_X)

print(model_X.model)    # public methode access anywhere and change its value
model_X.model = 2022
print(model_X.model)

rd = RegisteredDealer(2020, "V4", 1000)
rd.change_engine("v6")
rd.disply_engine()

model_X.open_cylinder()

model_X._engine = "v8"                   # protected and private access in anywhere but convention told that do not do this
print(model_X._engine)

model_X._Teslacar__cylinder = 2000
print(model_X._Teslacar__cylinder)






