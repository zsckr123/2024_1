'''
a1=1
a2=2
a(n+2)=a(n+1)/a(n)
 a(n) = a(n-1) / a(n-2)
.... a(n-3)  a(n-2)   a(n-1)   a(n)  a(n+1)  a(n+2) ....
'''

def ciag(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return ciag(n-1) / ciag((n-2))

print(ciag(100))