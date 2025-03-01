# 24

broj = 5

print("Позитиван" if broj > 0 else "Негативан")

rezultat = "ПАРАН" if broj % 2 == 0 else "НЕПАРАН"
print(rezultat)

print()

a = 6
b = 7

max_broj = a if a > b else b
min_broj = a if a < b else b
print(max_broj)
print(min_broj)

print()

godine = 25
status = "Одрасло" if godine >= 18 else "Дете"
print(status)

print()

temperatura = 20

vreme = "ТОПЛО" if temperatura > 20 else "ХЛАДНО"
print(vreme)

print()

ulogaKorisnika = "админ"

pristupniNivo = "Пун приступ" if ulogaKorisnika == "админ" else "Ограничен приступ"
print(pristupniNivo)
