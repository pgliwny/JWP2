class Customer:
    def __init__(self, name, acc_id):
        self.name = name
        self.acc_id = acc_id

    def __eq__(self, other):
        print("__eq__() is called")
        return (self.acc_id == other.acc_id) and (self.name == other.name)

    def __repr__(self):
        return f"Customer('{self.name}', {self.acc_id})"

    def __str__(self):
        cust_string = f"""
            Customer:
                    Name: {self.name},
                    Id: {self.acc_id}.
                    """
        return cust_string

customer1 = Customer("Maryam Azar", 123)

customer2 = Customer("Maryam Azar", 123)

print(customer1)
print(customer2)
print(customer1 == customer2)