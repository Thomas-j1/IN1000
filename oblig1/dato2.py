"""
Skriver ut om datoer blir skrevet inn i riktig rekkefølge
"""

dato1 = input("Skriv inn dato, måned så dag (mmdd): ")
dato2 = input("Skriv inn dato, måned så dag (mmdd): ") #får to dato input fra bruker

if dato1<dato2:
    print("Riktig rekkefølge!")
elif  dato1==dato2:
    print("Samme dato!")
else:
    print("Feil rekkefølge!") #sjekker om dato1 er før dato2 
