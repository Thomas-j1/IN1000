"""
Oppretter klassen Spilleliste, med tilhørende instansvariabel og metoder
"""

from sang import Sang

class Spilleliste:

    def __init__(self, listenavn): #konstruktør
        self._sanger = [] #liste med objekter
        self._navn = listenavn

    def lesFraFil(self, filnavn): #lager sang objekter fra tittel og artist i fil
        fil = open(filnavn)
        count=0
        for linje in fil:
            bit = linje.strip().split(";")
            self._sanger.append(Sang(bit[1], bit[0]))

    def leggTilSang(self, nySang): #legger til sang objekt i spilleliste
        self._sanger.append(nySang)

    def fjernSang(self, sang): #fjerner sang objekt fra spilleliste
        if sang in self._sanger:
            self._sanger.remove(sang)

    def spillSang(self, sang): #kaller på metode spill() fra sang klasse for objekt
            sang.spill()

    def spillAlle(self): #spiller alle sanger i spilleliste
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, tittel): #returnerer True om sang er i liste, ellers False
        finnes = False
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                finnes = True
                return sang
        if finnes == False:
            return None

    def hentArtistUtvalg(self, artistnavn): #Finner alle objekter i spilleliste med artist, og returnerer liste med disse
        egenListe = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                egenListe.append(sang)
        return egenListe
