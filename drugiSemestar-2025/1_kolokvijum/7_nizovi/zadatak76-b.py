# Zadatak 76-b
# Саставити програм који ће за унети низ (дужине n) целих бројева одредити и исписати:
# б) суму позитивних, суму негативних бројева и њихове средње вредности

niz = list()

sp = sn = poz = neg = 0

n = int(input("Дужина низа: n = "))
print("Унесите елементе низа: ")

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

for i in range(0, n):
    if niz[i] > 0:
        sp = sp + niz[i]
        poz = poz + 1
    elif niz[i] < 0:
        sn = sn + niz[i]
        neg = neg + 1

if poz == 0:
    ssp = 0
else:
    ssp = sp / poz
if neg == 0:
    ssn = 0

# try:
#     ssp = sp / par
# except ZeroDivisionError:
#     ssp = 0
#
# try:
#     ssn = sn / nep
# except ZeroDivisionError:
#     ssn = 0

print(f"Сума позитивних: {sp}")
print(f"Сума негативних: {sn}")

print(f"Средња вреднсот позитивних: {round(ssp, 3)}")
print(f"Средња вредност негативних: {round(ssn, 3)}")
