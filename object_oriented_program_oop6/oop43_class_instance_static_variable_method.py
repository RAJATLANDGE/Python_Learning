import datetime


class BankAccount:

    ROI = 3.5             #class variable = same for whole class

    def __init__(self, account_no, account_holder, balance, contact):
        self.account_no = account_no
        self.account_holder = account_holder
        self.balance = balance
        self.contact = contact
        self.passbook = True
        self.created = datetime.datetime.now()
        self.last_modified = datetime.datetime.now()

    def __str__(self):
        return f"{self.__dict__}"

    def balance_check(self):
        print(self.balance)

    def exact_balance(self):
        bal = self.balance + (self.balance * BankAccount.ROI) / 100
        print(bal)

# classmethod = (cls) generally use for access class variable,
# instancemethod = (self) generally use for access instance variable
# staticmethod = ()

    def update_passbok(self):
        self.last_modified = datetime.datetime.now()
        pass

    def withdraw(self, amount):                     #instance method
        if amount < self.balance:
            self.balance -= amount
            return "Please Collect Cash"
        else:
            "Insufficient Balance"

    def deposit(self, amount):                             #instance method  because when person deposit the money it applicable to only here account numbere thus it is instance method
        self.last_modified = datetime.datetime.now()
        self.balance += amount
        return self.balance

    @classmethod
    def update_roi(cls, new_roi):
        BankAccount.ROI = new_roi

    @staticmethod
    def sanitise():
        pass

    @staticmethod
    def show_last_modified(date):
        format = "%d-%m-%Y  %H:%M:%S"
        return date.strftime(format)

    
    

# variable in class are of two type
# 1 class variable      2 instance variable

ba1 = BankAccount(258963789, "Pankaj", 456982, 7896358245)
ba2 = BankAccount(587542269, "Nitin", 5887559, 8239756988)
print(ba1.contact)                           # ----- instance variable = value change for each object
print(ba1.account_holder)                    # ----- instance variable
print(ba1.balance)                           # ----- instance variable

print("------------------")

print(ba2.contact)                          #----- instance variable
print(ba2.account_holder)                    # ----- instance variable
print(ba2.balance)                           # ----- instance variable

ba2.check_book = True                        # assigning variable outside the class
ba2.credit_card = True
ba2.internation_transfer = True
print(ba1)
print(ba2)

print(BankAccount.ROI) # by this way always call class-variable ie by calling class, class variable we be access
ba1.exact_balance()
# ba1.ROI = 500  #do not call this way it can create variable of ROI in ba1
print(ba1)
ba1.exact_balance()
# when we access class variable with instance it check whether it has that attribute or not
# if it has that attribute it it does not have it then it will refer to the class level variable.

# print(ba2.DEBTROI)   #'BankAccount' object has no attribute 'DEBTROI'

BankAccount.update_roi(3.8)
print(BankAccount.ROI)

ba1.update_roi(3.9)
print(BankAccount.ROI)

print(BankAccount.show_last_modified(ba1.last_modified))
print(BankAccount.show_last_modified(datetime.datetime.now()))
print(ba1.show_last_modified(ba1.created))




