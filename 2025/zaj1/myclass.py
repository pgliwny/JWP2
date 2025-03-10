class MyClass:
    licznik = 0

    def __init__(self):
        MyClass.licznik += 1

    @classmethod
    def ile_obiektow(cls):
        return (f"Liczba utworzonych obiektów:"
                f" {cls.licznik}")
obj1 = MyClass()
obj2 = MyClass()

print(MyClass.ile_obiektow())

