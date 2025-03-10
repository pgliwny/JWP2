class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            text = f.readlines()
            name = text[0].split()[0]
            salary = text[0].split()[1]
        return cls(name, salary)


emp = Employee.from_file("salary_data.txt")
print(emp.name, emp.salary)
