# Zadatak 83
# Саставити програм који за учитани низ целих бројева А дужине n формира низ В који се састоји од чланова низа А,
# с тим да се прво копирају позитивни,
# нуле па негативни чланови низа

nizA = list()
nizB = list()

n = int(input("Унесите дужину низа: n = "))
print("Унесите елементе низа: ")

for i in range(0, n):
    temp = int(input())
    nizA.append(temp)

for i in range(0, n):
    if nizA[i] > 0:
        nizB.append(nizA[i])

for i in range(0, n):
    if nizA[i] == 0:
        nizB.append(nizA[i])

for i in range(0, n):
    if nizA[i] < 0:
        nizB.append(nizA[i])

print("Низ А: ")
print(nizA)

print("Низ Б: ")
print(nizB)
