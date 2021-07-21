"""
tester dato.py, ved metodene erDag, datoStreng, hentAar og forEtter.
"""
from dato import Dato

def hovedprogram():
    dato2 = Dato(15, 2, 1990) #lager objekt

    print(f"{dato2.hentAar()}") #skriver ut år til objekt

    if dato2.erDag(15): #sjekker om dag i objekt er 15
        print("Loenningsdag!")
    elif dato2.erDag(1): #^om dag er 1
        print("Ny maaned, nye muligheter.")

    dato = dato2.datoStreng() #lagrer dato i lesbar streng
    print(dato)

    valid = False
    while valid != True: #sålenge nydato er skrevet (aaaammdd)
        nyDato = int(input("skriv inn Dato(aaaammdd): "))
        if len(str(nyDato))==8:
            valid=True
        else:
            print("Ugyldig input, (aaaammdd)")
    dato2.forEtter(nyDato) #sammenligner dato med objekt

hovedprogram()
