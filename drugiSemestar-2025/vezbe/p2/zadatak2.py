# Zadatak 21

import math

print("Унесите странице троугла: ")

a = float(input(" a = "))
b = float(input(" b = "))
c = float(input(" c = "))

if a + b > c and a + c > b and b + c > a:
    s = (a + b + c) / 2
    p = math.sqrt(s * (s - a) * (s - b) * (s - c))
    p = round(p, 3)
    print(f"Странице формирају троугао површине p = {p}")
else:
    print("Странице не формирају троугао.")
