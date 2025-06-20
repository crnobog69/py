# Zadatak 95
# Саставити програм који ће учитати матрицу целих бројева димензије nxn,
# исписати матрицу у облику таблице,
# а затим суму елемената на главној,
# споредној,
# изнад главне и испод главне дијагонале.

mat = list()

n = int(input(" n = "))
print("Унесите елементе матрице: ")
for i in range(0, n):
    red = list()
    for j in range(0, n):
        print(f"A {i} {j} = ", end="")
        red.append(int(input()))
    mat.append(red)

print("\nМАТРИЦА")
for i in range(0, n):
    for j in range(0, n):
        print(mat[i][j], " ", end="")
    print()

sg = ss = iznad = ispod = 0

for i in range(0, n):
    for j in range(0, n):
        if i == j:
            sg += mat[i][j]
        if i + j == n - 1:
            ss += mat[i][j]
        if i < j:
            iznad += mat[i][j]
        if i > j:
            ispod += mat[i][j]

print(f"\nСума елемената на главној дијагонали: {sg}")
print(f"Сума елемената на споредној дијагонали: {ss}")
print(f"Сума елемената изнад главне дијагонале: {iznad}")
print(f"Сума елемената испод главне дијагонале: {ispod}")
