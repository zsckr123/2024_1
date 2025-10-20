def a(n):
    if n>=2:
        return a(n-1)+(n-1)
    return 1

for i in range(1,11):
    print(f'a({i})={a(i)}')