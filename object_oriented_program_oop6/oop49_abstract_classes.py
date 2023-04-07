from abc import ABC                   # abc = module = abstract base class   ABC = Class
from abc import abstractmethod

class A(ABC):

    @abstractmethod
    def method_one(self, params):
        pass

    @abstractmethod
    def method_two(self, params):
        pass

    def method_third(self):
        pass

# a = A()     Can't instantiate abstract class A with abstract methods method_one, method_two
# we cannot make object of abstract class
#if we want to make a object then first we want to make subclass of abstract class and then we can make the object of that method.
# if we derive a class from abstract class then all the abstract-method of the abstract class compulsory to implemented.
class B(A):

    def method_one(self, params):
        pass

    def method_two(self, params):
        pass

b = B()