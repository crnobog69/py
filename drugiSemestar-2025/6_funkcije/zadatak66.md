```python
# Zadatak 66

# Двоструки факторијал
def dfakt(n):
    f = 1
    while n >= 2:
        f = f * n
        n = n - 2
    return f


n = int(input("n = "))

suma = 0
znak = 1

for i in range(1, n + 1):
    suma = suma + znak * 1 / dfakt(i)
    znak = -znak

print(f"Сума = {round(suma, 4)}")

```