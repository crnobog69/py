```python
def proveri_limit(recenica, limit, naslov):
    """Proverava broj karaktera u recenici u odnosu na limit i prikazuje rezultat."""
    broj_karaktera = len(recenica)
    preostalo = limit - broj_karaktera

    print("\n" + "-" * 40)
    print(f"{naslov:^40}")
    print()
    print(f'Унета реченица: "{recenica}"')
    print(f"Број карактера: {broj_karaktera}")

    if broj_karaktera <= limit:
        print(f"Преостало до лимита: {preostalo} карактера")
    else:
        print(f"Прекорачење лимита за: {abs(preostalo)} карактера")

    print("-" * 40)


def main():
    while True:
        recenica = input("\nУнесите реченицу: ").strip()

        print("\nИзаберите опцију:")
        print("1. Провери за ИМЕ ДАТОТЕКЕ (лимит: 20 карактера)")
        print("2. Провери за БРОЈ ТЕКУЋЕГ РАЧУНА (лимит: 18 карактера)")
        print("3. Провери за ЈЕДИНСТВЕНИ МАТИЧНИ БРОЈ ГРАЂАНА (лимит: 13 карактера)")
        print("4. Провери за ПЛАТА (лимит: 23 карактера)")
        print("5. Провери УКУПНО (лимит: 136 карактера)")
        print("6. Изађи из програма")

        izbor = input("Унесите број опције: ")

        if izbor == "1":
            proveri_limit(recenica, 20, "ИМЕ ДАТОТЕКЕ")
        elif izbor == "2":
            proveri_limit(recenica, 18, "БРОЈ ТЕКУЋЕГ РАЧУНА")
        elif izbor == "3":
            proveri_limit(recenica, 13, "ЈЕДИНСТВЕНИ МАТИЧНИ БРОЈ ГРАЂАНА")
        elif izbor == "4":
            proveri_limit(recenica, 23, "ПЛАТА")
        elif izbor == "5":
            proveri_limit(recenica, 136, "УКУПНО")
        elif izbor == "6":
            print("Програм је завршен.")
            break
        else:
            print("Неважећа опција. Молимо покушајте поново.")


if __name__ == "__main__":
    main()

```
