# 23

temp = 40

if temp > 0 and temp < 30:
    print("Температура је добра.")
else:
    print("Температура је лоша.")

if temp > 0 or temp < 30:
    print("Температура је добра.")
else:
    print("Температура је лоша.")

print("\n")

suncano = True

# Овде ће одговоре бити: `Сунчано је вани`
if suncano:
    print("Сунчано је вани.")
else:
    print("Облачно је вани.")

# Овде че оговор бити: `Облчачно је вани`
if not suncano:
    print("Сунчано је вани.")
else:
    print("Облачно је вани.")
