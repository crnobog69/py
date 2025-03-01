# 5

# Подразумевано ће постати ниска (string) ако експлицитно не ставимо врсту податка испред 'input'

ime = input("Унесите ваше име: ")
godine = input("Унесите ваш број година: ")

# godine = int(input("Unesite vas broj godina: "))

godine = int(godine)
godine = godine + 1

print(f"Здраво, {ime}!")
print(f"Имате {godine}!")
