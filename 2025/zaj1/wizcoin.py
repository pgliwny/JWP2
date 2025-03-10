class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """Tworzy nowy obiekt Wizcoin z monetami: knutami, syklami, galeonami."""
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
    def value(self):
        """Wartość (w knutach) wszystkich monet w tym obiekcie WizCoin."""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)
    def weightInGrams(self):
        """Zwraca wagę monet w gramach."""
        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)