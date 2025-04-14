```python
# Zadatak 79

niz = list()
nadjen = 0

n = int(input("Дужина низа: n = "))
print("Унесите елементе низа: ")
for i in range(0, n):
    temp = int(input())
    niz.append(temp)

broj = int(input("Тражена вредност = "))

for i in range(0, n):
    if niz[i] == broj:
        najdne = 1
        print("Вредност", broj, "има елемент", i + 1)

if nadjen == 0:
    print("Вредност", broj, "није пронађена у низу!")

```