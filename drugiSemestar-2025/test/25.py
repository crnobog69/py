# 25

ime = input("Унесите ваше пуно име: ")

rezultat1 = len(ime)
print(rezultat1)

print()

rezultat2 = ime.find(" ")
print(rezultat2)

print()

rezultat3 = ime.find("m")
print(rezultat3)

print()

rezultat4 = ime.rfind("a")
print(rezultat4)

print()

rezultat5 = ime.rfind("q")
print(rezultat5)

print()

rezultat6 = ime.capitalize()
print(rezultat6)

print()

rezultat7 = ime.upper()
print(rezultat7)

print()

rezultat8 = ime.lower()
print(rezultat8)

print()

rezultat9 = ime.isdigit()
print(rezultat9)

print()

# Бразан карактер НИЈЕ карактер у алфабету
rezultat10 = ime.isalpha()
print(rezultat10)

print()

brojTelefona = input("Унесите Ваш број телефона: ")
rezultat11 = brojTelefona.count("-")
print(rezultat11)

print()

rezultat12 = brojTelefona.replace("-", " ")
print(rezultat12)

# print(help(str))
