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

lista =[100,100,-200,6,500]
lista1 = [i for i in range(-1000,random.randint(5000,100000))]
print('lewy koniec listy' , lista1[0])
print('prawy koniec listy' , lista1[-1])
# print(lista1)
# print(sorted(lista1, reverse=True))
pocz = time.time()
sort_b(lista1)
koniec = time.time()
print('sortowanie babelkowe',koniec-pocz)
print('ilosc elementow', len(lista1))

pocz = time.time()
sorted(lista1, reverse=True)
koniec = time.time()
print('sortowanie wbudowane',koniec-pocz)
print('ilosc elementow', len(lista1))