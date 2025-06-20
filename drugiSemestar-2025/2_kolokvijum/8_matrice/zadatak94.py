# Zadatak 94
# Саставити програм који учита две матрице целих бројева, А и В, обе димензија mхn,
# а затим врши сабирање ове две матрице и исписује нову матрицу С.
# Матрице се сабирају тако што се сабирају елементи матрица са истим индексима.

matA = list()
matB = list()
matC = list()

m = int(input("Број врста m: "))
n = int(input("Број колона n: "))

print("Унесите елементе матрице A: ")
for i in range(0, m):
    red = list()
    for j in range(0, n):
        print(f"A {i} {j} = ", end="")
        red.append(int(input()))
    matA.append(red)

print("Унесите елементе матрице B: ")
for i in range(0, m):
    red = list()
    for j in range(0, n):
        print(f"B {i} {j} = ", end="")
        red.append(int(input()))
    matB.append(red)

# Сабирање матрица А и Б
for i in range(0, m):
    red = list()
    for j in range(0, n):
        red.append(matA[i][j] + matB[i][j])
    matC.append(red)

print("\nМАТРИЦА A")
for i in range(0, m):
    for j in range(0, n):
        print(matC[i][j], " ", end="")
    print()

print("\nМАТРИЦА Б")
for i in range(0, m):
    for j in range(0, n):
        print(matA[i][j], " ", end="")
    print()

print("\nМАТРИЦА Ц")
for i in range(0, m):
    for j in range(0, n):
        print(matB[i][j], " ", end="")
    print()
