import numpy as np

def get_area(h, w, r):
    """
    Oblicza powierzchnię statku kosmicznego UFO.

    :param h: wysokość (metry)
    :param w: szerokość (metry)
    :param r: promień podstawy (metry)
    :return: powierzchnia całkowita (metry kwadratowe)
    """
    # powierzchnia podstawy (koło)
    base_area = np.pi * r**2

    # powierzchnia boczna (elipsoida)
    side_area = 2 * np.pi * r * np.sqrt(((w / 2)**2 + h**2) / 2)

    total_area = base_area + side_area
    return total_area