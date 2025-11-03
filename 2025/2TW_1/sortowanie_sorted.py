import random, time

lista = []
for _ in range(100):
    liczba = random.randint(-100000,100000)
    lista.append(liczba)
start = time.time()
sorted(lista)
end = time.time()
print(end-start)