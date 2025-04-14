```python
# Zadatak 87-a

nizA = list()
nizB = list()

n = int(input("Дужина низа: n = "))
print("Унесите елементе низа A: ")

for i in range(0, n):
    temp = int(input())
    nizA.append(temp)

print("Низ A: ")
print(nizA)

while len(nizA) > 0:
    prvi = nizA[0]
    isti = nizA.count(prvi)

    if isti == 1:
        nizB.append(nizA[0])
        nizA.remove(prvi)
    else:
        while isti != 1:
            nizA.remove(prvi)
            isti = isti - 1

print("Низ Б: ")
print(nizB)

```
