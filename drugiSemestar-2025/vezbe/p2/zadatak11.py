# Zadatak 30

a = int(input("Унесите a = "))
b = int(input("Унесите b = "))
s = 0

print(f"Бројеви од {a} do {b} дељиви са 7: ")

for i in range(a, b + 1, 1):
    if i % 7 == 0:
        s = s + i
        print(i)
print(f"Сума: {s}")
