# 27

# Креирамо стринг који представља број кредитне картице
brojKreditneKartice = "1234-5678-9012-3456"

# Исписујемо први знак броја кредитне картице (индекс 0)
print(brojKreditneKartice[0])

# Исписујемо прву групу бројева (прва 4 карактера)
print(brojKreditneKartice[0:4])  # или print(brojKreditneKartice[:4])

# Исписујемо другу групу бројева (карактери од 5. до 8. позиције)
print(brojKreditneKartice[5:9])

# Исписујемо све карактере од 5. позиције до краја
print(brojKreditneKartice[5:])

# Исписујемо последње три карактера, редом од последњег
print(brojKreditneKartice[-1])  # Последњи карактер
print(brojKreditneKartice[-2])  # Претпоследњи карактер
print(brojKreditneKartice[-3])  # Трећи од краја

# Исписујемо сваки други карактер у стрингу
print(brojKreditneKartice[::2])
# Исписујемо сваки трећи карактер у стрингу
print(brojKreditneKartice[::3])

# Креирамо маскирану верзију броја кредитне картице (приказујемо само последње 4 цифре)
poslednjiBrojevi = brojKreditneKartice[-4:]
print(f"XXXX-XXXX-XXXX-{poslednjiBrojevi}")

# Обрћемо редослед знакова у броју кредитне картице
brojKreditneKartice = brojKreditneKartice[::-1]
print(brojKreditneKartice)

# Закоментарисани код испод би исписао сваки карактер појединачно
# print(brojKreditneKartice[1])
# print(brojKreditneKartice[2])
# print(brojKreditneKartice[3])
# print(brojKreditneKartice[4])
# print(brojKreditneKartice[5])
# print(brojKreditneKartice[6])
# print(brojKreditneKartice[7])
# print(brojKreditneKartice[8])
# print(brojKreditneKartice[9])
# print(brojKreditneKartice[10])
# print(brojKreditneKartice[11])
# print(brojKreditneKartice[12])
# print(brojKreditneKartice[13])
# print(brojKreditneKartice[14])
# print(brojKreditneKartice[15])
# print(brojKreditneKartice[16])
# print(brojKreditneKartice[17])
# print(brojKreditneKartice[18])
