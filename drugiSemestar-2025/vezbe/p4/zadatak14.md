```python
# Zadatak 80

niz = list()

n = int(input("Дужина низа: n = "))
print("Унесите елементе низа: ")

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

for i in range(0, n - 1):
    for j in range(i + 1, n):
        if niz[i] > niz[j]:
            niz[i], niz[j] = niz[j], niz[i]

print("Сортирани низ: ")
print(niz)

```
