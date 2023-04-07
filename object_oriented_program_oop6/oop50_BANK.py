

class Bank:

    def __init__(self, acc_no, name, balance, contact):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.contact = contact

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)

