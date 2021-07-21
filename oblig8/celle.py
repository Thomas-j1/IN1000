"""
Klassen celle, med tilhørende konstruktør og metoder
"""

class Celle:
    def __init__(self): #Konstruktør med status paa celle
        self._status = "død"

    def settDoed(self): #Endre status til død
        self._status = "død"

    def settLevende(self): #Endre status til levende
        self._status = "levende"


    def erLevende(self): #Hente status på celle
        return self._status == "levende"

    def hentStatusTegn(self): #Hent tegn til spillebrett
        if self.erLevende():
            return "O"
        else:
            return "."
