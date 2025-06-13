# Zadatak 96
# Саставити програм који гeнерише матрицу случајних двоцифрених бројева димензије nxn,
# а затим формира и исписује низове који се редом састоје од на елемената на главној,
# споредној,
# изнад главне и испод главне дијагонале.

import random

mat = list()
nizA = list()
nizB = list()
nizC = list()
nizD = list()

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
    for j in range(0, n):
        if i == j:
            nizA.append(mat[i][j])  # Главна дијагонала
        if i + j == n - 1:
            nizB.append(mat[i][j])  # Споредна дијагонала
        if i < j:
            nizC.append(mat[i][j])  # Изнад главне дијагонале
        if i > j:
            nizD.append(mat[i][j])  # Испод главне дијагонале

print(f"\nНиз елемената на главној дијагонали: {nizA}")
print(f"Низ елемената на споредној дијагонали: {nizB}")
print(f"Низ елемената изнад главне дијагонале: {nizC}")
print(f"Низ елемената испод главне дијагонале: {nizD}")
