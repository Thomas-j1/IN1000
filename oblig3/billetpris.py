"""
Skriver ut billetpris basert på alder, med feil
"""

def beregning(): #skriver ut pris basert på alder input fra bruker
    alder = int(input("Skriv inn alder: "))
    billetpris = 0

    if alder<=17:
        billetpris=30
    elif alder>17:
        billetpris=50
    elif alder>=63:
        billetpris=35
    else:
        print("ugyldig input: ")

    print("Billetprisen for", alder, "er", billetpris)

beregning()

#prosedyren er gal fordi elif alder>17 er før elif alder>=63, som gjør at den første elifen alltid vil være sann før den andre.
