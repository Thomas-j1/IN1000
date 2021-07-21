"""
Først defineres funksjonen minFunksjon. Deretter defineres prosedyren hovedprogram. Så kalles hovedprogram. I hovedprogrammet opprettes variablene a med verdi 42 og b med verdi 0. Så printes b. Derretter blir verdien av b omgjort til a som er 42, og variabelen a blir gjort om til funksjonen minFunksjon. Etter det blir variabelen b printet ut, og så kaller vi på minFunksjon. I funksjonen oprettes en løkkke som kjøres tre ganger. I løkken er variabelen c definert med verdien 2 og printes deretter, så øker variabelen med 1. Deretter defineres variablen b som 10, og så skal den øke med variablen a som ikke er definert i funksjonen, så dette vil ikke kjøre.
Programmet oppførte seg ikke som jeg trodde, den gikk rett på å kjøre minfunksjon når variablen a ble endret til funksjonen
"""
def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print (b)
    print (a)

hovedprogram()
