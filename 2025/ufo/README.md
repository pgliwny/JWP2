# 🛸 UFO Area Calculator

**UFO Area Calculator** to biblioteka Python przeznaczona do szybkiego obliczania powierzchni całkowitej statku kosmicznego typu UFO. Obliczenia uwzględniają podstawowe wymiary pojazdu oraz opierają się na funkcjach biblioteki `numpy`.

---

## 🚀 Instalacja

Aby zainstalować bibliotekę lokalnie, uruchom polecenie:

```bash
pip install .

lub w trybie edytowalnym (zalecane podczas rozwoju):


pip install -e .

🔧 Użycie
Przykładowy program demonstrujący działanie biblioteki:

import ufo_area

# Podaj wymiary statku UFO w metrach
wysokosc = 5.0
szerokosc = 12.0
promien = 3.5

# Oblicz powierzchnię
powierzchnia = ufo_area.get_area(wysokosc, szerokosc, promien)

print(f"Powierzchnia całkowita UFO: {powierzchnia:.2f} m²")

Przykładowy wynik działania programu:

Powierzchnia całkowita UFO: 239.37 m²

📦 Wymagania
Python >= 3.8
numpy >= 1.26 (instalowany automatycznie)

📂 Struktura pakietu

ufo_area/
├── setup.py
├── README.md
└── ufo_area/
    ├── __init__.py
    └── UFO.py
    
📝 Autor
Pawel Gliwny
📧 pawel.gliwny@przyklad.com









