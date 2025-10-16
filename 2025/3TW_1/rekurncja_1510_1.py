def a(n):
    if n==1:
        return 1
    return a(n-1)**2 - (n-1) 


for i in range(1,6):
    print(a(i))
