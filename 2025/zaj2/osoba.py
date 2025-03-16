class Osoba:
    def __init__(self, name):
        self.name = name

    def przedstaw_sie(self):
        return f"Nazywam się {self.name}."

class Pracownik:
    def __init__(self, stanowisko):
        self.stanowisko = stanowisko

    def opis_pracy(self):
        return f"Pracuję jako {self.stanowisko}."

class Menedzer(Osoba, Pracownik):  # Dziedziczenie po dwóch klasach
    def __init__(self, name, stanowisko, zespol):
        Osoba.__init__(self, name)
        Pracownik.__init__(self, stanowisko)
        self.zespol = zespol

    def przedstaw_sie(self):
        return f"{super().przedstaw_sie()} Pełnię rolę {self.stanowisko}."

# Testowanie klasy Menedżer
menedzer = Menedzer("Anna Kowalska", "Kierownik", "Zespół IT")
print(menedzer.przedstaw_sie())  # "Nazywam się Anna Kowalska. Pełnię rolę Kierownik."
print(menedzer.opis_pracy())  # "Pracuję jako Kierownik."

print(Menedzer.mro())