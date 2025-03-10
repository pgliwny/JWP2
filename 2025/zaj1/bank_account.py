class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.owner, self.balance + other.balance)

    def __str__(self):
        return f"Konto ({self.owner}, saldo: {self.balance} PLN)"

    def __repr__(self):
        cust_string = f""" 
            Owner: {self.owner}\n
            Balance: {self.balance}.
        """
        return cust_string

    def __eq__(self, other):
        print("__eq__() jest wywoływane!")
        return (self.acc_id == other.acc_id) and (self.owner == other.owner)

# Tworzenie obiektów
acc1 = BankAccount("Jan", 5000, 12)
acc2 = BankAccount("Jan", 3000, 13)

print(acc1)
acc1

# Suma dwóch kont
acc3 = acc1 + acc2
print(acc3)  # Konto Jan, saldo: 8000 PLN
