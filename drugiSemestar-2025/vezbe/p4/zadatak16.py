# Zadatak 88-b

import random

niz = list()
brojac = list()

for j in range(0, 10):
    brojac.append(0)

n = int(input("Дужина низа: n = "))

for i in range(0, n):
    niz.append(random.randint(0, 9))
for j in range(0, 10):
    brojac[j] = niz.count(j)

print("Низ: ")
print(niz)

for j in range(0, 10):
    print("Цифра", j, "Број појављивања =", brojac[j])
