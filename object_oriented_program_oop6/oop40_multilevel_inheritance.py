

class College:

    auditorium = ""
    ground = ""

    def book_auditorium(self):
        pass

    def book_ground(self):
        pass

class EngineerDept(College):

    library = ""

    def book_library(self):
        pass

class ITDept(EngineerDept):

    lab = ""

    def book_lab(self):
        pass

class FirstYear(ITDept):
    pass


# --------------------------------


class CentralGovernment:

    health_funds = 0
    security_funds = 0

    def deploy_security(self):
        pass

    def approve_healthfunds(self):
        pass

class StateGovernment(CentralGovernment):

    def pwd(self):
        pass

class MahanagarPalika(StateGovernment):

    def zilla_parishad(self):
        pass

class NagarPalika(MahanagarPalika):
    pass

class GramPanchyat(NagarPalika):
    pass


gp = GramPanchyat()

print(gp.health_funds)



class A:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class B(A):
    def __init__(self,c,d):
        self.c = c
        self.d = d
        A.__init__(self,a,b)

class C(B):
    def __init__(self,e,f):
        self.e = e
        self.f = f
        A.__init__(self,a,b)
        B.__init__(self,c,d)


c = C()
