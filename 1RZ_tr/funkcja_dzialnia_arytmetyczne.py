def arytmetyka(a, b):
    print(f'Działania arytmetyczne dla liczb {a} i {b}')
    print(f'Wynik dodawania= {a+b}')
    print(f'Wynik odejmowania= {a-b}')
    print(f'Wynik mnożenia= {a*b}')
    if b==0:
        print('Dzielnie nie wykonalne')
    else:
        print(f'Wynik dzielenia= {a/b}')
    print('xxxxxxxxxxxxxxxxxxxx')


arytmetyka(2,0)
arytmetyka(2,3)
arytmetyka(2,4)
arytmetyka(2,6)
arytmetyka(2,12)
