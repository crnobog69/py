# Zadatak 82
# Саставити програм за сортирање унетог низа целих бројева,
# дужине n,
# у неопадајући поредак методом уметања (Insert Sort).
# Исписати сортирани низ.
# Insert Sort: Нека је првих k елемената већ уређено у неопадајућем поретку,
# тада се узима (k+1)-ви елемент и умеће на одговарајуће место међу првих k елемената тако да првих k+1 елемената буде уређено.
# Овај се метод примењује за k од 0 до n-2.

niz = list()

n = int(input("Дужина низа: n = "))
print("Унесите елементе низа: ")

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

for i in range(1, n, 1):
    pom = niz[i]
    j = i - 1

    while j >= 0 and niz[j] > pom:
        niz[j + 1] = niz[j]
        j = j - 1

    niz[j + 1] = pom

print("Сортирани низ: ")
print(niz)

# brojevi = [5, 2, 9, 1]
# brojevi.sort()
# print(brojevi)  # Излаз: [1, 2, 5, 9]
# -----
# brojevi.sort(reverse=True)
# print(brojevi)  # Излаз: [9, 5, 2, 1]
# brojevi = [5, 2, 9, 1]
# -----
# novi = sorted(brojevi)
# print(novi)     # [1, 2, 5, 9]
# print(brojevi)  # Оригинална остаје: [5, 2, 9, 1]
