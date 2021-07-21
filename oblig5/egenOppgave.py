"""
Lag et program som kjører en liste med mail adresser mot nettsiden haveibeenpwned.com og sjekker om adressene er med i noen data brudd.
NB! kan bare kjøre 10 adresser om gangen med samme mailadresse før ip adresse må byttes grunnet restriksjoner på nettsiden
"""
import time
from bs4 import BeautifulSoup
import requests

def lagMailAdresserIFil(filnavn): #lager test mail liste til fil i parameter
    adresser = []
    for i in range(12):
        adresser.append(f"testmail{i}@gmail.com")
    filen = open(filnavn, "w")
    for j in adresser:
        filen.write(f"{j}\n")


def getData(element): #sjekker mail adresse mot haveibeenpwned Database
    req = requests.get(f"https://haveibeenpwned.com/account/{element}")
    soup = BeautifulSoup(req.text, 'html.parser')

    print("Mailadresse: ", element) #printer mailadressen som blir søkt på

    contaieren = soup.findAll(class_="pwnedCompanyTitle") #finner taggen som inneholder titlen på databruddet
    if len(contaieren)>0: #hvis taggen inneholder noen databrudd
        for x in range(len(contaieren)): #for hver databrudd tag
            companyTitle = str(contaieren[x])
            companyTitle = companyTitle.replace('<span class="pwnedCompanyTitle">', '')
            companyTitle = companyTitle.replace(':</span>', '')
            companyTitle = companyTitle.split("<")[0] #^fjerner alt utenom strengen i title taggen
            print("Breach: ", companyTitle)
    else:
        print("Breach: None")


def adresseFraListe(fil): #lager liste med mail adresser fra liste
    linjer = []
    filen = open(fil)

    for linje in filen: #legger til adresse i liste
        linjer.append(linje.rstrip('\n'))

    index = 0
    count=0
    lengde = len(linjer)
    while index<lengde:
        while count<10: #sålenge ikke flere en 10 adresser er søkt på på samme ip adresse
            getData(linjer[index]) #kaller på funksjon som sjekker adresse mot databasen
            time.sleep(1.5) #restriksjon på ett søk hvert 1500 millesekund på haveibeenpwned.com
            count+=1
            index+=1
            break
        else:
            svar = input("10 eller flere søk gjennomført med samme ip adresse. Bytt ip adresse før du fortsetter\nfortsette? y/n\n>")
            if svar == "y":
                count=0
            else:
                exit() #avslutter program

testfil = "testadresser.txt"
lagMailAdresserIFil(testfil)
adresseFraListe(testfil)
