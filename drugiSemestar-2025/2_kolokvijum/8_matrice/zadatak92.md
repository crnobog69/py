```python
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

# Први начин
print("\nМАТРИЦА")
print(mat)

# Други начин
print("\nМАТРИЦА")
for i in range(0, m):
    print(mat[i])

# Трећи начин
print("\nМАТРИЦА")
for red in mat:
    for element in red:
        print(element, " ", end="")
    print()

# Четврти начин
print("\nМАТРИЦА")
for i in range(0, m):
    for j in range(0, n):
        print(mat[i][j], " ", end="")
    print()

```