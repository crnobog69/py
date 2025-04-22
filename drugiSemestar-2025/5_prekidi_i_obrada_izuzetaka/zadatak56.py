# Zadatak 56
# Саставити програм који исписује све бројеве мање од 100 који нису дељиви са бројем 2, 3 и 5.

for i in range(1, 101, 1):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 5 == 0:
        continue
    print(i)
