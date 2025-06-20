# Zadatak 103
# Саставити програм који учита матрицу А случајних једноцифрених бројева,
# димензије nxn,
# а затим формира и исписује нову матрицу В која представља производ АхА.

import random

matA = list()
matB = list()

n = int(input(" n = "))

for i in range(0, n):
    red = list()
    for j in range(0, n):
        red.append(random.randrange(0, 9))
    matA.append(red)

print("\nМАТРИЦА А")

for i in range(0, n):
    for j in range(0, n):
        print(matA[i][j], " ", end="")
    print()

for i in range(0, n):
    red = list()
    for j in range(0, n):
        red.append(0)
    matB.append(red)

for i in range(0, n):
    for j in range(0, n):
        for k in range(0, n):
            matB[i][j] += matA[i][k] * matA[k][j]

print("\nМАТРИЦА Б")

for i in range(0, n):
    for j in range(0, n):
        print(matB[i][j], " ", end="")
    print()
