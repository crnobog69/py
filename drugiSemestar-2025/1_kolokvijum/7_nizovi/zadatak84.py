# Zadatak 84

nizA = list()
nizB = list()

n = int(input("Дужина низа: n = "))
print("Унесите елементе низа А: ")

for i in range(0, n):
    temp = int(input())
    nizA.append(temp)

for i in range(0, n):
    if nizA[i] == 0:
        temp = 0
    else:
        temp = 1 / nizA[i]
        temp = round(temp, 3)
    nizB.append(temp)

print("Низ А: ")
print(nizA)

print("низ Б: ")
print(nizB)
