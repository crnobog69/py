# 20

operator = input(" Унесите оператор ( + - * / ): ")

broj1 = float(input(" Унесите први број: "))
broj2 = float(input(" Унесите други број: "))

if operator == "+":
    rezultat = broj1 + broj2
    print(f" Резултат је: {round(rezultat, 3)}")
elif operator == "-":
    rezultat = broj1 - broj2
    print(f" Резултат је: {round(rezultat, 3)}")
elif operator == "*":
    rezultat = broj1 * broj2
    print(f" Резултат је: {round(rezultat, 3)}")
elif operator == "/":
    rezultat = broj1 / broj2
    print(f" Резултат је: {round(rezultat, 3)}")
else:
    print(f" Оператор {operator} није подржан.")
    print(" Могуци избор само између ( + - * / ).")
