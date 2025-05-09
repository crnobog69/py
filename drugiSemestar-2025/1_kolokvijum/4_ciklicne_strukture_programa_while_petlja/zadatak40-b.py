# Zadatak 40
# Саставити програм којим се:
# б) израчунава и исписује сума првих n елемената Фибоначијевог низа.
# Фибоначијев низ је: f1=1, f2=1, fi=fi-1+fi-2,    i=3, 4, 5, ...

# Учитавамо број n (број елемената Фибоначијевог низа чију суму рачунамо)
# Функција int() конвертује унети стринг у цео број
# Параметар: корисников унос; Повратна вредност: цео број
broj_elemenata = int(input("n = "))

# Иницијализација променљивих
# brojac - бројач који пратимо да бисмо знали до ког елемента смо стигли
brojac = 3
# prvi_broj - први број у Фибоначијевом низу (f1=1)
prvi_broj = 1
# drugi_broj - други број у Фибоначијевом низу (f2=1)
drugi_broj = 1
# suma - сума првих елемената низа, иницијализујемо на 2 јер су први и други елемент 1+1=2
suma = 2

# Петља која рачуна елементе Фибоначијевог низа почевши од трећег (f3)
# Услов: настављамо док не израчунамо n-ти елемент
while brojac <= broj_elemenata:
    # Израчунавамо следећи број Фибоначијевог низа као збир претходна два
    sledeci_broj = prvi_broj + drugi_broj
    # Додајемо израчунати број у укупну суму
    suma = suma + sledeci_broj
    # Припремамо се за следећу итерацију - померамо бројеве
    # први број постаје други број
    prvi_broj = drugi_broj
    # други број постаје следећи број
    drugi_broj = sledeci_broj
    # Повећавамо бројач за 1 јер смо израчунали још један елемент низа
    brojac = brojac + 1

# Исписујемо резултат - суму свих првих n елемената Фибоначијевог низа
# f-string омогућава уметање вредности променљиве унутар стринга
print(f"Сума = {suma}")
