# 36

# Листа = [] уређена и променљива. Дупликати дозвољени
# Сет   = {} неуређен и непроменљив, али Додавање/Уклањање је дозвољено. Без дупликата
# Торка = () уређена и непроменљива. Дупликати дозвољени. БРЖА

## Сетови
# Сетови су колекције које не дозвољавају дупликате елемената
# и немају одређени редослед (неиндексирани су).

# print(dir(hrane))
# print(help(hrane))

# идаље ће имати само један "кокос"
hrane = {"јабука", "поморанџа", "банана", "кокос", "кокос"}
# Дупликат "кокос" ће бити аутоматски уклоњен

hrane.add("ананас")  # Додаје се елемент "ананас" у сет
hrane.remove("јабука")  # Уклања елемент "јабука" из сета
hrane.pop()  # Уклања и враћа произвољан елемент (сетови немају редослед)
hrane.clear()  # Уклања све елементе из сета - сет постаје празан

print(hrane)  # Исписује празан сет: set()

# print(len(hrane))  # Враћа број елемената у сету
# print("јабука" in hrane)  # Проверава да ли елемент постоји у сету
