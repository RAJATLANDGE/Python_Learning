

class Medicine:

    def __init__(self,mid, name, manufacturer, price, exp_date, mfg_date, qty ):
        self.mid = mid
        self.name = name
        self.manufacturer = manufacturer
        self.price = price
        self.exp_date = exp_date
        self.mfg_date = mfg_date
        self.qty = qty

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)

    # def __add__(self, other):                        # from this and below function we can attain operator overloading
    #     self.qty = self.qty + other.qty
    #
    # def __sub__(self, other):
    #     pass
    #
    # def __mul__(self, other):                       # multiplication
    #     pass
    #
    # def __divmod__(self, other):                   #
    #     pass
    #
    # def __mod__(self, other):
    #     pass
    #
    # def __truediv__(self, other):                       #division
    #     pass
    #
    # def __gt__(self, other):                           # greater than
    #     if self.qty > other.qty and self.exp_date > other.exp_date:
    #         return True
    #     return False
    #
    #
    # def __lt__(self, other):                          # less than
    #     pass
    #
    # def __ge__(self, other):                          # greter than equal to
    #     pass
    #
    # def __le__(self, other):                          # less than equal to
    #     pass
    #
    # def __len__(self):                                # length
    #     pass

# refere oop37