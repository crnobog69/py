```python
# Zadatak 34

xmin = int(input(" xmin = "))
xmax = int(input(" xmax = "))
dx = int(input("   dx = "))

print("    x       y")
for x in range(xmin, xmax, dx):
    y = (2 * x + 1) / (x * x - 1)
    print(format(x, "5"), end="")
    print(format(round(y, 2), "8.2f"))

    # ИЛИ
    # print(f"{x:5}{round(y, 2):8.2f}")

```