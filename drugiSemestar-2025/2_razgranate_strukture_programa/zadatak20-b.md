```python
# zadatak 20-b

# import math

x = float(input("x = "))
y = float(input("y = "))

if y <= 0:
    z = max(
        x * x, y * y
    )  # max() враћа највећу вредност од прослеђених аргумената (веће између x² и y²)
else:
    z = min(
        x, y
    )  # мин() враћа најмању вредност од прослеђених аргумената (манје између x и y)

print("z = ", z)

```
