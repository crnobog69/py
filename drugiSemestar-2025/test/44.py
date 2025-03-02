# 44

meni = {
    "Пица": 300.50,
    "Кокице": 250.99,
    "Нaћос": 280.00,
    "Сендвич": 220.00,
    "Кока-Кола": 180.00,
    "Лимунада": 150.00,
    "Чипс": 200.99,
    "Сладолед": 170.99,
}

korpa = []
ukupno = 0

print("|", ("-" * 7), "МЕНИ", ("-" * 7), "|")
for kljuc, vrednost in meni.items():
    print(f" {kljuc:10}: {vrednost:.2f} дин")
print("|", ("-" * 20), "|")

while True:
    hrana = input("Изабретие ставку (q за излаз): ")
    if hrana == "q" or hrana == "Q" or hrana == "љ" or hrana == "Љ":
        break
    elif meni.get(hrana) is None:
        print(f"{hrana} није на мениу.")
    elif meni.get(hrana) is not None:
        korpa.append(hrana)
        print(f"Додали сте: {hrana} у корпу.")

print()

print("|", ("-" * 1), "ВАША ПОРУЏБИНА", ("-" * 1), "|")
for hrana in korpa:
    ukupno += float(meni.get(hrana))
    print(hrana, end=" ")

print()
print(f"Укупно: {ukupno:.2f} дин")
