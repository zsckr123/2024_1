liczba = int(input('Podaj liczbe'))
lista_dzielnikow = []
for i in range(2,int(liczba/2)+1):
    if liczba % i == 0:
        lista_dzielnikow.append(i)
print(f'Lista dzielnikow liczby {liczba} wynosi {lista_dzielnikow}')