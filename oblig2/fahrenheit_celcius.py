"""
Gjør om tempratur i fahrenheit til celcius
"""
tempratur = input("Skriv inn tempratur i fahrenheit: ")

tempraturf = int(tempratur)

tempraturc = (tempraturf-32)*(5/9) #regner om tempratur i fahrenheit til celcius

print("%.2f " % tempraturc) #printer tempratur i celius med to desimaler
