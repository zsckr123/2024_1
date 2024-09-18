''' Dzielimy liczba1 przez liczba2 NWD(liczba1, liczba2) '''
liczba1 = int(input('podaj pierwszą liczbę: '))
liczba2 = int(input('podaj drugą liczbę: '))

if liczba2 == 0:
      print("NWD to:",liczba1)
else:
    while liczba2 > 0:
        reszta = liczba1 % liczba2
        liczba1 = liczba2
        liczba2 = reszta

# koniec pętli
print("najwiekszy wspolny dzielnik to:",liczba1)