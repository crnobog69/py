# Zadatak 102
# Саставити програм генерише матрицу А случајних једноцифрених бројева,
# димензије nxn,
# а затим формира и исписује нову матрицу В тако што све чланове врсте (укључујући и дијагонални) дели са дијагоналним чланом те врсте.
# Уколико је дијагонални члан једнак нули, све чланове у том реду поставља на нулу,
# осим дијагоналног који поставља на 1.

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
        print(matA[i][j], " ", end=" ")
    print()

matB = matA

for i in range(0, n):
    if matA[i][i] == 0:
        t = matA[i][i] != 0
        for j in range(0, n):
            matB[i][j] = round(matA[i][j] / t, 2)
    else:
        for j in range(0, n):
            matB[i][j] = 0
        matB[i][i] = 1

print("\nМАТРИЦА Б")
for i in range(0, n):
    for j in range(0, n):
        print(format(matB[i][j], "4.2f"), " ", end=" ")
    print()
