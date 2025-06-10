```python
# Zadatak 91
# Саставити програм који штампа генерисану матрицу 3x3.

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Prvi način
print("\nМАТРИЦА")
print(mat)

# Други начин
print("\nМАТРИЦА")
for i in range(0, 3):
    print(mat[i])

# Трећи начин
print("\nМАТРИЦА")
for red in mat:
    for element in red:
        print(element, " ", end="")
    print()

# Четврти начин
print("\nМАТРИЦА")
for i in range(0, 3):
    for j in range(0, 3):
        print(mat[i][j], " ", end="")
    print()

```