"""
Lager lister, slår dem sammen, legger til liste og endrer lister
"""
liste = [3, 2, 3]

liste.append(4) #legger til 4 i slutten av liste

print(liste[0])
print(liste[2])

navneliste = []

def leggtilnavn(): #legger til navn i navneliste
    navn = input("Legg til navn i liste: ")
    navneliste.append(navn)

for x in range(4): #kjører leggtilnavnprosedyre 4 ganger
    leggtilnavn()

if "thomas" in navneliste: #sjekker om navneliste inneholder verdi
    print("Du husket meg!")
else:
    print("Glemte du meg?")

tall1 = sum(liste) #summerer liste

tall2=1
for x in liste: #skriver ut produkt av liste
    tall2=tall2*x

liste2=[]
liste2.append(tall1)
liste2.append(tall2)

liste3=liste+liste2
print(liste3)

del liste3[-1]
del liste3[-1]

print(liste3)
