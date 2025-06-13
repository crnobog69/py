# Zadatak 93
# Саставити програм који учита матрицу целих димензије mхn,
# а затим врши сабирање позитивних и негативних елемената.

mat = list()
m = int(input("Број врста m: "))
n = int(input("Број колона n: "))
print("Унесите елементе матрице A: ")

for i in range(0, m):
    red = list()
    for j in range(0, n):
        print(f"A {i} {j} = ")
        red.append(int(input()))
    mat.append(red)

print("\nМАТРИЦА")
for i in range(0, m):
    for j in range(0, n):
        print(mat[i][j], " ", end="")
    print()

sp = sn = 0

for i in range(0, m):
    for j in range(0, n):
        if mat[i][j] > 0:
            sp = sp + mat[i][j]
        else:
            sn = sn + mat[i][j]

print(f"\nСума позитивних елемената: {sp}")
print(f"Сума негативних елемената: {sn}")
