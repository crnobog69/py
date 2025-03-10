# Zadatak 33


n = int(input("Унесите n = "))
s = 0
print("Делиоци: ")

for i in range(1, n + 1, 1):
    if n % i == 0:
        print(i)
        s = s + i
if s - n == n:
    print(f"Број {n} јесте савршен.")
else:
    print(f"Број {n} није савршен.")
