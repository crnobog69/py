# Zadatak 28

n = int(input("Унесите n = "))
m = int(input("Унесите m = "))
suma = 0
znak = 1

for i in range(1, m + 1, 1):
    suma += znak / (n + i * m)
    znak = -znak

print(f"Сума = {suma:.5f}")
