''' Zamiana na inny system '''
# 1100  2^0 2^1 , 2^2, 2^3
liczba_w_innym_systemie = [1,3,4]
podstawa = int(input('Podaj podstawę'))
liczba_10 = 0
potega = 0
for i in liczba_w_innym_systemie[::-1]:
    liczba_10 += i * podstawa ** potega
    potega +=1
print(f'Liczba w systemie o podstawie {podstawa}: {liczba_10}')