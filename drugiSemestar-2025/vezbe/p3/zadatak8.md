```python
# Задатак 45 - Рачунање експоненцијалне функције e^(-x) коришћењем редова

import math  # Увоз математичке библиотеке за коришћење функције апсолутне вредности

# Унос вредности од корисника
x = float(input(" x = "))  # Вредност параметра x за који рачунамо e^(-x)
eps = float(input(" eps = "))  # Задата прецизност израчунавања (епсилон)

# Иницијализација променљивих
i = 0  # Бројач који представља редни број члана и факторијел у имениоцу
clan = 1  # Први члан реда (почетна вредност)
s = 1  # Сума чланова реда, почињемо са првим чланом

# Рачунање суме реда док апсолутна вредност текућег члана не постане мања од епсилон
while math.fabs(clan) >= eps:
    i = i + 1  # Повећавамо бројач за следећи члан
    clan = -clan * x / i  # Израчунавамо следећи члан према формули: (-1)^i * x^i / i!
    s = s + clan  # Додајемо израчунати члан у суму

# Исписујемо резултат заокружен на 5 децимала
print(
    f" S = {round(s, 5)}"
)  # Крајњи резултат представља апроксимацију вредности e^(-x)

```