"""
funksjon som legger sammen tall, og funksjon som skriver ut hvor mange ganger en bokstav forekommer i et ord
"""

def adder (tall1, tall2): #adderer to tall
    res = tall1 + tall2
    return res

addert1 = adder(10, 5)
addert2 = adder(25, 75)
print(f"10 + 5 = {addert1}, 25 + 75 = {addert2}")

tekststreng = input("Skriv inn tekststreng: ")
bokstav = input("Skriv inn bokstav: ")

def tellForekomst(minTekst, minBokstav): #teller antall ganger en bokstav forekommer i en strenge
    count = 0
    for i in minTekst:
        if i==minBokstav:
            count+=1
    return count

print(f"bokstaven {bokstav}, forekommer {tellForekomst(tekststreng, bokstav)} ganger i {tekststreng}")
