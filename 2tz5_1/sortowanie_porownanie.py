import time
import random
from random import random, randint


def sort_insert(A):

    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j >= 0 and A[j] > klucz: # zmiana znaku = zmiana typu sortowania
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz

    return A

def babelek(t):
  for i in range(len(t)-1):
    if t[i] > t[i+1]:
      t[i], t[i+1] = t[i+1], t[i] #  przestawienie elementów
  return t


def sort_b(t):
    for j in range(len(t)):
        babelek(t)
    return t


lista =[]
for _ in range(10000):
    liczba = randint(-100000,100000)
    lista.append(liczba)
print('Lista nieposortowana ')
print(20*'-')
print(lista)
print('Lista posortowana. Metoda przez wstawianie')
print(20*'-')
start = time.time()
print(sort_insert(lista))
stop = time.time()
print('Czas sorotowania ', stop - start)
print('Lista posortowana. Metoda bąbelkowa')
print(20*'-')
start = time.time()
print(sort_b(lista))
stop = time.time()
print('Czas sorotowania ', stop - start)
print('Sortowanie wbudowane w Python. Metoda sorted')
start = time.time()
print(sorted(lista))
stop = time.time()
print('Czas sorotowania ', stop - start)

