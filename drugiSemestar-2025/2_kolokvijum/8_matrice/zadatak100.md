```python
# Zadatak 100

mat = list()

n = int(input(" n = "))

for i in range(0, n):
    red = list()
    for j in range(0, n):
        if i == j:
            red.append(1)
        else:
            red.append(0)
    mat.append(red)

print("\nМАТРИЦА")

for i in range(0, n):
    for j in range(0, n):
        print(mat[i][j], " ", end="")
    print()

```