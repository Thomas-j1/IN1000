"""
Lager ordbok av fil, og oppdaterer denne med ny data, før den skriver ut orboken til ny fil. Også utskrift av varmebølger fra fil
"""

def filOrdbok(file): #lager ordbok av fra fil og returnerer denne
    ordbok = {}
    liste = []
    filen = open(file)
    for linje in filen:
        liste.append(linje.rstrip("\n"))
    for linje in liste:
        bit = linje.split(",")
        float(bit[1])
        ordbok[bit[0]]=float(bit[1])
    return ordbok

print(filOrdbok("max_temperatures_per_month.csv"))
ordboken = filOrdbok("max_temperatures_per_month.csv")


def nyTemp(ordbokV, minFil): #sammenligner fil med ordbok, og returnerer ordbok ned ny data
    filen = open(minFil)
    for linje in filen:
        bit = linje.rstrip("\n").split(",")
        bit[2] = float(bit[2])
        if ordbokV[bit[0]]<bit[2]:
            ordbokV[bit[0]]=bit[2]
    return ordbokV

oppdatertOrdbok = nyTemp(ordboken, "max_daily_temperature_2018.csv")
print(nyTemp(ordboken, "max_daily_temperature_2018.csv"))

def nyFil(oppdatertOrdbok, filNavn): #skriver ut oppdatert ordbok til fil
    filen = open(filNavn, "w")
    for linje in oppdatertOrdbok:
        filen.write(f"{linje}, {oppdatertOrdbok[linje]} \n")

nyFil(oppdatertOrdbok, "testfil.csv")

def varmebolge(filNavn): #sjekker fil for varmebølger(fem dager med tempraturer over 25 grader), og skriver ut startdato og sluttdato for varmebølge
    count = 0
    filen = open(filNavn)
    startdatobolge = ""
    sluttdatobolge = ""
    bolge = False
    slutt = False
    for linje in filen:
        bit = linje.rstrip("\n").split(",")
        bit[2] = float(bit[2])
        currentdate = bit[1] + " " + bit[0]
        if bit[2]>=25.00:
            if count==0:
                startdatobolge = currentdate
            count+=1
        else:
            if bolge==True:
                slutt = True
            count=0
            bolge=False
        if count>=5:
            bolge=True
            sluttdatobolge=currentdate
        if slutt==True:
            print(f"Startdato for varmebølge var {startdatobolge}, og sluttdato for varmebølge var {sluttdatobolge}")
            slutt=False

varmebolge("max_daily_temperature_2018.csv")
