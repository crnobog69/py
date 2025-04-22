# Zadatak 57
# Саставити програм за рачунање суме природних бројева од 1 до n,
# изузимајући број који је дељив са х који дефинише корисник.

n = int(input("n = "))
x = int(input("x = "))

suma = 0

for i in range(1, n + 1, 1):
    if i % x == 0:
        continue
    suma = suma + i
print(f"Сума = {suma}")
