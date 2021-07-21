"""
Spør om bruker vil ha brus og skriver ut svar basert på input
"""

jaEllerNei = input("Vil du ha brus, ja eller nei?: ") #ja eller nei input fra bruker

if jaEllerNei == "ja":
    print("Her har du en brus!")
elif jaEllerNei == "nei":
    print("Den er grei.")
else:
    print("Det forstod jeg ikke helt") #skriver ut svar basert på ja eller nei input
