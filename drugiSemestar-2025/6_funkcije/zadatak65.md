```python
# Zadatak 65


def fakt(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
    return f


n = int(input("n = "))
k = int(input("k = "))

c = fakt(n) // (fakt(k) * fakt(n - k))

print(f"c = {c}")

```