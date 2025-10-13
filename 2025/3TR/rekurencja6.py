def ciag(n):
    if n >1:
        return ciag(n-1) +(n-1)
    return 1



print(ciag(6))