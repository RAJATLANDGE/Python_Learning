# MRO  =  Method Resolution ORDER-- it is an order which determines which method to execute in case of inheritance.
# MRO Order is determine by C3 Algorithem


class O:
    pass

class F(O):
    pass

class E(O):
    pass

class D(O):
    pass

class C(D,F):
    pass

class B(D,E):
    pass

class A(B,C):
    pass

a = O()
print(help(a))
b = D()
print(help(b))
c = E()
print(help(c))
d = F()
print(help(d))
e = B()
print(help(e))
f = C()
print(help(f))
g = A()
print(help(g))

'''
MRO(class): classname + merge(MRO(immediate parents ),list of immediate parents)

MRO(O)= O + merge(MRO(builtins.object), builtins.object)
      = O +  merge(builtins.object, builtins.object)
      = O + builtins.object
      = O

MRO(D)= D + merge(MRO(O),O)
      = D + merge(O,O)
      = D + O
      = DO


MRO(E)= E + merge(MRO(O),O)
      = E + merge(O,O)
      = E + O
      = EO

MRO(F)= F + merge(MRO(O),O)
      = F + merge(O,O)
      = F + O
      = FO
      
MRO(B)= B + merge(MRO(D,E),DE)    DO, head= D and tail = O 
      = B + merge(DO,EO,DE)        EO, head= E and tail = O 
      = B + D + merge (O,EO,E)
      = BD + E + merge(O,O)
      = BDEO

MRO(C)= C + merge(MRO(D,F),DF)    DO, head= D and tail = O 
      = C + merge(DO,FO,DF)        FO, head= F and tail = O 
      = C + D + merge (O,FO,F)      
      = CD + F + merge(O,O)
      = CDFO

MRO(A)= A + merge(MRO(B,C),BC)    BDEO, head= B and tail = DEO 
      = A + merge(BDEO,CDFO,BC)        CDFO, head= C and tail = DFO 
      = A + B + merge (DEO,CDFO,C)      D is in tail of CDFO hence next CDFO
      = AB +merge(DEO,CDFO,C)
      = AB + C + merge(DEO, DFO)
      = ABC +D + merge(EO,FO)
      = ABCD + E + merge(O,FO)
      = ABCDE + F + merge(O,O)
      = ABCDEFO
'''





















