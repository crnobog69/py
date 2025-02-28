# 5

# Подразумевано ће постати ниска (string) ако експлицитно не ставимо врсту податка испред 'input'

ime = input("Unesite vase ime: ")
godine = input("Unesite vas broj godina: ")

# godine = int(input("Unesite vas broj godina: "))

godine = int(godine)
godine = godine + 1

print(f"Zdravo, {ime}!")
print(f"Imate {godine}!")
