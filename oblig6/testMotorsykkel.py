"""
tester motorsykkel klasse, med opprettelse av objekter og testing av metoder
"""

from motorsykkel import Motorsykkel

def hovedprogram():
    motorsykkel1 = Motorsykkel("merke1", "RE123", 10)
    motorsykkel2 = Motorsykkel("merke2", "RE345", 20)
    motorsykkel3 = Motorsykkel("merke3", "RE567", 30) #oppretter tre motorosykkel objekter

    motorsykkel1.skrivUt()
    motorsykkel2.skrivUt()
    motorsykkel3.skrivUt() #skriver ut all data til objekter

    motorsykkel3.kjor(10) #øker kilomteravstand til tredje objekt
    print(motorsykkel3.hentKilometerstand()) #skriver ut kilomteravstand til tredje objekt

hovedprogram()
