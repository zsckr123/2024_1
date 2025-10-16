def a(n):
    if n > 1 :
        return a(n-1) + 5
    return 2
n = int(input('Podaj n'))
for i in range(1,11):
    print(a(i))