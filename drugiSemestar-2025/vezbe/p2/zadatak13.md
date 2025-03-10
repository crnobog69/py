```python
# Zadatak 32

# Саставити програм којим све процифрене бројеве код којих је друга цифра за 4 већа од орве,
# а трећа за 3 већа од друге

print("Бројеви: ")

for a in range(1, 9 + 1, 1):
    for b in range(0, 9 + 1, 1):
        for c in range(0, 9 + 1, 1):
            broj = 100 * a + 10 * b + c
            if b == a + 4 and c == b + 3:
                print(broj)

```