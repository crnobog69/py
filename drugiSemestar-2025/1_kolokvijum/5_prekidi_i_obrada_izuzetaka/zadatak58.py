# Zadatak 58
# Саставити програм који рачуна квадрат броја n.
# Уколико корисник унесе реалан број или карактер захтевати поновни унос.

while True:
    n = input("n = ")

    try:
        n = int(n)
        break
    except:
        # Сигурније да се пише - except ValueError
        print("Погрешна вредност! Поновите унос!")
        continue
kvadrat = n * n

print(f"n * n = {kvadrat}")
