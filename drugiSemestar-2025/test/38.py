# 38

hrane = []
cene = []
ukupno = 0

while True:
    hrana = input("Унесите храну коју желите да купије: (q за излазак): ")

    # if hrane == "q" or hrane == "Q":
    if hrana.lower() == "q":
        break
    else:
        cena = float(input(f"Унесите цену {hrana}: дин "))
        hrane.append(hrana)
        cene.append(cena)

print()

print("----- Ваша корпа -----")
for hrana in hrane:
    print(hrana, end=" ")

for cena in cene:
    ukupno += cena

print()

print(f"Укупно: {ukupno} дин")
