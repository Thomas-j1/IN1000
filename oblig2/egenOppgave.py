"""
Gjør om fasit til oppgave 02.20: busstur på https://trix.ifi.uio.no/assignments/429 til å bruke funksjon og løkke istedenfor å skrive kode om igjen.
"""
passasjerer = 0

def utregning(nye): #sjekker om passasjerer er over 30 og legger til nye passasjerer
    global passasjerer
    if passasjerer + nye >= 30:
        print("Bussen er full.", passasjerer + nye - 30, "må gå til fots")
        passasjerer = 30
    else:
        passasjerer += nye
        print(nye, "personer gaar ombord i bussen.", passasjerer, "om bord.")


for x in range(3): #går igjennom funksjonen utregning(nye) 3 ganger og øker stasjontallet med en for her gang
    inp = input("Stasjon {}! Hvor mange går på bussen?\n> ".format(x+1))
    ny = int(inp)
    utregning(ny)


print("Bussen er fremme med", passasjerer, "personer ombord")
