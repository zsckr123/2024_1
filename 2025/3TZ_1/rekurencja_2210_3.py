def d(n):
    if n==1:
        return -10
    return d(n-1)+9


for i in range(1,11):
    print(f'd({i})={d(i)}')