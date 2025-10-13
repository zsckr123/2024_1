def silnia(n):
    if n > 1:
        return n * silnia(n-1)
    return 1

for n in range(1,40):
    print(f"silnia({n})={silnia(n)}")