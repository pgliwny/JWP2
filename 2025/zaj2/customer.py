class BalanceError(Exception):
    pass

class Customer:
    def __init__(self, name, balance):
        if balance < 0 :
            raise BalanceError("Balance has to be non-negative!")
        else:
            self.name = name
            self.balance = balance

cust = Customer("Larry Torres", -100)

try:
    cust = Customer("Larry Torres", -100)
except BalanceError as Err:
    print("Error in call Customer()")
    print(Err)