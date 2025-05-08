'''
Utwórz funkcję która wyświetla kod ASCII dowolnego znaku .

Funkcja musi posiadać argument .
'''

def ascii(znak):
    return ord(znak)

z = input('Podaj pojedyńczy znak')
print(ascii(z))