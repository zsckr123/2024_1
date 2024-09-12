''' Dzielimy liczba1 przez liczba2 '''
while True:
    liczba1 = int(input('podaj pierwszą liczbę: '))
    liczba2 = int(input('podaj drugą liczbę: '))

    if liczba2 == 0:
          print("NWD = ", liczba1)
    else:
        while liczba2 > 0:
            reszta = liczba1 % liczba2
            liczba1 = liczba2
            liczba2 = reszta
        print("najwiekszy wspolny dzielnik to:", liczba1)
    key = input('Podaj x aby zakończyć')
    if key == 'x':
        break

# koniec pętli