"""
Lager brukernavn, epostbrukere, printer ut epostadresser og tester funksjoner
"""
ordbok = {}

def lagBrukernavn(fulltNavn, ordbok): #lager unike brukernavn med navn og ordbok som parametere
    deltNavn = fulltNavn.split(" ")
    print(deltNavn)
    brukernavn = deltNavn[0].lower() + deltNavn[1][0].lower()
    count = 2
    while brukernavn in ordbok:
        brukernavn = deltNavn[0].lower() + deltNavn[1][0:count].lower()
        count+=1
    return brukernavn

def lagBrukernavnTest():#test for lagBrukernavn(), funker ikke etter siste deloppgave
    resulat = lagBrukernavn("Thomas Johannessen")
    korrektresultat = "thomasj"
    assert resulat==korrektresultat, "Forventet resultat: " + korrektresultat + " resultat: " + resulat
#lagBrukernavnTest()

def lagEpost(prefix, suffix): #lager eposadresse basert på prefix og suffix
    mail = prefix + "@" + suffix
    return mail

def lagEpostTest(): #tester lagEpost()
    resulat = lagEpost("thomasj", "uio.no")
    korrektresultat = "thomasj@uio.no"
    assert resulat==korrektresultat, "Forventet resultat: " + korrektresultat + " resultat: " + resulat
lagEpostTest()

def printEposter(ordbok): #skriver ut alle epostadresser i ordbok
    for element in ordbok:
        print(lagEpost(element, ordbok[element]))


testordbok = {
"olan": "ifi.uio.no",
"karian": "student.matnat.uio.no"
}
#printEposter(testordbok)
fortsett=True
while fortsett==True: #tar imot input fra bruker å kjører funksjoner basert på disse
    bokstav = input("i : lag bruker\np : print epost\ns : avslutt program\n>")
    if bokstav == "i": #kaller på lagBrukernavn med brukerinnput som argumenter
        navn = input("Skriv inn ett navn: ")
        suffix = input("Skriv inn suffix: ")
        brukernavn = lagBrukernavn(navn, ordbok)
        ordbok[brukernavn]=suffix

    elif bokstav == "p": #kaller på printEposter
        printEposter(ordbok)

    elif bokstav == "s": #stopper while løkke
        fortsett=False
