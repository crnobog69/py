```python
# Zadatak 74-b
# Саставити програм који ће учитати низ од n елемената и
# б) исписати их обрнутим редоследом.

n = int(input("Унесите дужину низа: n = "))
print("унесите елементе низа: ")

niz = list()

for i in range(0, n):
    temp = int(input())
    niz.append(temp)

print("Обрнути низ: ")
for i in range(n - 1, -1, -1):
    print(niz[i])

# Једноставнија верзија решења:
print("\nЈедноставнија верзија за приказ обрнутог низа:")
# Метод 1: Коришћењем обрнуте листе
print("Метод 1:")
for element in reversed(niz):
    print(element)

# Метод 2: Коришћењем слајсинга листе
print("Метод 2:")
for element in niz[::-1]:
    print(element)

# Метод 3: Коришћењем .reverse() методе
print("Метод 3:")
obrnuti_niz = niz.copy()  # Правимо копију да не модификујемо оригинални низ
obrnuti_niz.reverse()
for element in obrnuti_niz:
    print(element)

# Напомена: .reverse() метода мења низ на месту и не враћа нову листу

```