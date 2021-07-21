"""
Legg til tallene fra 0-100 i en liste med en løkke, bruk så en løkke til å lage en ny liste som er liste1 baklengs, uten å bruke reversed(). Skriv så ut liste 2 med en løkke.
"""

liste = []
liste2 = []

for i in range(0, 101): #legger inn tallene 0-100 i en liste
    liste.append(i)

lengde = len(liste)-1
for i in liste: #lager ny liste2 som er liste baklengs
    liste2.append(lengde-i)

for i in liste2: #skriver ut liste2
    print(i)
