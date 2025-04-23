```python
# Zadatak 79
# Саставити програм који за унети низ целих бројева,
# дужине n,
# проналази позицију траженог елемента или исписује обавештење да тражени елемент не постоји у низу.

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
        nadjen = 1
        print(f"Вредност {broj} има елемент {i + 1}")

if nadjen == 0:
    print(f"Вредност {broj} није пронађена у низу!")

```