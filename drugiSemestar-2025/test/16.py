# 16

godine = int(input("Unesite broj vasig godina: "))

if godine >= 100:
    print("Previse ste stari da bi ste se prijavili.")
elif godine >= 18:
    print("Sada ste prijavljeni.")
elif godine < 0:
    print("Niste rodjeni!")
else:
    print("Morate imate 18+ godina da bi ste se prijavaili.")
