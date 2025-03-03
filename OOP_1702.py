


# Python program to create Bankaccount class
# with both a deposit() and a withdraw()
class Bank_Account:
    def __init__(self, balance, costumer, id):
        self.balance = balance
        self.costumer = costumer
        self.id = id


    def withdraw(self, amount):
            if self.balance - amount > 0:
                print('Successfully withdraw')
                self.balance -= amount
            return amount

    def deposit(self, amount):
        amount = abs(amount)
        self.balance += amount

    def __str__(self):
        return f'good morning {self.costumer} your balance:{self.balance}₪' \
               f' in {self.id} account'

class Checking_Account(Bank_Account):
    def __init__(self, balance, costumer, id, overdraft):
        super().__init__(costumer, balance, id)
        self.overdraft()

class Loan_Account(Bank_Account):
    def __init__(self, balance, costumer, id):
        super().__init__(costumer, -balance, id) #negetive balance
        self.debt = balance




class SavingAccount(Bank_Account):
    def __init__(self, balance, costumer, intrest_rate):
        super().__init__(costumer, balance, id) #negetive
        self.intrest_rate = intrest_rate\

    def add_intrest(self, intrest, intrest_rate):
        self.intrest = balance * self.intrest_rate

acc1 = Bank_Account(0, 'chen', '29897')
print(acc1)
acc1.deposit(int(input('enter the deposit : ')))
print(acc1)
acc1.withdraw(155)
print(acc1)







