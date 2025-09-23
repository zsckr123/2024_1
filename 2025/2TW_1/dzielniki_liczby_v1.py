liczba = int(input('Podaj liczbe'))
lista_dzielnikow = []
for i in range(2,liczba):
    if liczba % i == 0:
        lista_dzielnikow.append(i)
print(f'Lista dzielnikow liczby {liczba} wynosi {lista_dzielnikow}')