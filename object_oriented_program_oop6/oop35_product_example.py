

class Product:

    def __init__(self, pid: int, pname: str, mfg: str, price: float, qty: int, categoary: str, warranty : int =0):
        """

        :param pid:
        :param pname:
        :param mfg:
        :param price:
        :param qty:
        :param categoary:
        :param warranty:
        """
        self.pid = pid
        self.product_name = pname
        self.manufacturer = mfg
        self.cost = price
        self.quantity = qty
        self.category = categoary
        self.warranty = warranty

    def __str__(self):                     #"help to display the string representation of the object "
        # return f"Product id :- {self.pid}\nProduct Name :- {self.product_name}\nProduct Manufacturer :- {self.manufacturer}\n" \
        #        f"Product cost :- {self.cost}\nQuantity :- {self.quantity}\nProduct Category :- {self.category}\nWarranty :- {self.warranty}"
        return f"{self.__dict__}"
        # return f"{self.pid}---> {self.product_name}---> {self.manufacturer}"

    def __repr__(self):                    # "help to display the object
        return str(self)


iron = Product(pid=1, pname="steam iron", mfg="Bajaj", price=1250, qty=10, categoary="electric")
print(iron.product_name)
print(iron.manufacturer)
print(iron)


# CRUD = create read update delete
