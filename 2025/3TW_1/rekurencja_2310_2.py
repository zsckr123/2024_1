def a(n):
    if n==1:
        return 2
    if n==2:
        return 4
    return (a(n-1)+a(n-2))/2

for i in range(1,21):
    print(f'a({i})={a(i)}')