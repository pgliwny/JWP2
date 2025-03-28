def dodaj(a,b):
 return a+b

def odejmij(a,b):
    wynik=a-b
    return wynik

def czyParzysta(liczba):
    if liczba%2==0:
        return True
    else:
        return False

liczba1=10
liczba2 =5

print("Dodawanie:",dodaj(liczba1,liczba2))
print("Odejmowanie:",odejmij(liczba1,liczba2))

if czyParzysta(liczba1):
  print(f"{liczba1} jest parzysta")
else:
      print(f"{liczba1} jest nieparzysta")
