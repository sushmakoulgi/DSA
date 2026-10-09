from abc import ABC, abstractmethod

class IAccount(ABC):

    @abstractmethod
    def deposit(self,amount):
        pass


from collections import deque

class Account(IAccount):

    def __init__(self, accountnumber:int,amount:int):
        self.accountnumber=accountnumber
        self.balance=amount
        self.log={}

    def deposit(self,amount,t):
        if amount>0:
            self.balance=self.balance+amount
        self.log_history(t,amount)

    def log_history(self,t,amout):
        self.log[t]=f"deposited {amout}"

    def __str__(self) -> str:
        return f"{self.accountnumber}--> {self.balance}"

    def transaction_history(self,number:int):
        top_keys=sorted(self.log.keys(),reverse=True)[:number]
        for key in top_keys:
            print(f"at timestamp {key} ---> {self.log[key]} ")



acc=Account(1,100)
acc.deposit(200,1)
acc.deposit(100,2)
acc.deposit(30,4)
acc.deposit(1,5)

print(acc.balance)
print(str(acc))

acc.transaction_history(2)