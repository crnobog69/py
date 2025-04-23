# Zadatak 74-a
# Саставити програм који ће учитати низ од n елемената и
# a) исписати их оним редоследом којим су учитани,

n = int(input("Дужина низа: n = "))
print("унесите елементе низа: ")

niz = list()

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

# Верзија 1
print(f"\nЕлементи низа: {niz}")

# Верзија 2
print("\nЕлементи низа: ")
for i in niz:
    print(i)

# Верзија 3
print("\nЕлементи низа: ")
for i in range(0, n, 1):
    print(i)

# Верзија 4
print("\nЕлементи низа:", *niz)
