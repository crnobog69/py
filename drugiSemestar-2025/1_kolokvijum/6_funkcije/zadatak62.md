```python
# Zadatak 62


def zbir(a, b):
    return a + b


def razlika(a, b):
    return a - b


def proizvod(a, b):
    return a * b


def kolicnik(a, b):
    if b == 0:
        return 0
    else:
        return a / b


def kvadrat(a):
    return a * a


def kub(a):
    return a * a * a


x = float(input("x = "))
y = float(input("y = "))

z1 = zbir(x, kvadrat(y))
z2 = razlika(kub(x), kolicnik(x, y))
z3 = zbir(proizvod(x, y), razlika(5, y))

print(f"z1 = {round(z1, 3)}")
print(f"z2 = {round(z2, 3)}")
print(f"z3 = {round(z3, 3)}")

```