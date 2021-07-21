"""
testing av klassen hund, ved metodene spring, faaVekt og spis
"""
from hund import Hund

def hovedprogram():
    hundeobjekt1 = Hund(3, 15) #lager objekt
    print(hundeobjekt1.faaVekt()) #skriver ut vekt

    for i in range(6):
        hundeobjekt1.spring() #kaller på metoden spring(senker metthet/vekt)
        print("springer")
        print(hundeobjekt1.faaVekt())

    for i in range(3):
        hundeobjekt1.spis(3) #kaller på metoden spis(øker metthet/vekt)
        print("spiser")
        print(hundeobjekt1.faaVekt())

hovedprogram()
