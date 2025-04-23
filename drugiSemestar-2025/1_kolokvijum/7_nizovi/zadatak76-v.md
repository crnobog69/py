```python
# Zadatak 76-v
# Саставити програм који ће за унети низ (дужине n) целих бројева одредити и исписати:
# в) суму елемената са парним индексима, суму елемената са непарним индексима и њихове средње вредности.

niz = list()

sp = sn = par = nep = 0

n = int(input("Унесите дужину низа: n = "))
print("Унесите елементе низа: ")

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

for i in range(0, n):
    if i % 2 == 0:
        sp = sp + niz[i]
        par = par + 1
    else:
        sn = sn + niz[i]
        nep = nep + 1

if par == 0:
    ssp = 0
else:
    ssp = sp / par

if nep == 0:
    ssn = 0
else:
    ssn = sn / nep

# try:
#     ssp = sp / par
# except ZeroDivisionError:
#     ssp = 0
#
# try:
#     ssn = sn / nep
# except ZeroDivisionError:
#     ssn = 0

print(f"Сума парних индекса: {sp}")
print(f"Сума непарних индекса: {sn}")

print(f"Средња вредност парних индекса: {round(ssp, 3)}")
print(f"Средња вредности непарних индекса: {round(ssn, 3)}")

```