import random
import fnmatch
import simpleaudio as sa
import time

class Sang:

    def __init__(self, artist, tittel, filnavn):
        self._tittel = tittel
        self._artist = artist
        self._filnavn = filnavn

    def spill(self):
        wave_obj = sa.WaveObject.from_wave_file(self._filnavn)
        play_obj = wave_obj.play()
        time.sleep(8)
        #play_obj.stop()
        play_obj.wait_done()

    def sjekkArtist(self, navn):
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

    def sjekkTittel(self, tittel):
        delAvOrd = int(len(tittel)/4) #ny int som er 1/4 av lengden på tittel
        likStrenge = tittel[0:-delAvOrd] + "*" #de første 3/4 av tittel
        if fnmatch.fnmatch(self._tittel.lower(), likStrenge.lower()): #Hvis de første 3/4 av tittel matcher tittel i objekt
            return True
        else:
            return False

    def sjekkArtistOgTittel(self, artist, tittel):
        if self.sjekkTittel(tittel) and self.sjekkArtist(artist):
            return True
        else:
            return False
