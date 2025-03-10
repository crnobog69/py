# Zadatak 20-a

x = float(input(" x = "))
y = float(input(" y = "))

if y <= 0:
    if (x * x) < (y * y):
        z = y * y
    else:
        z = x * x
else:
    if x < y:
        z = x
    else:
        z = y

print(f" z = {z}")
