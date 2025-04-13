# Zadatak 42
# Саставити програм којим се за дати природни број n израчунава сума:
# Сума = 1/(2*1+1)² + 1/(2*2+1)² + ... + 1/(2*n+1)²

# Унос природног броја n од корисника
# Функција int() конвертује унети стринг у целобројну вредност
# input() функција приказује поруку "n = " и чека унос корисника
n = int(input("n = "))

# Иницијализација помоћних променљивих
# i - бројач који ће ићи од 1 до n
# s - променљива за чување суме (почиње од 0)
i = 1
s = 0

# Цикличка структура која се извршава док је i мање или једнако n
# Ова петља се користи за израчунавање суме формуле 1/(2i+1)²
while i <= n:
    # Израчунавање текућег члана суме и додавање на укупну суму s
    # Формула: 1/(2*i+1)² за сваку вредност i од 1 до n
    # Множење у имениоцу се ради два пута јер је (2*i+1)² = (2*i+1)*(2*i+1)
    s = s + 1 / ((2 * i + 1) * (2 * i + 1))

    # Повећање бројача за следећу итерацију
    i = i + 1

# Испис резултата
# Функција round() заокружује суму s на 5 децималних места
# Коришћењем print() функције приказујемо кориснику израчунату суму
print("S =", round(s, 5))
