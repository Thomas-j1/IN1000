"""
Opretter klassen motorsykkel med merke, registreringsnummer og kilometeravstand kjørt som instansvariabler.
"""

class Motorsykkel:

    def __init__(self, m, r, k): #konstruktør
        self._merke = m
        self._regnr = r
        self._km = k

    def kjor(self, km): #metode som øker kilomteravstand kjørt
        self._km+=km

    def hentKilometerstand(self): #metode som returnerer kilometeravstand kjørt
        return self._km

    def skrivUt(self): #metode som skriver ut all tilhørende data til objekt
        print(f"merke: {self._merke}\nRegistreringsnummer: {self._regnr}\nKilometerstand: {self._km}")
