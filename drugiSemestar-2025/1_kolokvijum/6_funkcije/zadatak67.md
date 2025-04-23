```python
# Zadatak 67
# Рачунар “замишља” број од 1 до n, а играч се труди да га погоди.
# Ако је играч неуспешан у погађању, рачунар, после сваких m ≤ n покушаја,
# бира нови број из истог интервала.
# Реализовати игру погађања,
# уз испис броја покушаја и могућност поновног играња.

import random


def partija(n, m):
    pokusaji = 0
    x = random.randint(1, n + 1)

    while True:
        p = int(input("Ваш број: "))
        pokusaji += 1

        if p < 1 or p > n:
            return -1
        elif p == x:
            return pokusaji
        elif pokusaji % m == 0:
            print(f"Мењам број! Замишљени број је: {x}")
            x = random.randint(1, n + 1)


while True:
    print("---------- Нова игра ----------")

    n = int(input("Опсег: n = "))
    m = int(input("Број покушаја: m(m<=n) = "))

    if n > 1 and m >= 1 and m <= n:
        rezultat = partija(n, m)
        if rezultat == -1:
            print("било је занимљиво играти са вама!")
            break
        else:
            print(f"Погодили сте из {rezultat} пута!")

```