class A:
    def display(self):
        pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(B):
    pass

class F(C):
    pass

class G(C):
    pass

g = G()
g.display()

d = D()
d.display()

c = C()
c.display()

# -----------------

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class Z(B, C):
    pass

class K(B):
    pass

k = K()

z = Z()

# -----------------------

class Product:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        pass

    def display_product(self):
        return f"{self.__dict__}"

class Electronics(Product):

    def __init__(self, id, name, voltage):
        self.voltage = voltage
        super().__init__(id, name)

class Digital(Electronics):
    pass

class AC(Electronics):
    pass

class Chemical(Product):
    pass

class Cosmatic(Product):
    pass

class Motor(Product):

    def __init__(self, id, name, power):
        self.power = power
        super().__init__(id, name)

class HouseHold(Motor):

    def __init__(self, id, name, power, weight):
        self.weight = weight
        super().__init__(id, name, power)

class Industrial(Motor):

    def __init__(self, id, name, power, weight):
        self.weight = weight
        super().__init__(id, name, power)

class Hydrolic(Industrial):
    pass

class Diesel(Industrial):
    pass

d = Diesel()
d.display_product()