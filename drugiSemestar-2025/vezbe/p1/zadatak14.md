```python
# Zadatak 14

sek = int(input("Uneti vreme u sekundama: "))

# променљива 'sek' је укупан број секунди

# потребно је број секунди поделити данима израженим у секундама
dan = sek // 86400  # jedan dan ima 24 * 60 * 60 = 86400 sekundi

# остатак дељења потребно је порделити сатима израженим у секундама
sat = (sek % 86400) // 3600  # jedan sat ima 60 8 60 = 3600 sekundi

# остатак дељења потребно је поделити минутима израженим у секундама
minut = ((sek % 86400) % 3600) // 60

# остатак дељења ће представљати број секунди
sekunda = ((sek % 86400) % 3600) % 60

print("Dani:", dan, "; Sati:", sat, "; Minuti:", minut, "; Sekunde:", sekunda)

```