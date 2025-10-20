import random
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
# lista1 = [i for i in range(1,random.randint(1,10000))]
# print(lista1)
# print(sorted(lista, reverse=True))
print(sort_b(lista))