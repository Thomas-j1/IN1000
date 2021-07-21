"""
Skriver ut variabler, tall, finner differanse på tall, og slår sammen navn
"""

navn = input("Skriv navn: ") #får navn fra bruker

print("Hei " + navn) #printer navnet

ht1 = 10
ht2 = 2

print(ht1)
print(ht2) #printer tall variabler

dif = ht1-ht2 #regner ut differanse mellom tall variabler

print("Differanse ", dif) #printer differansen

navn2 = input("Skriv nytt navn: ") #får nytt navninput fra bruker

sammen = navn + navn2 #slår sammen navn

print(sammen) #printer sammenslått navn

sammen = navn + " og " + navn2 #gjør om variabel med " og " mellom

print(sammen) #printer ny variabel
