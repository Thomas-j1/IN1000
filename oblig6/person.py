"""
Skriv en klasse Person med en konstruktør som tar imot navn og alder og oppretter
og initialiserer instansvariabler med disse. I tillegg skal konstruktøren opprette en
instansvariabel med en tom liste hobbyer. Skriv en metode leggTilHobby som tar
imot en tekststreng og legger den til i hobbyer-listen. Skriv også en metode
skrivHobbyer. Denne metoden skal skrive alle hobbyene etter hverandre på en linje.
Gi deretter Person-klassen en metode skrivUt som i tillegg til å skrive ut navn og
alder kaller på metoden skrivHobbyer. La brukeren skrive inn navn og alder, og lag et
Person-objekt med informasjonen du får. Deretter skal brukeren ved hjelp av en
løkke få legge til så mange hobbyer de vil. Når brukeren ikke lenger ønsker å oppgi
hobbyer skal statistikk om brukeren skrives ut.
"""

class Person:

    def __init__(self, n, a): #konstruktør med alder, navn og hobbyer
        self._navn = n
        self._alder = a
        self._hobbyer = []

    def leggTilHobby(self, streng): #legger til hobby
        self._hobbyer.append(streng)

    def skrivHobbyer(self): #skriver ut strenge med hobbyer
        strenge = ""
        for i in self._hobbyer:
            strenge += f"{i} "
        print(strenge)

    def skrivUt(self): #skriver ut navn og alder, og kaller på metode skrivHobbyer()
        print(f"Navn: {self._navn} \n Alder: {self._alder}")
        self.skrivHobbyer()

navn = input("Skriv navn: ")
alder = input("skriv alder: ")
person1 = Person(navn, alder) #lager objekt

fortsett = True
while fortsett: #tar inn hobby input fra bruker til det er en bokstav i innput
    hobby = input("skriv inn hobby (en bokstav for å avslutte): ")

    if len(hobby)==1:
        person1.skrivUt()
        fortsett=False
    else:
        person1.leggTilHobby(hobby)
