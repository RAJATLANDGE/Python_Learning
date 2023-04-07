from abc import ABC, abstractmethod
from oop50_BANK import Bank


class RBI(ABC):

    @abstractmethod
    def withdraw(self, acc_no, amount):
        pass

    @abstractmethod
    def deposit(self, acc_no, amount):
        pass

    @abstractmethod
    def provide_account(self, acc_no, name, balance, contact):
        pass

    @abstractmethod
    def provide_passbook(self):
        pass

    def provide_loan(self):
        pass


class ICICI(RBI):

    accounts = []
    min_balance = 1000

    def get_accounts(self, acc_no):
        for account in ICICI.accounts:
            if account.acc_no == acc_no:
                return account

    def withdraw(self, acc_no, amount):
        account = self.get_accounts(acc_no)
        if account:
            bal =  account.balance - amount
            if bal < ICICI.min_balance:
                print("You are crossing minimum balance limit")
            if bal <= 0:
                return {"Error Message": "Insufficient Fund"}
            else:
                return {"Status": "Amount Withdraw"}

        else:
            return {"Error Message": "Not Exists"}


    def deposit(self, acc_no, amount):
        pass

    def provide_account(self, acc_no, name, contact):
        ICICI.accounts.append(Bank(acc_no, name,1000, contact))

    def provide_passbook(self):
        pass

    def online_banking(self):
        pass

    def credit_card(self):
        pass

    def foreign_exchange(self):
        pass


class HDFC(RBI):

    accounts = []
    min_balance = 500

    def get_accounts(self, acc_no):
        for account in HDFC.accounts:
            if account.acc_no == acc_no:
                return account

    def withdraw(self, acc_no, amount):
        account = self.get_accounts(acc_no)
        if account:
            bal = account.balance - amount
            if bal < HDFC.min_balance:
                return {"Error Message":"Insufficient Funds"}
            else:
                return {"Status":"Amount Withdrawn"}


        else:
            acc_no = input("enter account number")
            name = input("enter account holder name")
            contact = input("enter contact number")
            HDFC.accounts.append(Bank(acc_no, name, 500, contact))

    def deposit(self, acc_no, amount):
        pass

    def provide_account(self, acc_no, name, contact):
        HDFC.accounts.append(Bank(acc_no, name, 500, contact))

    def provide_passbook(self):
        pass



ici = ICICI()

ici.provide_account(1, "LMN", 12345)
print(ICICI.accounts)

hdf = HDFC()
hdf.provide_account(1, "PQR", 12345)
print(HDFC.accounts)


