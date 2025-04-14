```python
# Zadatk 7

dolar = float(input("Unesite vrednost dolara: "))
kurs = float(input("Unesite vrednost kursa: "))

dinar = dolar * kurs

# заокруживање променљиве 'dinar' на три децимале
dinar = round(dinar, 3)

print("Vrednost", dolar, "dolara iznosi", dinar, "dinara")

```