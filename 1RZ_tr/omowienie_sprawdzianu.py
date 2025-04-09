''' Zadanie 1'''
print('dziś jest środa')
'''Zadanie 2'''
''' Wykonaj mnożenie dwóch 
liczb całkowitych wprowadzonych z klawiatury.'''
a = int(input('PodaJ pierwszą liczbę'))
b = int(input('PodaJ pierwszą liczbę'))
print('Iloczyn liczb', a*b)

''' Zadanie 3'''
'''Utwórz funkcję która oblicza pole dowolnego kwadratu.

Oblicz pole dowolnego kwadratu za pomocą tej funkcji.'''

# def pole_kwadratru():
#     x = int(input('Podaj `bok'))
#     return x**2
#
# print(pole_kwadratru())
# Drugi sposób

def pole_kwadratru(x):

    return x**2
x = int(input('Podaj `bok'))
print(pole_kwadratru(x))