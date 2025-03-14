''' Pole prostokąta'''

def pole_prostokata( x, y):
    if x<=0 or y<=0:
        return ' Obliczenie pole nie możliwe'
    return f' Pole wynosi {x * y}'

a=float(input('Podaj pierwszy bok:'))
b=float(input('Podaj pierwszy bok:'))

print(pole_prostokata(a,b))