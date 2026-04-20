class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")

    def get_balance(self):
        return self.__balance


account1 = BankAccount("Ahsan",1000)
account2 = BankAccount("Fazeel",600)

account1.deposit(1000)
account1.withdraw(400)

account2.deposit(300)
account2.withdraw(100)

print(f"Ahsan's balance: {account1.get_balance()}")
print(f"Fazeel's balance: {account2.get_balance()}")
