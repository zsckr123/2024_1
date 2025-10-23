def a(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return a(n-1)/a(n-2)

for i in range(1,11):
    print(f'a({i})={a(i)}')