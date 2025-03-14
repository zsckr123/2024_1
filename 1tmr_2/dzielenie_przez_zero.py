def iloraz(x,y):
    if y==0:
        return 'Dzielnie niewykonalne'
    return x / y



a=float(input('Podaj pierwszą liczbę:'))
b=float(input('Podaj drugą liczbę:'))
print('Iloraz:  ', iloraz(a,b))