```python
# Zadatak 23

import math

print(" Unesite koeficijente: ")

a = float(input(" a = "))
b = float(input(" b = "))
c = float(input(" c = "))

if a != 0:
    D = b * b - 4 * a * c
    if D > 0:
        x1 = -b + math.sqrt(D) / (2 * a)
        x2 = -b - math.sqrt(D) / (2 * a)

        x1 = round(x1, 2)
        x2 = round(x2, 2)

        print(f" Rešenja: \nx1 = {x1} x2 = {x2}")
    elif D == 0:
        x1 = -b / (2 * a)
        x1 = round(x1, 2)

        print(f" Rešenje: \nx1 = x2 = {x1}")
    else:
        x1 = -b / (2 * a)
        x2 = math.sqrt(-D) / (2 * a)

        x1 = round(x1, 2)
        x2 = round(x2, 2)
        print(" Kompletna rešenja: ")
        print(f" x1 = {x1} + i {x2}     x1 = {x1} - i {x2}")
elif b != 0:
    x1 = -c / b
    print(f" Rešenje: \nx = {x1}")
else:
    print(" Sistem nema rešenja.")

```