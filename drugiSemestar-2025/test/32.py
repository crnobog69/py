# 32

import time

mojeVreme = int(input("Унесите врме у секундама: "))

# for _ in range(0, mojeVreme):
#     print(_ + 1)
#     time.sleep(1)
# print("ВРЕМЕ ЈЕ ИСТЕКЛО!")
#
# print()
#
# for _ in reversed(range(0, mojeVreme)):
#     print(_)
#     time.sleep(1 + 1)
# print("ВРЕМЕ ЈЕ ИСТЕКЛО!")
#
# print()
#
# for _ in range(mojeVreme, 0, -1):
#     print(_)
#     time.sleep(1)
# print("ВРЕМЕ ЈЕ ИСТЕКЛО!")
#
# print()

for x in range(mojeVreme, 0, -1):
    sekunde = x % 60
    minuti = int(x / 60) % 60
    casovi = int(x / 3600)
    print(f"{casovi:02}:{minuti:02}:{sekunde:02}")
    time.sleep(1)
print("ВРЕМЕ ЈЕ ИСТЕКЛО!")
