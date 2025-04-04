
a = input('Wprowadź tekst do zmiennej a')
b = input('Wprowadź tekst do zmiennej b')
print(f' Drukowanie zmiennej a: {a} ')
print(f' Drukowanie zmiennej b: {b} ')
# # ''' Ile znaków ma tekst w zmiennej a'''
print(f'długość napisu "{a}" {len(a)}')
print(f'długość napisu "{b}" {len(b)}')

#
# ''' Łączenie napisów '''
c = a + b
d = b + a
print(f'{a} + {b}: "{c}"')
print(f'{b} + {a}: "{d}"')

# #
# # ''' Powielanie napisów'''
print('Powielanie napisów')
print(20 * 'x-')