"""
Oppretter klassen hund, med alder, vekt og metthet som instansvariabler
"""

class Hund:

    def __init__(self, a, v): #konstruktør med alder, vekt og metthet
        self._alder = a
        self._vekt = v
        self._metthet = 10

    def faaAlder(self): #returnerer alder
        return self._alder

    def faaVekt(self): #returnerer vekt
        return self._vekt

    def spring(self): #minker metthet og vekt
        self._metthet-=1
        if self._metthet<5:
            self._vekt-=1

    def spis(self, mengde): #øker metthet og vekt
        self._metthet+=mengde
        if self._metthet>7:
            self._vekt+=1
