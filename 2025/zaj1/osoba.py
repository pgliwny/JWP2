class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

    def __str__(self):
        return f"{self.imie}, lat {self.wiek}"

    def __repr__(self):
        return f"Osoba('{self.imie}', {self.wiek})"

osoba = Osoba("Paweł", 30)
print(osoba)       # __str__: Paweł, lat 30
print(repr(osoba)) # __repr__: Osoba('Paweł', 30)
