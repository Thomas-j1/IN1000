"""
Lag en liste med dyrene til en dyrepark, å la bruker søke om dyreparken har dyret.
"""

dyr = ["tiger", "løve", "jaguar", "leopard", "koala", "ape"]

soket = input("Sjekk om dyret finnes i dyrepakren: ")
sok = soket.lower()

if sok in dyr: #sjekker om sok er i liste, og skriver ut beskjed til bruker om dyret finnes i parken
    print(sok, "finnes i dyreparken")
else:
    print(sok, "finnes ikke i dyreparken")
