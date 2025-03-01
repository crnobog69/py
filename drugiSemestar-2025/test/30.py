# 30

pocetniIznos = 0
kamata = 0
vreme = 0

# while pocetniIznos <= 0:
#     pocetniIznos = float(input("Унесите почетни износ: "))
#     if pocetniIznos <= 0:
#         print("Почетни износ не може бити мањи или једнак нули.")
#
# while kamata <= 0:
#     kamata = float(input("Унесите каматну стопу: "))
#     if kamata <= 0:
#         print("Каматна стопа не може бити мања или једнака нули.")
#
# while vreme <= 0:
#     vreme = int(input("Унесите време у годинама: "))
#     if pocetniIznos <= 0:
#         print("Време не може бити мање или једнако нули.")

while True:
    pocetniIznos = float(input("Унесите почетни износ: "))
    if pocetniIznos < 0:
        print("Почетни износ не може бити мањи од нуле.")
    else:
        break

while True:
    kamata = float(input("Унесите каматну стопу: "))
    if kamata < 0:
        print("Каматна стопа не може бити мања од нуле.")
    else:
        break

while True:
    vreme = int(input("Унесите време у годинама: "))
    if pocetniIznos < 0:
        print("Време не може бити мање од нуле.")
    else:
        break

print(pocetniIznos)
print(kamata)
print(vreme)

vreme = pocetniIznos * pow((1 + kamata / 100), vreme)
print(f"Стање након {vreme} година: {vreme:.2f} дин")
