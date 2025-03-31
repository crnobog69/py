```python
# Zadatak 13

cena = int(input("Unesite cenu proizvoda: "))

n500 = cena // 500
n100 = (cena % 500) // 100
n1 = (cena % 500) % 100

print("Br. novcanica od 500 dinara: ", n500)
print("Br. novcanica od 100 dinara: ", n100)
print("Br. novcanica od 1 dinar: ", n1)

```