class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name}")

class Employee(Person):
    def __init__(self, name, age, title):
        Person.__init__(self, name, age)
        # lub super().__init__(name, age)
        self.title = title

    def charge_position(self, new_title):
        self.title = new_title

adam = Employee("Adam", 25, "technik it")
adam.introduce()
print(adam.title)

adam.charge_position("Kasjer")
print(adam.title)