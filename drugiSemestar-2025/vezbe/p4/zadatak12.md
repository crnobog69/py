```python
# Zadatak 78

niz = list()
ind = 0

n = int(input("Дужина низа: n = "))
print("Унесите елементе низа: ")
for i in range(0, n):
    temp = int(input())
    niz.append(temp)
for i in range(0, n):
    if niz[i] % 2 == 0:
        maks = niz[i]
        mini = niz[i]
        imaks = i + 1
        imini = i + 1
        ind = 1
        break

if ind == 0:
    print("Нема парних бројева у низу!")
else:
    for i in range(0, n):
        if niz[i] % 2 == 0 and niz[i] > maks:
            maks = niz[i]
            imaks = i + 1
            if niz[i] % 2 == 0 and niz[i] < mini:
                mini = niz[i]
                imini = i + 1

print(f"Максимални парни елемент: {maks}")
print(f"Позиција максималног: {imaks}")
print(f"Минимални парни елемент: {mini}")
print(f"Позиција миниланог: {imini}")

```
