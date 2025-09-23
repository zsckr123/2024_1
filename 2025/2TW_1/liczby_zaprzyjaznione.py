# Liczby zaprzyjaznione
'''Liczby zaprzyjaźnione – para różnych liczb naturalnych, 
takich że suma dzielników właściwych 
każdej z tych liczb równa się drugiej liczbie. '''
liczba = int(input('Podaj liczbe'))
suma =0
for i in range(1,liczba):
    if liczba % i == 0:
        suma +=i
print(f'Suma dzielnikow wlasciwych liczby {liczba} wynosi {suma}')