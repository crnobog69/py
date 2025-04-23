# Zadatak 61
# Саставити функцију за сабирање два цела броја и приказ резултата.
# Затим позвати функцију n пута у главном програму


def zbir():
    a = int(input("a = "))
    b = int(input("b = "))

    c = a + b

    print(f"Збир = {c}")


n = int(input("n = "))

print()

for i in range(1, n + 1):
    zbir()
    print("--------------------")
