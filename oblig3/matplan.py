"""
Ordbok med matplan for beboere på eldrehjem
"""
matplan = {
"ola": {
"frokost":"brød",
"lunsj":"egg",
"middag":"pizza"
},
"kari": {
"frokost":"pannekaker",
"lunsj":"yoghurt",
"middag":"taco"
},
"jose": {
"frokost":"chips",
"lunsj":"pan",
"middag":"enchiladas"
}
}

def skrivUtBeboer(): #printer matplan nøkkler, og skriver ut verdier baser på brukerinnput
    print(matplan.keys())
    navn = input("Skriv navn på beboer for matplan: ")

    if navn in matplan:
        print(matplan[navn])
    else:
        print("Beboer ikke registrert")

skrivUtBeboer()

"""
a) mengde: fordi brukernavnene må være unike
b) ordbok: fordi det er flere variabler knyttet til en nøkkelverdi
c) liste: fordi det kan være flere av samme, og bare en verditype
d) liste: fordi det er lettere å bruke, og det ikke er like stort krav om unikhet, og greit å kunne sortere
"""
