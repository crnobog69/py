# 46

import random

najmanjiBroj = 1
najveciBroj = 100

odgovor = random.randint(najmanjiBroj, najveciBroj)
# print(odgovor)

pokusaja = 0

print("Добродошли у Python игрицу за нагажање бројева!")

while True:
    korisnikovOdgovor = input("Унесите број (1 - 100):")

    if korisnikovOdgovor.isdigit():
        korisnikovOdgovor = int(korisnikovOdgovor)
        pokusaja += 1
        if korisnikovOdgovor == odgovor:
            print(f"Погодили сте! Одговор је: {odgovor}")
        if korisnikovOdgovor > najveciBroj or korisnikovOdgovor < najmanjiBroj:
            print("Тај број је ван домета!")
        elif korisnikovOdgovor < odgovor:
            print("Ниско! Пробвајте поново!")
        elif korisnikovOdgovor > odgovor:
            print("Високо! Покушајте поново!")
        else:
            print()
            print(f"ТАЧНО! Одговор је био: {odgovor}")
            print(f"Број покушаја: {pokusaja}")
            break
    else:
        print(f"Унели сте: {korisnikovOdgovor}. Можете унети само бројеве.")
