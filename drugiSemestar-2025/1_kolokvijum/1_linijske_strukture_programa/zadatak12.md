```python
# Zadatak 12
# Саставити програм који за унеи троцифрени број испитује његове цифре и суму цифара.

broj = int(input("Unesite trocifreni broj: "))

x = broj // 100
y = (broj // 10) % 10
z = broj % 10

# Ili da se pretvori u 'string' i onda pozicija stringa
# desetica = broj[1]
# i onda da se prebaci u 'int'

print("Cifre broja", broj, "su", x, ",", y, "i", z)
print("Suma cifara je:", x + y + z)

```