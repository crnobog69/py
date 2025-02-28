# 8

predmet = input("Unesite ime predmeta: ")
cena = float(input("Unesite cenu predmeta: "))
kolicina = int(input("Unesite kolicinu: "))

ukupno = cena * kolicina

print(f"Kupili ste {kolicina} x {predmet}")
print(f"Ukupno za placanje: {round(ukupno, 2)} RSD")
