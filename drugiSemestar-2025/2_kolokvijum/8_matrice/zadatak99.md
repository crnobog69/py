```python
# Zadatak 99
# Саставити програм који гeнерише матрицу случајних двоцифрених бројева димензије nxn,
# а затим формира четири низа чији су елементи редом једнаки:
# најмањем елементу у сваком реду матрице,
# највећем елементу у сваком реду матрице,
# најмањем елементу у свакој колони матрице,
# највећем елементу у свакој колони матрице.

import random

mat = list()
nizMAXV = list()
nizMINV = list()
nizMAXK = list()
nizMINK = list()

n = int(input(" n = "))

for i in range(0, n):
    red = list()
    for j in range(0, n):
        red.append(random.randint(10, 99))
    mat.append(red)

print("\nМАТРИЦА")

for i in range(0, n):
    for j in range(0, n):
        print(mat[i][j], " ", end="")
    print()

for i in range(0, n):
    maksV = mat[i][0]
    miniV = mat[i][0]
    maksK = mat[0][i]
    miniK = mat[0][i]

    for j in range(0, n):
        if mat[i][j] > maksV:
            maksV = mat[i][j]
        if mat[i][j] < miniV:
            miniV = mat[i][j]
        if mat[j][i] > maksK:
            maksK = mat[j][i]
        if mat[j][i] < miniK:
            miniK = mat[j][i]

    nizMAXV.append(maksV)
    nizMINV.append(miniV)
    nizMAXK.append(maksK)
    nizMINK.append(miniK)

print("Максимални врста", nizMAXV)
print("Минимални врста", nizMINV)
print("Максимални колона", nizMAXK)
print("Минимални колона", nizMINK)

```