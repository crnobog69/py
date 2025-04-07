# Zadatak 62

# Функција која враћа збир два броја
def zbir(a, b):
    return a + b


# Функција која враћа разлику два броја (први минус други)
def razlika(a, b):
    return a - b


# Функција која враћа производ два броја
def proizvod(a, b):
    return a * b


# Функција која враћа количник два броја (први подељен другим)
# Ако је делилац једнак нули, враћа 0 да би избегла грешку дељења са нулом
def kolicnik(a, b):
    if b == 0:
        return 0
    else:
        return a / b


# Функција која враћа квадрат броја
def kvadrat(a):
    return a * a


# Функција која враћа куб броја
def kub(a):
    return a * a * a


# Учитавање вредности променљивих x и y од корисника
x = float(input("x = "))
y = float(input("y = "))

# Израчунавање вредности израза z1 = x + y²
z1 = zbir(x, kvadrat(y))
# Израчунавање вредности израза z2 = x³ - (x / y)
z2 = razlika(kub(x), kolicnik(x, y))
# Израчунавање вредности израза z3 = (x * y) + (5 - y)
z3 = zbir(proizvod(x, y), razlika(5, y))

# Исписивање резултата заокружених на 3 децимале
print(f"z1 = {round(z1, 3)}")
print(f"z2 = {round(z2, 3)}")
print(f"z3 = {round(z3, 3)}")
