# 4

# 💱

## Експлицитно претварање из вредности у другу

ime = "Lain"
godine = 18
prosecna_ocena = 4.9
student = True

print("Тип:", type(ime), "\n", "Вредост:", ime)
print("Тип:", type(godine), "\n", "Вредост:", godine)
print("Тип:", type(prosecna_ocena), "\n", "Вредост:", prosecna_ocena)
print("Тип:", type(student), "\n", "Вредост:", student)

print("\n ")

godine = float(godine)
print("Тип:", type(godine), "\n", "Вредост:", godine)

prosecna_ocena = int(prosecna_ocena)
print("Тип:", type(prosecna_ocena), "\n", "Вредост:", prosecna_ocena)

student = str(student)
print("Тип:", type(student), "\n", "Вредост:", student)

student_2 = True
student_2 = int(student_2)
print("Тип:", type(student_2), "\n", "Вредост:", student_2)

print("\n ")

godine_2 = 18  # True
godine_2 = bool(godine_2)
print("Тип:", type(godine_2), "\n", "Вредост:", godine_2)

godine_3 = 0  # False
godine_3 = bool(godine_3)
print("Тип:", type(godine_3), "\n", "Вредост:", godine_3)

ime_2 = "Lain"  # True
ime_2 = bool(ime_2)
print("Тип:", type(ime_2), "\n", "Вредост:", ime_2)

ime_3 = ""  # False
ime_3 = bool(ime_3)
print("Тип:", type(ime_3), "\n", "Вредост:", ime_3)

ime_4 = " "  # True
ime_4 = bool(ime_4)
print("Тип:", type(ime_4), "\n", "Вредост:", ime_4)

print("\n")

# Имплицитно претварање из вредности у другу

x = 2
y = 2.0

x = x / y

#
print(x)
