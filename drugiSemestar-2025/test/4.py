# 💱

## Експлицитно претварање из вредности у другу

ime = "Lain"
godine = 18
prosecna_ocena = 4.9
student = True

print("Tip:", type(ime), "\n", "Vredost:", ime)
print("Tip:", type(godine), "\n", "Vredost:", godine)
print("Tip:", type(prosecna_ocena), "\n", "Vredost:", prosecna_ocena)
print("Tip:", type(student), "\n", "Vredost:", student)

print("\n ")

godine = float(godine)
print("Tip:", type(godine), "\n", "Vredost:", godine)

prosecna_ocena = int(prosecna_ocena)
print("Tip:", type(prosecna_ocena), "\n", "Vredost:", prosecna_ocena)

student = str(student)
print("Tip:", type(student), "\n", "Vredost:", student)

student_2 = True
student_2 = int(student_2)
print("Tip:", type(student_2), "\n", "Vredost:", student_2)

print("\n ")

godine_2 = 18  # True
godine_2 = bool(godine_2)
print("Tip:", type(godine_2), "\n", "Vredost:", godine_2)

godine_3 = 0  # False
godine_3 = bool(godine_3)
print("Tip:", type(godine_3), "\n", "Vredost:", godine_3)

ime_2 = "Lain"  # True
ime_2 = bool(ime_2)
print("Tip:", type(ime_2), "\n", "Vredost:", ime_2)

ime_3 = ""  # False
ime_3 = bool(ime_3)
print("Tip:", type(ime_3), "\n", "Vredost:", ime_3)

ime_4 = " "  # True
ime_4 = bool(ime_4)
print("Tip:", type(ime_4), "\n", "Vredost:", ime_4)

print("\n")

# Имплицитно претварање из вредности у другу

x = 2
y = 2.0

x = x / y

#
print(x)
