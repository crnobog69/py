```python
# Zadatak 35-g

n = int(input("n = "))

for i in range(1, n + 1, 1):
    for j in range(1, i + 1, 1):
        if i == n:
            print("* ", end="")
        elif j == 1 or j == i:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

```
