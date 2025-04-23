# Zadatak 60
# Саставити програм који генерише случајни цели број у интервалу од 1 до 20 и тражи од корисника да погоди који је број у питању.
# Ако се број који унесе корисник разликује од замишљеног,
# кориснику се даје информација да ли је његов број већи или мањи од случајног броја.
# Корисник има 5 покушаја за погађање броја,
# иначе програм прекида рад уз одговарајућу поруку

MAX_POKUSAJA = 5
MAX_BROJ = 21

import random

print(f"Програм за погађање случајног броја између 1 и {MAX_BROJ}")
print(f"Дозвољено је: {MAX_BROJ} покушаја")

broj = random.randrange(1, MAX_BROJ + 1)

brojacPokusaja = 0

while True:
    pokusaj = int(input("\nПогодите случајни број: "))
    brojacPokusaja = brojacPokusaja + 1

    if pokusaj == broj:
        print("Честитамо погодили сте број!")
        print(f"Број покушаја: {brojacPokusaja}")
        break
    elif pokusaj < broj:
        print("Сувише мали број!")
    else:
        print("Сувише велики број!")

    if brojacPokusaja == MAX_POKUSAJA:
        print(f"Нажалост, нисте погодили у {MAX_POKUSAJA} покушаја.")
        print(f"Случајни број је био: {broj}")

print("Хвала на игри.")
