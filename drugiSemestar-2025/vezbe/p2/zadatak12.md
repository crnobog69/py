```python
# Zadatak 31

# Армстронг број је број који је једнак збиру својих цифара степенираних на број цифара
# У случају троцифрених бројева, број абц је Армстронг ако је abc = a^3 + b^3 + c^3
# На пример: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

print("Армстронгови бројеви: ")

# Користимо три угњеждене петље за генерисанје свих троцифрених бројева
# Прва цифра (a) може бити od 1 до 9
for a in range(1, 9 + 1, 1):
    # Друга цифра (b) може бити од 0 до 9
    for b in range(0, 9 + 1, 1):
        # Трећа цифра (c) може бити од 0 до 9
        for c in range(0, 9 + 1, 1):
            # Формирамо троцифрени број
            broj = 100 * a + 10 * b + c

            # Проверавамо да ли је Армстронг број
            # (Збир кубова цифара једнак оригиналном броју)
            if (
                broj == a**3 + b**3 + c**3
            ):  # Алтернативни начин записа: a*a*a + b*b*b + c*c*c
                print(broj)

```