```python
# Zadatak 29

import math

n = int(input("Унесите n = "))
x = int(input("Унесите x = "))
s = 0
p = 1

for i in range(1, n + 1, 1):
    p = p * x
    s = s + math.cos(p)
print(f"Сума = {s:.5f}")

```
