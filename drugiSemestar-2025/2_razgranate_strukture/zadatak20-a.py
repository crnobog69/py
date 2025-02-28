# Zadatak 20-a

x = float(input("Unesite x: "))
y = float(input("Unesite y: "))

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

print("z = ", z)
