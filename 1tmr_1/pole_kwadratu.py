''' Pole kwadratu'''

def pole_kwadratu( bok):
    return bok ** 2

a = int(input('podaj długość boku '))
print('Pole wynosi' , pole_kwadratu(a))