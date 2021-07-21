"""
nøstet reiseplan liste hvor bruker skriver inn sted, klesplag og dato. bruker kan så søke opp i listen
"""
steder = []
klesplagg = []
avreisedato = []

for i in range(5): #legger til sted, klesplagg og avreisedato i egne lister 5 ganger
    sted = input("Skriv inn sted: ")
    klaer = input("Skriv inn klesplagg: ")
    dato = input("Skriv inn avreisedato(mmdd): ")
    steder.append(sted)
    klesplagg.append(klaer)
    avreisedato.append(dato)

reiseplan = steder, klesplagg, avreisedato #kombinerer lister

for i in reiseplan:
    print(i)

i1 = int(input(f"Skriv inn plass i reiseplan(0-{len(reiseplan)-1}): ")) #søker opp i reiseplan liste
if i1>=0 and i1<=len(reiseplan)-1:
    i2= int(input(f"Skriv inn plass i liste(0-{len(reiseplan[i1])-1}): "))
    if i2>=0 and i2<=len(reiseplan[i1])-1:
        print(reiseplan[i1][i2])
    else:
        print("Ugyldig innput!")
else:
    print("Ugyldig innput!")
