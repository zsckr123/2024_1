def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    return 1
n = int(input('Podaj n='))
# print(len(str(silnia(n))),silnia(n))

print(silnia(n))


''' silnia(5) = 5 * silnia(4)
ale silnia(4) = 4 * silnia(3)
ale silnia(3) = 3 * silnia(2)
ale silnia(2) = 2 * silnia(1)
zatem zbieramy silnia(1) = 1'''