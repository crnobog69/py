# 8

predmet = input("Унесите име предмета: ")
cena = float(input("Унесите цену предмета: "))
kolicina = int(input("Унесите количину: "))

ukupno = cena * kolicina

print(f"Купили сте {kolicina} x {predmet}")
print(f"Укупно за плаћање: {round(ukupno, 2)} дин")
