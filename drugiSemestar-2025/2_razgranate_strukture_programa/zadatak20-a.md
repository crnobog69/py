```python
# Zadatak 20-a

x = float(input("Унесите x: "))
y = float(input("Унесите y: "))

if y <= 0:
    if (x * x) < (y * y):
        z = y * y
    else:
        z = x * x
else:
    if x < y:
        z = x
    else:
        z = y

print("z = ", z)

```