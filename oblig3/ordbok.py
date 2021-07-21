"""
Ordbok over varer, med flyttall
"""

varer = {
"melk": 14.90,
"brød": 24.90,
"yoghurt": 12.90,
"pizza": 39.90
}

print(varer)

leggTilVare1 = input("Legg til vare: ")
leggTilPris1 = float(input("pris på vare(00.00): "))
leggTilVare2 = input("Legg til vare: ")
leggTilPris2 = float(input("pris på vare(00.00): "))

varer[leggTilVare1]=leggTilPris1 #legger til vare sammen med pris i ordbok
varer[leggTilVare2]=leggTilPris2 #legger til vare sammen med pris i ordbok

print(varer)
