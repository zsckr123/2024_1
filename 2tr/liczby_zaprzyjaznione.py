# Liczby zaprzyjaznione
liczba = int(input('Podaj liczbe'))
suma =0
for i in range(1,liczba):
    if liczba % i == 0:
        suma +=i
print(f'Liczba zaprzyjazniona z  {liczba} to:  {suma}')