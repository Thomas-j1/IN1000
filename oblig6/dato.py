"""
oppretter klassen dato, lager strenge av dato, sjekker dag, og forhold mellom datoer
"""

class Dato:

    def __init__(self, nyDag, nyMaaned, nyttAar): #konstruktør med dag, måned og år
        self._dag = int(nyDag)
        self._maaned = int(nyMaaned)
        self._aar = int(nyttAar)

    def hentAar(self): #skriver ut år
        return self._aar

    def datoStreng(self): #lager strenge av dato
        streng = f"{self._dag}/{self._maaned}/{self._aar}"
        return streng

    def erDag(self, dagen): #sjekker om dato er dag
        if self._dag == dagen:
            return True
        else:
            return False

    def forEtter(self, nyDato): #sjekker om dato er før eller etter
        gammelDato = 0
        if self._maaned<10 and self._dag<10: #lager sammenlignbart int
            gammelDato = int(f"{self._aar}0{self._maaned}0{self._dag}")
        elif self._maaned<10:
            gammelDato = int(f"{self._aar}0{self._maaned}{self._dag}")
        elif self._dag<10:
            gammelDato = int(f"{self._aar}{self._maaned}0{self._dag}")

        if gammelDato<nyDato:
            print("Dato er etter")
        elif gammelDato>nyDato:
            print("Dato er før")
        else:
            print("Datoene er like")
