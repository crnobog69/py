# Zadatak 38-a
# Саставити програм који употребом WHILE петље исписује:
# a)  све бројеве прве десетице

# Иницијализација бројачке променљиве - постављамо почетну вредност на 1
# 'i' представља бројач који ће се инкрементирати у свакој итерацији
i = 1

# Почетак while петље
# Услов: петља ће се извршавати све док је вредност променљиве 'i' мања или једнака 10
# Петља се извршава док је услов истинит (враћа True)
while i <= 10:
    # Тело петље - код који се извршава у свакој итерацији

    # print функција - исписује тренутну вредност бројача 'i'
    # Параметри: "i =" је текстуални део који се исписује, i је променљива чија се вредност приказује
    # Повратна вредност: None (print функција не враћа вредност, само исписује на екран)
    print("i =", i)

    # Инкрементирање бројача - повећавамо вредност 'i' за 1 након сваког исписа
    # Ова линија је кључна за избегавање бесконачне петље
    i = i + 1

# Крај програма - када услов while петље постане нетачан (i > 10),
# програм наставља извршавање испод петље
