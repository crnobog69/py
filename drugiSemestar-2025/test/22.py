# 22

mernaJedinica = input("Да ли је температура у Целзијусима или Фаренхајтима? (C/F): ")
temperatura = float(input("Унесите температуру: "))

if mernaJedinica == "C" or mernaJedinica == "c":
    temperatura = round((9 * temperatura) / 5 + 32, 1)
    print(f"Температура у Фаренхајтима је: {temperatura} °F")
elif mernaJedinica == "F" or mernaJedinica == "f":
    temperatura = round((temperatura - 32) * 5 / 9, 1)
    print(f"Температура у Целзијусима је: {temperatura} °C")
else:
    print(f"{mernaJedinica} није подржана јединица.")
