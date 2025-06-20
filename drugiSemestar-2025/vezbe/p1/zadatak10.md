```python
# Zadatak 10

x = float(input("x = "))
y = float(input("y = "))

import math

S = math.exp(2 * x) * math.sqrt(x**3 + y * y / (2 + x))

print("S =", S)

Szaokruzeno = round(S, 3)

print("Zaokruzeno S =", Szaokruzeno)

```