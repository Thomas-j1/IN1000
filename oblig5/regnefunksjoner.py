"""
regnefuksjoner adderer, subtraherer, dividerer og konverterer fra tommer til cm
"""

def adder(tall1, tall2): #legger sammen to tall og returnerer disse
    return tall1+tall2

print(adder(3,7))

def substraksjon(tall1, tall2): #subtraherer to tall og returnerer disse
    return tall1-tall2

assert(substraksjon(10,5)==5)
assert(substraksjon(10,-5)==15)
assert(substraksjon(-10,-5)==-5)

def divisjon(tall1, tall2): #dividerer to tall og returnerer svar
    return tall1//tall2

assert(divisjon(10,2)==5)
assert(divisjon(10,-2)==-5)
assert(divisjon(-10,-2)==5)

def tommerTilCm(antallTommer): #konverterer fra tommer til cm
    assert(antallTommer>0)
    return antallTommer*2.54

print(tommerTilCm(10))

def skrivBeregninger(): #kaller på summerer, subtraherer og dividerer, og tommerTilCm konverterer
    tall1 = float(input("tall1 som skal beregnes: "))
    tall2 = float(input("tall2 som skal beregnes: "))

    print(f"Sum: {adder(tall1,tall2)}, differanse: {substraksjon(tall1,tall2)}, dividerte: {divisjon(tall1, tall2)}")

    tall3 = float(input("Konverter fra tommer til cm: "))
    print(f"resultat: {tommerTilCm(tall3)}")

skrivBeregninger()
