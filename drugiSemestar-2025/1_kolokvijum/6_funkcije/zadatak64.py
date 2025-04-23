# Zadatak 64


def prosto(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


n = int(input("n = "))

print("Прости бројеви: ")

for p in range(1, n + 1, 1):
    # или (правилније) - if prosto:
    if prosto(p) == True:
        print(p)
