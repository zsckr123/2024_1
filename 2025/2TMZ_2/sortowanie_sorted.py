import random, time
lista = []
for _ in range(1000):
    liczba = random.randint(-100000,100000)
    lista.append(liczba)
pocz = time.time()
sorted(lista)
koniec = time.time()
print(koniec-pocz)