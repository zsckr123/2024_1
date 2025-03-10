''' Pole prostokąta'''

def pole_trojkata( a, b):
    return a*b/2

a=float(input('Podaj podstawę:'))
b=float(input('Podaj wysokość:'))

print('Pole wynosi' , pole_trojkata(a,b))