```python
# Zadatak 97
# Саставити програм који гeнерише матрицу случајних једноцифрених бројева димензије nxn,
# а затим формира низ чији елементи су редом једнаки суми елемената у свакој врсти.

import random

mat = list()
niz = list()

n = int(input(" n = "))

for i in range(0, n):
    red = list()
    for j in range(0, n):
        red.append(random.randint(0, 9))
    mat.append(red)

print("\nМАТРИЦА")
for i in range(0, n):
    for j in range(0, n):
        print(mat[i][j], " ", end="")

for i in range(0, n):
    s = 0
    for j in range(0, n):
        s += mat[i][j]
    niz.append(s)

print("Низ:", niz)

```