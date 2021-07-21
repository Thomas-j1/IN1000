"""
Funksjoner som teller bokstaver i ord og lager ordbok av en setning med forekomst av ord. Tar så innput fra bruker, å tar i bruk funksjonene 
"""

def bokstaverIOrd(ord): #teller antall bokstaver i et ord
    count = 0
    for i in ord:
        count+=1

    return count

def ordISetning(tekst): #lager en ordbok av ord i en setning, med hvor mange forekomster det er av hvert ord
    dict = {}
    ordene = tekst.split()
    for i in ordene:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    return dict

setning = input("Skriv inn en setning: ")
forekomstAvOrd = ordISetning(setning.lower())

print(f"Det er {len(forekomstAvOrd)} ord i setningen din.")
for i in forekomstAvOrd:
    print(f"ordet {i}, forekommer {forekomstAvOrd[i]} ganger, og har {bokstaverIOrd(i)} bokstaver")
