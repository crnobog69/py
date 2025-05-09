# Zadatak 64


def prosto(x):
    # Функција која проверава да ли је број прост.
    # Прост број је природан број већи од 1 који је дељив само са 1 и самим собом.

    # Број 1 по дефиницији није прост број
    if x == 1:
        return False

    # Проверавамо да ли је број дељив са било којим бројем од 2 до x-1
    for i in range(2, x):
        # Ако је број дељив са i, онда није прост
        if x % i == 0:
            return False

    # Ако број није дељив ни са једним бројем осим 1 и самог себе, онда је прост
    return True


# Унос броја n од корисника
n = int(input("n = "))
print("Прости бројеви.")

# Пролазимо кроз све бројеве од 1 до n
for p in range(1, n + 1):
    # Проверавамо да ли је број прост помоћу функције prosto()
    if prosto(p) == True:
        # Исписујемо прост број
        print(p)
