"""
Skriver ut om datoer blir skrevet inn i riktig rekkefølge
"""

dato1 = int(input("Skriv inn dato, dag(dd):  "))
dato2 = int(input("Skriv inn dato, måned(mm):  "))
dato3 = int(input("Skriv inn dato, dag(dd):  "))
dato4 = int(input("Skriv inn dato, måned(mm):  ")) #får 2 dato input fra bruker

if dato2<dato4 or dato2<=dato4 and dato1<dato3:
    print("Riktig rekkefølge!")
elif  dato2==dato4 and dato1==dato3:
    print("Samme dato!")
else:
    print("Feil rekkefølge!") #sjekker om dato input 1&2 kommer før 3&4
