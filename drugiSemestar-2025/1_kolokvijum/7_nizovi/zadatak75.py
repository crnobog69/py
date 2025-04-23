# Zadatak 75
# Саставити програм за израчунавање
# и исписивање аритметичке средине задатог низа (дужине n) целих бројева.

n = int(input("Дужина низа: n = "))
print("Унесите елемемнте низа: ")

niz = list()

suma = 0

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

for i in range(0, n):
    suma = suma + niz[i]

asr = round(suma / n, 5)
print(f"аритметичка средниа низа је: {asr}")
