class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class B:
    def __init__(self,c,d):
        self.c = c
        self.d = d

class C:
    def __init__(self,e,f):
        self.e = e
        self.f = f

class D(A,B,C):
    def __init__(self,a,b,c,d,e,f,g,h):
        self.g = g
        self.h = h
        A.__init__(self,a,b)
        B.__init__(self,c,d)
        C.__init__(self,e,f)

    def __str__(self):
        return f"{self.__dict__}"




# ---------------------------------

database = []


class CreatObject:

    def create(self, obj):
        database.append(obj)

class ReadObject:

    def read(self, id):
        for item in database:
            if item.id == id:
                return item

class DeleteObject:

    def delete(self, id):
        for item in database:
            if item.id == id:
                database.remove(item)

class UpdateObject:

    def update(self, id, obj):
        pass

class ProductCR(CreatObject, ReadObject):
    pass

class ProductDRU(DeleteObject, ReadObject, UpdateObject):
    pass


pcr = ProductCR()
pcr.read(1)
pcr.create("123")

pdru = ProductDRU()
# pdru.delete()
# pdru.read()
# pdru.update()


class India:
    def export_spices(self):
        pass

class Israel:
    def export_agritech(self):
        pass

class Africa(India, Israel):
    pass


# -----------------------------

class A:
    pass

class B(A):
    pass

class C(B):
    pass

class D:
    pass

class E(C, D):
    pass

# --------------------------


# class A:                                #TypeError: Cannot create a consistent method resolution
#     pass                                #order (MRO) for bases A, B, C
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(A, B, C):
#     pass
#
# d = D()





































