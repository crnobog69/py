```python
# Zadatak 73


def Fibonaci(x):
    if x == 0 or x == 1:
        return 1
    else:
        return Fibonaci(x - 1) + Fibonaci(x - 2)


while True:
    n = int(input("n = "))
    f = Fibonaci(n)

    print(f"Фиб = {f}")
    print("----------")

    # Приказ сваког Фибоначијевог броја и њихова сума
    suma = 0
    print("Fibonačijevi brojevi:")
    for i in range(n + 1):
        fib = Fibonaci(i)
        suma += fib
        print(f"F({i}) = {fib}")

    print(f"Suma Fibonačijevih brojeva: {suma}")
    print("----------")

```