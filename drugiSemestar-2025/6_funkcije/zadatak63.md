```python
# Zadatak 63


def paran(n):
    if n % 2 == 0:
        print("Број је паран.")
    else:
        print("број је непаран.")


def negativan(n):
    if n < 0:
        print("број је негативан.")
    elif n > 0:
        print("број је позитиван.")
    else:
        print("број је нула.")


x = int(input("x = "))

paran(x)

negativan(x)

```