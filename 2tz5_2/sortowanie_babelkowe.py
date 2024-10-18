import time
import random
def babelek(t):
  for i in range(len(t)-1):
    if t[i] > t[i+1]:
      t[i], t[i+1] = t[i+1], t[i] #  przestawienie elementów
  return t


def sort_b(t):
    start = time.time()
    for j in range(len(t)):
        babelek(t)
    stop = time.time()
    delta = stop - start
    return t, delta

lista = []
for _ in range(100000):
    liczba = random.randint(-100000,100000)
    lista.append(liczba)

# print(sorted(lista,reverse=True))
print('Lista nieposortowana ', lista)
print(sort_b(lista)[0])
print('Czas wykonania ', sort_b(lista)[1])