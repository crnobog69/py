# 21

tezina = float(input(" Унесите тежину: "))
mernaJedinica = input(" Унесите мерну јединицу (kg, lb): ")

if mernaJedinica == "kg":
    tezina = tezina * 2.205
    mernaJedinica = "kg"
elif mernaJedinica == "lb":
    tezina = tezina * 2.205
    mernaJedinica = "lb"
else:
    print(f"Мерна јединица `{mernaJedinica}` није подржана")

print(f"Тежина је: {round(tezina, 2)} {mernaJedinica}.")
