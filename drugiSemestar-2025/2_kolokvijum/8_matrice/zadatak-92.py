# Zadatak 92
# Саставити програм који учитава,
# а затим исписује елементе матрице mxn.
# Елементи матрице су цели бројеви.

mat = list()

m = int(input("Број врста m: "))
n = int(input("Број колона n: "))
print("Унесите елементе матрице A: ")

for i in range(0, m):
    red = list()
    for j in range(0, n):
        print("A", i, j, "= ", end="")
        red.append(int(input()))
    mat.append(red)
