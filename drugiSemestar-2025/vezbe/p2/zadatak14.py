# Zадатак 33

# Уносимо број n
n = int(input("Унесите n = "))
# Иницијализујемо суму делилаца
s = 0
print("Делиоци: ")

# Прођемо кроз све бројеве од 1 до n
for i in range(1, n + 1, 1):
    # Ако је i делилац броја n
    if n % i == 0:
        # Исписујемо делилац
        print(i)
        # Додајемо делилац у суму
        s = s + i

# Проверавамо да ли је број савршен
# Савршен број је број који је једнак збиру својих правих делилаца
if s - n == n:
    print(f"Број {n} јесте савршен.")
else:
    print(f"Број {n} није савршен.")
