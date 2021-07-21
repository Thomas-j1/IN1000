"""
Klassen Spillebrett, med tilhørende konstruktør og metoder
"""
from random import randint
from celle import Celle

class Spillebrett:
    def __init__(self, rader, kolonner): #Konstruktør som lager brett, og kaller på _generer()
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = []
        self._generasjonsnummer = 0
        for i in range(rader):
            self._rutenett.append([])
            for j in range(kolonner):
                self._rutenett[i].append(Celle())
        self._generer()

    def tegnBrett(self): #lager utskrift av Spillebrett
        for rad in self._rutenett:
            for objekt in rad:
                print(objekt.hentStatusTegn(), " ", end="")
            print("\n")

    def oppdatering(self): #oppdaterer status på celle til neste generasjon
        giLiv = []
        giDod = []
        levende = 0

        for rad in range(len(self._rutenett)):
            for kolonne in range(len(self._rutenett[rad])):
                for i in self.finnNabo(rad, kolonne):
                    if i.erLevende(): #finner antall levende naboer
                        levende+=1

                if self._rutenett[rad][kolonne].erLevende(): #hvis celle er levende
                    if levende<2 or levende>3: #antall levende naboer
                        giDod.append(self._rutenett[rad][kolonne]) #legg til i giDod liste
                else: #hvis celle er død
                    if levende==3: #antall levende naboer
                        giLiv.append(self._rutenett[rad][kolonne]) #legg til i giLiv liste
                levende=0 #tilbakestiller antall levende naboer

        for i in giLiv: #setter status på alle celler i liste til levende
            i.settLevende()

        for i in giDod: #setter status på alle celler i liste til død
            i.settDoed()

        self._generasjonsnummer+=1

    def finnAntallLevende(self): #returnerer antall levende celler
        antallLevende = 0
        for rad in self._rutenett:
            for objekt in rad:
                if objekt.erLevende():
                    antallLevende+=1
        return antallLevende

    def _generer(self): #genererer generasjon 0 av Spillebrett
        for rad in self._rutenett:
            for objekt in rad:
                tilfeldig = randint(1, 3)
                if tilfeldig == 1:
                    objekt.settLevende()


    def finnNabo(self, rad, kolonne): #finner naboer til celle, og returnerer disse i en liste
        naboer = []


        for i in range(-1, 2):
            for j in range(-1, 2):
                naboRad = rad + i
                naboKolonne = kolonne + j

                gyldig = True

                if i == 0 and j == 0: #hvis samme posisjon som self celle
                    gyldig = False

                if naboRad < 0 or naboRad >= len(self._rutenett): #hvis innenfor spillebrett
                    gyldig = False

                if naboKolonne < 0 or naboKolonne >= len(self._rutenett[rad]): #hvis innenfor spillebrett
                    gyldig = False

                if gyldig:
                    naboer.append(self._rutenett[naboRad][naboKolonne]) #legg til celle i naboer liste

        return naboer
