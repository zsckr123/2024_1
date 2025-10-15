def a(n):
    if n==1:
        return 2
    return 2*a(n-1)-1


for i in range(1,10):
    print(f'a({i})={a(i)}')