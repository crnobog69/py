```python
# Zadatak 43
# Саставити програм којим се за дате бројеве k и n израчунава сума: k/1² - 2k/3² + 3k/5² - 4k/7² + ... + (-1)^(n+1)*nk/(2n-1)²

# Унос параметара k и n од корисника
# k - фактор који се множи са бројиоцем сваког члана
# n - број чланова у низу које треба сабрати
k = int(input("k = "))  # Претвара унети текст у целобројну вредност
n = int(input("n = "))  # Претвара унети текст у целобројну вредност

# Иницијализација променљивих
i = 1  # Бројач петље који иде од 1 до n
s = 0  # Променљива за чување текуће суме низа
znak = 1  # Променљива која контролише знак члана (1 за +, -1 за -)

# Петља која израчунава суму низа
while i <= n:  # Извршава се док i не достигне вредност n
    # Формула за израчунавање i-тог члана низа:
    # znak * (i * k) / ((2 * i - 1) * (2 * i - 1))
    # - znak: контролише знак члана (наизменично +1 и -1)
    # - i * k: бројилац разломка
    # - (2 * i - 1) * (2 * i - 1): квадрат имениоца (1², 3², 5², 7², итд.)
    s = s + znak * (i * k) / ((2 * i - 1) * (2 * i - 1))

    i = i + 1  # Повећање бројача за следећу итерацију
    znak = -znak  # Промена знака за следећи члан (наизменично +1 и -1)

# Исписивање коначног резултата
# Функција round() заокружује број на одређени број децимала (у овом случају на 5)
print("Сума =", round(s, 5))

```