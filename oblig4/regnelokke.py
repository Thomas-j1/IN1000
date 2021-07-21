"""
While løkke til å skrive inn tall i liste, for løkker for å printe liste, summen av liste og største og minste tall i liste
"""

fortsett = True
liste = []
while fortsett == True: #skriver inn tall i liste til bruker skriver inn 0
    tall = int(input("Skriv inn tall: "))

    if tall == 0:
        fortsett = False
    else:
        liste.append(tall)

for i in liste: #skriver ut liste
    print(i)

minSum = 0
for j in liste: #finner summen av liste
    minSum+=j

print(f"Summen av tall er {minSum}")

storst = liste[0]
for k in liste: #finner største tallet i liste
    if k>storst:
        storst = k

print(f"Det største tallet er {storst}")

minst = liste[0]
for l in liste: #finner minste tallet i liste
    if l<minst:
        minst=l

print(f"Det minste tallet er {minst}")
