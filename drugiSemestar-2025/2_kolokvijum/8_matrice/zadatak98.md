```python
# Zadatak 98
# Саставити програм који гeнерише матрицу случајних двоцифрених
# бројева димензије mxn, а затим формира низ чији је редослед
# елемената добијен на следећи начин

import random

mat = list()
niz = list()

m = int(input(" m = "))
n = int(input(" n = "))

for i in range(0, m):
    red = list()
    for j in range(0, n):
        red.append(random.randint(10, 99))
    mat.append(red)

print("\nМАТРИЦА")
for i in range(0, m):
    for j in range(0, n):
        print(mat[i][j], " ", end="")
    print()

for j in range(0, n):
    if j % 2 == 0:
        for i in range(0, m):
            niz.append(mat[i][j])
        else:
            for i in range(m - 1, -1, -1):
                niz.append(mat[i][j])

print("Низ:", niz)

```