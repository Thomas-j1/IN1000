"""
hovedprogram
"""
from spillebrett import Spillebrett

def main():
    rader = int(input("Skriv antall rader: "))
    kolonner = int(input("Skriv antall kolonner: "))
    brett = Spillebrett(rader, kolonner) #oppretter spillebrett objekt
    brett.tegnBrett()

    fortsett = True
    while fortsett: #til bruker skriver inn q
        bruker = input("Skriv inn q for å avslutte, enter for å fortsette: ")
        if bruker == "q":
            fortsett = False

        for i in range(5):
            print("\n")
        brett.oppdatering()
        brett.tegnBrett()
        print(f"Antall levende celler: {brett.finnAntallLevende()}")
        print(f"Generasjon: {brett._generasjonsnummer}")

main()
