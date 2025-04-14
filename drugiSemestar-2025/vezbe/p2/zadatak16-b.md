```python
# Zadatak 35-b

n = int(input("n = "))

for i, ј in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):  # \/ Склањамо овај део
        if (i == 1 or i == n) or (j == 1 or j == n):
            print("* ", end="")
        # elif j == 1 or j == n:
        #     print("* ", end="")
        else:
            print("  ", end="")
    print()

```