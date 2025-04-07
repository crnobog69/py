# Zadatak 77

niz = list()
n = int(input("Дужина низа n = "))
print("унеисте елементе низа:")

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

maks = niz[0]
mini = niz[0]
imaks = imini = 1

for i in range(1, n):
    if niz[i] > maks:
        maks = niz[i]
        imaks = i + 1
    if niz[i] < mini:
        mini = niz[i]
        imini = i + 1

print(f"Максимални елемент: {maks}")
print(f"Позиција максималног: {imaks}")
print(f"Минимални елемент: {mini}")
print(f"Позиција минималног: {imini}")
