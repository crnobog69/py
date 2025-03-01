# 29

ime = input("Унесите ваше име: ")

while ime == "":
    print("Нисте унели ваше име.")
    # ESCAPE секвенца
    ime = input("Унесите ваше име: ")
else:
    print(f"Здраво, {ime}!")

godine = int(input("Увесите ваше године: "))

while godine < 0:
    print("Године не могу да буду негативне.")
    # ESCAPE секвенца
    године = int(input("Увесите ваше године: "))
else:
    print(f"Имате {godine}!")

hrana = input("Унесите храну коју волите (q за излазак): ")

# while not hrana == "q":
#     print(f"Волите {hrana}!")
#     hrana = input("Унесите храну коју волите (q за излазак): ")

while True:
    if hrana == "q":
        break  # Користите бреак уместо exit() да бисте изашли из петље
    else:
        print(f"Волите {hrana}!")
        hrana = input("Унесите храну коју волите (q за излазак): ")

print("пој")

broj = int(input("Унесите број између 1 и 10: "))

while broj < 1 or broj > 10:
    print(f"{broj} није валидан.")
    broj = int(input("Унесите број између 1 и 10:"))

print("Браво!")
