from sang import Sang

class Spilleliste:

    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        fil = open(filnavn)
        count=0
        for linje in fil:
            bit = linje.strip().split(";")
            self._sanger.append(Sang(bit[1], bit[0]))

    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.remove(sang)

    def spillSang(self, sang):
            sang.spill()

    def spillAlle(self):
        for sang in self._sanger:
            sang.spill()

    def finnSang(self, tittel):
        finnes = False
        for sang in self._sanger:
            if sang.sjekkTittel(tittel):
                finnes = True
                return sang
        if finnes == False:
            return None

    def hentArtistUtvalg(self, artistnavn):
        egenListe = []
        for sang in self._sanger:
            if sang.sjekkArtist(artistnavn):
                egenListe.append(sang)
        return egenListe
