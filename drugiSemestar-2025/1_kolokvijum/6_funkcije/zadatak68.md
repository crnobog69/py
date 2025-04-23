```python
# Zadatak 68
# Саставити програм који за дато n рачуна и исписује суму S = 1! + 2! + 3! + ... + n!.
# За рачунање факторијела користити рекурзивну функцију.


def fakt(n):
    if n == 1:
        return 1
    return n * fakt(n - 1)


def dvostruki_faktorijal(n):
    if n <= 0:
        return 1
    else:
        return n * dvostruki_faktorijal(n - 2)


n = int(input("n = "))

suma = 0

for i in range(1, n + 1, 1):
    suma = suma + fakt(i)
print(f"Сума = {suma}")

```