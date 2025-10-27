import random, time
def babelek(t):
  for i in range(len(t)-1):
    if t[i] < t[i+1]:
      t[i], t[i+1] = t[i+1], t[i] #  przestawienie elementów
  return t


def sort_b(t):
    for j in range(len(t)):
        babelek(t)
    return t


lista1 = [i for i in range(-1000,random.randint(5000,10000))]
start = time.time()
sorted(lista1, reverse=True)
stop = time.time()
print('Czas sortowanie metody wbudowanej sorted', stop - start)
# print('lewy koniec listy' , lista1[0])
# print('prawy koniec listy' , lista1[-1])
# print(lista1)
# print(sorted(lista1, reverse=True))
pocz = time.time()
sort_b(lista1)
koniec = time.time()
print('sortowanie babelkowe',koniec-pocz)
print('ilosc elementow', len(lista1))
#  Sortowanie przez wstawianie

import time
import random
def sort_insert(A):
    start = time.time()
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz: # zmiana znaku = zmiana typu sortowania
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    delta = time.time() - start
    print(f'Czas sortowania przez wstawianie {delta}')
    return A

sort_insert(lista1)


# pocz = time.time()
# sorted(lista1, reverse=True)
# koniec = time.time()
# print('sortowanie wbudowane',koniec-pocz)
# print('ilosc elementow', len(lista1))