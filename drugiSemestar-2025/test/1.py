import sys

broj = input("Unesite trocifreni broj: ")

# Provjera uslova
if len(broj) != 3:
    print("Greška: Morate unijeti tačno tri cifre!")
    sys.exit(1)

print(f"Stotine: {broj[0]}")
print(f"Desetice: {broj[1]}")
print(f"Jedinice: {broj[2]}")