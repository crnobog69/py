# Ниске - Стрингови - String

ime = "Lain"
hrana = "pica"
e_posta = "lain@lain.com"

print(f"Zdravo, {ime}!")
print(f"Ti volis hranu poz nazivom {hrana}!")
print(f"Tvoja e-posta je: {e_posta}.")

# Цео број - Интиџер - Integer

godine = 19
kolicina = 10
broj_studenata = 100

print(f"Ti imas {godine} godina.")
print(f"Kupio si {kolicina} slatkisa.")
print(f"Tvoja ucionica ima {broj_studenata} studentata.")

# Реално број - Флоут - Float

cena = 10.99
proseca_ocena = 3.2
daljina = 321.4

print(f"Cena je {cena} Динара.")
print(f"Prosečna ocena je {proseca_ocena}.")
print(f"Trcao si {daljina} Km.")

# Булеан - Бул - Bool

## Први начин
da_li_je_sunce_izaslo = True

if da_li_je_sunce_izaslo:
    True
    print("Sunce je izaslo.")
else:
    False
    print("Sunce nije izaslo.")

print(f"Da li je sunce izaslo? {da_li_je_sunce_izaslo}")

## Други начин
na_prodaju = False

if na_prodaju:
    print("Ta stvar je na prodaju.")
else:
    print("Ta stvar nije na prodaju.")

jeste_onlajn = True

if jeste_onlajn:
    print("Onlajn ste.")
else:
    print("Oflajn ste.")
