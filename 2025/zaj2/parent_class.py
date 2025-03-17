class ParentClass:
    def printHello(self):
        print('Witaj, świecie!')

class ChildClass(ParentClass):
    def someNewMethod(self):
        print('Obiekty klasy ParentClass nie mają tej metody.')

class GrandchildClass(ChildClass):
    def anotherNewMethod(self):
        print('Tę metodę mają tylko obiekty klasy GrandchildClass.')

print('Utwórz obiekt klasy ParentClass i wywołaj jego metody:')
parent = ParentClass()
parent.printHello()

print('Utwórz obiekt klasy ChildClass i wywołaj jego metody:')
child = ChildClass()
child.printHello()
child.someNewMethod()

print('Utwórz obiekt klasy GrandchildClass i wywołaj jego metody:')
grandchild = GrandchildClass()
grandchild.printHello()
grandchild.someNewMethod()
grandchild.anotherNewMethod()
print('Błąd:')
parent.someNewMethod()