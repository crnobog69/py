# Zadatak 19

import math

x=float(input("x = "))
y=float(input("y = "))

if (x >= -2) and (x < 10):
    z = 2 * x + 3 * y
elif (x >= 5) and (x < 10):
    z = x / (2 * x + math.pow(y, 3))
else:
    z = math.sqrt(2 * x + 3 * y * y) 

z = round(z, 4)

print("z =", z)