"""
Oppretter klassen Sang, med tilhørende instansvariabel og metoder
"""
import fnmatch

class Sang:

    def __init__(self, artist, tittel): #konstruktør
        self._tittel = tittel
        self._artist = artist

    def spill(self): #spiller sang
        print(f"Spiller {self._tittel} av {self._artist}")

    def sjekkArtist(self, navn): #returnerer True hvis deler av navn finnes i objekt
        ord = navn.split(" ")
        objektord = self._artist.split(" ")
        finnes = False
        for x in ord:
            if x in objektord:
                finnes = True
        if finnes:
            return True
        else:
            return False

    def sjekkTittel(self, tittel): #returnerer True hvis første 3/4 av tittel finnes i objekt, ellers false
        delAvOrd = int(len(tittel)/4) #ny int som er 1/4 av lengden på tittel
        likStrenge = tittel[0:-delAvOrd] + "*" #de første 3/4 av tittel
        if fnmatch.fnmatch(self._tittel.lower(), likStrenge.lower()): #Hvis de første 3/4 av tittel matcher tittel i objekt
            return True
        else:
            return False

    def sjekkArtistOgTittel(self, artist, tittel): #kaller på metodene sjekkTittel() og sjekkArtist(), og returnerer True hvis begge stemmer, ellers false
        if self.sjekkTittel(tittel) and self.sjekkArtist(artist):
            return True
        else:
            return False
