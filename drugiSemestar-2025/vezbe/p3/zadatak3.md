```python
# Задатак 39
# Програм израчунава суму бројева дељивих са 6 од 1 до н

gornja_granica = int(input(" n = "))  # Учитавамо број н са тастатуре

tekuci_broj = 1  # Бројач који почиње од 1
suma = 0  # Променљива у којој чувамо суму

# Петља која иде од 1 до н
while tekuci_broj <= gornja_granica:
    if tekuci_broj % 6 == 0:  # Проверавамо да ли је број дељив са 6
        suma = suma + tekuci_broj  # Додајемо број суми ако је дељив са 6
    tekuci_broj = tekuci_broj + 1  # Повећавамо бројач

print(f" Сума = {suma}")  # Исписујемо коначну суму

```