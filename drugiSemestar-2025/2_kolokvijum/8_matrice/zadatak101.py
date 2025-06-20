# Zadatak 101
# Саставити програм који гeнерише матрицу А случајних двоцифрених бројева димензије nxn,
# а затим формира нову матрицу В тако што све непарне елементе увећава за 1 а парне смањује за 1.

import random

matA = list()
matB = list()

n = int(input(" n = "))

for i in range(0, n):
    red = list()
    for j in range(0, n):
        red.append(random.randrange(10, 99))
    matA.append(red)

print("\nМАТРИЦА А")

for i in range(0, n):
    for j in range(0, n):
        print(matA[i][j], end="")
    print()

for i in range(0, n):
    red = list()
    for j in range(0, n):
        if matA[i][j] % 2 == 0:
            red.append(matA[i][j] - 1)
        else:
            red.append(matA[i][j] + 1)
    matB.append(red)

print("\nМАТРИЦА Б")

for i in range(0, n):
    for j in range(0, n):
        print(matB[i][j], " ", end="")
    print()
