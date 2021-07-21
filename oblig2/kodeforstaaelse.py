"""
1. Dette er ikke lovelig kode fordi i print(b + "hei!") blir heltallet b etterfulgt av en strenge, som man ikke kan legge sammen.

2. Når vi kjører denne koden vil vi få en error ettersom du ikke kan legge samme strenge og heltall med +
"""

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (b + "Hei!")
