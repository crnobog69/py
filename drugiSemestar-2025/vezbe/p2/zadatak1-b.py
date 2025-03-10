# Zadatak 20-b

# import math

x = float(input(" x = "))
y = float(input(" y = "))

if y <= 0:
    z = max(x * x, y * y)
else:
    z = min(x, y)

print(f" z = {z}")
