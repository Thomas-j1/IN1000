from sang import Sang
from spilleliste import Spilleliste

def hovedprogram():
    sang1 = Sang("Albinoni", "Adagio", "adagio.wav")
    sang2 = Sang("“Beethoven", "Ode to Joy", "ode_to_joy.wav")
    alle = Spilleliste("Alle")

    alle.leggTilSang(sang1)
    alle.leggTilSang(sang2)
    alle.spillAlle()

hovedprogram()
