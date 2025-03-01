# 33

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()
#

redovi = int(input("Унесите број редова: "))
kolone = int(input("Унесите број колона: "))
simbol = input("Унесите симбол: ")

for x in range(redovi):
    for y in range(kolone):
        print(simbol, end="")
    print()
