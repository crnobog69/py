```python
# Zadatak 59
# Саставити програм који рачуна количник бројева x и y.
# Уколико корисник унесе вредност нула за y дати одговарајуће обавештење и захтевати поновни унос.

while True:
    x = float(input("x = "))
    y = float(input("y = "))

    try:
        z = x / y
        break
    except:
        print("Дељење нулом! Поновите унос!\n")
        continue
print(f"Резултат = {round(z, 4)}")

```